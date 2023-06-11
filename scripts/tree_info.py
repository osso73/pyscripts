#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 20:34:34 2021

tree_info.py: provide information about a tree in the filesystem. For each
branch it provides the number of files and total size of all folders below.

@author: osso73
"""

import os, argparse


def command_line():
    """setup argparse variables and help, return arguments"""
    
    desc = 'provide information about a tree in the filesystem. For each \
        branch it provides the number of files and total size of all folders \
        below.'
    epi= ''
    parser = argparse.ArgumentParser(description=desc, epilog=epi)
    
    parser.add_argument("starting", nargs='?', default='.',
                        help="Path of folder to query")
    parser.add_argument('-d', '--depth', help='Depth of the tree to show.', 
                        type=int)
    
    args = parser.parse_args()
    if not os.path.isdir(args.starting):
        parser.error("The path is not a valid path. Type 'tree_info --help'\n" +
                     "for additional information.")
    
    # remove potential trailing / to avoid errors
    args.starting = os.path.abspath(args.starting)

    return args



def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''
    Convert a file size to human-readable form. Function taken from:
    https://diveinto.org/python3/your-first-python-program.html#divingin

    Parameters
    ----------
    size : int
        file size in bytes.
    a_kilobyte_is_1024_bytes : boolean, optional
        if True (default), use multiples of 1024.
        if False, use multiples of 1000.

    Raises
    ------
    ValueError
        If the number provided is larger than YiB.

    Returns
    -------
    string
        The size formatted in human readable form.

    '''

    SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
                1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')


def add_subdirs(tree):
    '''
    Adds the totals (directories, files and size) of the subdirectories to
    the current directory numbers.

    Parameters
    ----------
    tree : dictionary
        Contains the data of the folder, and a dictionary for each of the
        subfolders

    Returns
    -------
    None.

    '''
    if tree['__data__'][0]:
        for subdir in tree:
            if subdir == '__data__':
                continue
            add_subdirs(tree[subdir])
            tree['__data__'] = [ i+j for i,j in zip(tree['__data__'], 
                                                   tree[subdir]['__data__']) ]

    
def show_tree(tree, name='top', level=0, max_level=None):
    '''
    Print information from the tree, to the level indicated. It is a 
    recursive function, that will call itself for each subfolder found.

    Parameters
    ----------
    tree : dict
        Dictionary containing all the information of the subfolders. Each 
        subfolder is itself a dictionary containing one key '__data__' with
        the info about # folders, # files, and total size of the that folder
        and its subfolders; and one key for each of the subfolders.
    name : string, optional
        Name of the folder, this is what is printed. The default is 'top'.
    level : int, optional
        Level of the folder, compared to the top. This info is used to indent
        when printing the name of the folder. The default is 0.
    max_level : int, optional
        Maximum level to be printed. The function will stop after level 
        levels. The default is None, which will print all levels.

    Returns
    -------
    None.

    '''
    if max_level:
        if level >= max_level:
            return
        
    for subdir in tree:
        if subdir == '__data__':
            prefix = '│  '*level + '\u2514\u2500' if level else ''
            d, f, s = tree["__data__"]
            d_name = 'directory' if d==1 else 'directories'
            f_name = 'file' if f==1 else 'files'
            s = approximate_size(s)
            print(f'{prefix}{name}: {d:,} {d_name} // {f:,} {f_name} // {s}', sep='')
        else:
            show_tree(tree[subdir], subdir, level+1, max_level)


def get_attributes(tree, folder):
    '''
    Get data of a folder. This is a recursive function, that will call itself
    for each of the subfolders.

    Parameters
    ----------
    tree : dict
        Contains the folder information: first key is '__data__', which 
        contains a list with number of folders, number of files, and total
        size of the folder. Create a key for each subfolder, that is a
        dictionary itself following the same structure.
    folder : string
        Folder that is explored.

    Returns
    -------
    None.

    '''
    num_dirs = num_files = size = 0
    tree['__data__'] = []
    for f in os.scandir(folder):
        if f.is_dir():
            num_dirs += 1
            tree[f.name] = dict()
            get_attributes(tree[f.name], os.path.join(folder, f.name))
        else:
            num_files += 1
            size += f.stat().st_size
    tree['__data__'] = [num_dirs, num_files, size]


def build_unit_tree(folder):
    '''
    Start building the top tree. The subfolders will be triggered by the
    recursive function, until all subfolders' info is populated.

    Parameters
    ----------
    folder : string
        Folder to start exploration.

    Returns
    -------
    tree : dictionary
        Tree with the information of the folder and its subfolders.

    '''
    tree = dict()
    get_attributes(tree, folder)
    return tree


def main():
    """main program"""
    
    args = command_line()
    print('Searching ... ', args.starting)
    tree_unit = build_unit_tree(args.starting)
    tree_total = dict(tree_unit)
    add_subdirs(tree_total)
    top = os.path.basename(args.starting)
    
    show_tree(tree_total, top, max_level=args.depth)
    

if __name__ == '__main__':
    main()
