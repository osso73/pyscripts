#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 12/03/2020 12:22

grep.py - searches all files in current folder for lines that match 
a certain regular expression introuced by the user.

see usage below
    
@author: opujo
"""
DESCRIPTION = """Usage: grep files pattern
    
where:
    files is the list of files, including path
    pattern is the regex to search for. If it contains spaces or 
       special characters, put between ""
    
Example: grep c:\scripts\*.py "^import"
"""

import re, sys
from pathlib import Path

# read regex from the command line arguments
if len(sys.argv) < 3:
    print(DESCRIPTION)

else:
    path = Path(sys.argv[1])
    regex = re.compile(" ".join(sys.argv[2:]))
    
    p = path.parent if path.parent != Path('.') else Path.cwd()
    g = path.name
    
    print(f'Searching in {p}\\{g}')
    
    # get list of files of current folder
    filelist = list(p.glob(g))
    
    # search for pattern in each file
    num = 0
    for file in filelist:
        try:
            with open(file, 'r') as f:
                contents = f.readlines()
        except PermissionError:
            continue
        for line in contents:
            match = regex.search(line)
            if match:
                print(f'{file.name}: {line}', end='')
                num += 1
    
    print(f'\n{num} matches found.')