#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 19/03/2020 09:13

pyrename.py - Rename files, based on a pattern provided.
       
@author: opujo
"""

import os, argparse, re, shutil, time

desc = """Rename files, searching a pattern provided and replacing by 
a replace string or sequence..
"""
epi= """The string to replace can use the groups detected by the pattern 
regular expression, by using \\1 for 1st group, \\2 for second group, etc. 
In order to do that, you need to ensure your pattern includes the groups you 
want to reuse. Example: 
    pyrename "\\d\\d(\\d\\d)-(\\d\\d)-(\\d\\d)" "\\1\\2\\3" 

would transform an ISO date to a 6-digit date.'
"""

def get_parameters(original, path, filename):
    """transforms string with % into regex. Considers the following parameters:
          %d[d[d[d[...]]]]: sequence of numbers
    """
    global seq_counter
    
    fullfilename = os.path.join(path, filename)
    
    seq_regex = re.compile('<d+>')
    seq_match = seq_regex.search(original)
    
    date_regex = re.compile('<date(\[.+\])?>')
    date_match = date_regex.search(original)

    final = original
    if seq_match:
        seq_counter += 1
        num_digits = seq_match.group(0).count('d')
        digits = f'{seq_counter:0{num_digits}d}'
        final = seq_regex.sub(digits, final)
    
    if date_match:
        date = time.localtime(os.path.getatime(fullfilename))
        fmt = date_match.group(1) if date_match.group(1) else "[ymd]"
        for c in "yYmdHMS":
            fmt = fmt.replace(c, '%'+c)
        date_str = time.strftime(fmt[1:-1], date)
        final = date_regex.sub(date_str, final)
        
    return final


parser = argparse.ArgumentParser(description=desc, epilog=epi,
                                 formatter_class=argparse.RawDescriptionHelpFormatter,)

parser.add_argument("folder", help="Folder to start the search on.")
parser.add_argument("pattern", help="Pattern to search for, it should be \
                    a regular expression.")
parser.add_argument("replace", help="String to replace the pattern. See below for\
                    a description of possible syntax.")

parser.add_argument('-R', '--recursive', action='store_true', 
                    help='Do the search recursively.')
parser.add_argument('-i', '--ignorecase', action='store_true', 
                    help='Search pattern ignoring case.')
parser.add_argument("-f", "--folders", action='store_true', 
                    help="Do the rename on folders instead of filenames")

args = parser.parse_args()

if args.ignorecase:
    regex = re.compile(args.pattern, re.IGNORECASE)
else:
    regex = re.compile(args.pattern)

numfileRegex = re.compile(r'\((\d+)\)$') # used to avoid duplication of files
replace_string = args.replace
seq_counter = 0

#start recursive search (if not recursive will break)
for foldername, subfolders, files in os.walk(args.folder):
    if args.folders:
        list_obj = subfolders
    else:
        list_obj = files
    
    for obj in list_obj:
        if regex.search(obj):
            if '<' in args.replace:
                replace_string = get_parameters(args.replace, foldername, obj)
            new_name = regex.sub(replace_string, obj)
            while os.path.isfile(new_name):
                mo = numfileRegex.search(new_name)
                if mo:
                    num = int(mo.group(1))
                    new_name = numfileRegex.sub(f'({num+1})', new_name)
                else:
                    new_name += '(1)'
            
            print(f'renaming "{obj}" to "{new_name}"')
            shutil.move(os.path.join(foldername, obj), 
                        os.path.join(foldername, new_name))
    
    #if recursive is False, it will stop at the first iteration
    if not args.recursive:
        break

