#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 20/03/2020 20:21

openURLs.py - Searches clipboard to find URLs, and will open them
in separate tabs.

@author: opujo
"""
 
import os
import pyperclip
import requests
import webbrowser

import regex

#DOWNLOAD_FOLDER = r'C:\Cloud\PC_Folders\Downloads'
DOWNLOAD_FOLDER = r'C:\Cloud\PC_Common\Downloads'
#DOWNLOAD_FOLDER = r'/home/oriol/Downloads'

# get the clipboard
contents = pyperclip.paste()


# find pattern
mo = regex.urlRegex.findall(contents)
mo = list(set(mo))   # to remove duplicates
print(f'Found {len(mo)} URLs.')
if len(mo) > 10:
    ans = input('Do you want to limit to the first 10 pages? ')
    if ans.lower() in ['yes', 'y']:
        mo = mo[:10]

ans = input('Do you want to open in browser, or download ([O]pen / ([D]ownload) ')

if ans.lower().startswith('o'):
    print('Opening urls...')
    # launch browser
    for each in mo:
        webbrowser.open(each[0])

elif ans.lower().startswith('d'):
    print('Downloading urls...')
    for link in mo:
        url = link[0]
        r = requests.get(url)
        filename = url.split('/')[-1]
        fullname = os.path.join(DOWNLOAD_FOLDER, filename)
        print(f'    {url} --> {fullname}')
        open(fullname, 'wb').write(r.content)

else:
    print("Ok, I'll do nothing then.")
