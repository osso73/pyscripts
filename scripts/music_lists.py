#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 02/04/2022 13:41

music_lists.py - searches music list files (.m3u) in a particular and replaces
the character '\' by character '/', to allow usage of lists on a linux/unix
OS. This is needed for my streaming server running on FreeBSD.

see usage below
    
@author: opujo
"""

import argparse
import os


def command_line():
    """setup argparse variables and help, return arguments"""

    desc = 'Searches music list files (.m3u) in a particular and replaces \
        the character "\" by character "/", to allow usage of lists on a \
        linux/unix OS.'
    
    epi= ''' '''
    parser = argparse.ArgumentParser(description=desc, epilog=epi, 
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument('-f', '--folder', help="Folder containing the .m3u \
                        files. By default: 'Z:\\03. Music'")
    
    return parser.parse_args()

def replace_char(file, char_original, char_new):
    """ open file, and replace any instance of char_original by new_char """
    with open(file, 'rt', encoding='utf8') as f:
        contents = f.read()
    new_contents = ''
    for char in contents:
        if char == char_original:
            new_contents += char_new
        else:
            new_contents += char
    
    with open(file, 'wt', encoding='utf8') as f:
        f.write(new_contents)

        

def main():
    args = command_line()
    folder = args.folder if args.folder else r"Z:\03.Musica"
    if not os.path.isdir(folder):
        print(f"{folder} is not a valid folder name. Please provide a valid folder name.")
    files = os.listdir(folder)
    for f in files:
        if f.endswith('m3u'):
            print(f'Processing {f}... ', end='')
            full_path = os.path.join(folder, f)
            replace_char(full_path, '\\', '/')
            print('Done!')
    
    

if __name__ == '__main__':
    main()