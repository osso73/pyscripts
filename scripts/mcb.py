#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 12/03/2020 12:22

mcb.py - Multiclipboard: puts text in clipboard, based on short key value
Usage: mcb save <keyword> - Saves clipboard to keyword.
       mcb del <keyword> - Deletes keyword
       mcb <keyword> - Loads keyword to clipboard.
       mcb list - Loads a list of all keywords to clipboard.
       
@author: opujo
"""
# folder to save the config. Change as needed
SAVE_CONFIG = r'C:\Cloud\Data\Programacion\Python\scripts'

import sys, pyperclip, shelve

#read command line and open saved file
args = sys.argv[1:]
text = shelve.open(SAVE_CONFIG + r'\mcb')

if not len(args) or len(args)>2 or args[0].lower() == '-h':
    print('''mcb.py - Multiclipboard: puts text in clipboard, based on short key value
Usage: mcb save <keyword> - Saves clipboard to keyword.
       mcb del <keyword> - Deletes keyword
       mcb <keyword> - Loads keyword to clipboard.
       mcb list - Loads all keywords to clipboard.
       ''')
    input('Press <ENTER> to continue . . .')
    exit(1)
    
elif args[0].lower() == 'save':
    text[args[1]] = pyperclip.paste()
    
elif args[0].lower() == 'del':
    if args[1] in text:
        del text[args[1]]
    else:
        input('Key not found. Press <ENTER> to continue')
    
elif args[0].lower() == 'list':     # list printed in the clipboard
    contents = "List of keywords\n" + "-"*16 + "\n"
    for key, value in text.items():
        if len(value) > 30:
            value = value[:15] + '[...]' + value[-15:]
        contents += f'{key}: "{value}"\n'
    pyperclip.copy(contents)
    
else:
    if args[0] in text:
        pyperclip.copy(text[args[0]])    
    else:
        pyperclip.copy('')


# close file
text.close()

