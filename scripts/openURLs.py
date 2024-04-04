#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
openURLs - Searches clipboard to find URLs, and will open them
in separate tabs of browser, or download them.

Usage: openURLs [options]

Options:
    -h, --help          show this help message and exit
    -d, --download      download the URLs, instead of opening
    -l, --limit <n>     limit to first n URLs [default: 10]. Use 0 for unlimited
    -p, --path <path>   download to path [default: ~/Downloads]
"""
 
import os
import pyperclip
import requests
import webbrowser
from docopt import docopt

import regex

__version__ = '0.1.0'


def parse_arguments(raw_arguments: dict) -> dict:
    """
    Parse command-line arguments and return a dictionary of values.

    :param raw_arguments: dictionary containing raw arguments
    :return: dictionary with updated values after parsing
    """
    arguments = raw_arguments.copy()
    arguments['limit'] = int(arguments['--limit'])
    arguments['path'] = os.path.expanduser(arguments['--path'])


def main():
    """Main program"""

    # get command line arguments
    raw_arguments = docopt(__doc__, version=f'openURLs {__version__}')
    args = parse_arguments(raw_arguments)

    # get the clipboard
    contents = pyperclip.paste()

    # find pattern
    mo = regex.urlRegex.findall(contents)
    mo = list(set(mo))   # to remove duplicates

    print(f'Found {len(mo)} URLs.')
    if len(mo) > args['--limit'] and args['--limit'] != 0:
        print(f'Limiting to {args["--limit"]} URLs.')
        mo = mo[:args['--limit']]

    if args['--download']:
        print('Downloading urls...')
        for link in mo:
            url = link[0]
            r = requests.get(url)
            filename = url.split('/')[-1]
            fullname = os.path.join(args['--path'], filename)
            print(f'  {url} --> {fullname}')
            open(fullname, 'wb').write(r.content)
    
    else:
        print('Opening urls...')
        # launch browser
        for each in mo:
            webbrowser.open(each[0])
    

if __name__ == '__main__':
    main()