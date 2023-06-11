# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:48:20 2019

@author: opujo
"""

import re

phoneUSRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?            # area code
        (\s|-|\.)?                    # separator
        \d{3}                         # first 3 digits
        (\s|-|\.)                     # separator
        \d{4}                         # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
        )''', re.VERBOSE)


emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+      # username
        @                      # @ symbol
        [a-zA-Z0-9.-]+         # domain name
        (\.[a-zA-Z]{2,4})      # dot-something
        )''', re.VERBOSE)


urlRegex = re.compile('''(
                      (http|ftp|https)://            # protocol
                      ([\w_-]+(?:(?:\.[\w_-]+)+))    # server name
                      ([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?  # folder - many characters allowed
                      )''', re.VERBOSE)


dateRegex = re.compile(r'''(
        (([0]?[1-9])|([1-2][0-9])|(30|31))    # day between 1 and 31
        [/\-\.]                               # separator
        (([0]?[1-9])|(1[12]))                 # month between 1 and 12
        [/\-\.]                               # separator
        ([12]\d{3})                           # year between 1000 and 2999
        )''', re.VERBOSE)



romanNumeralRegex = re.compile(r'''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    ''', re.VERBOSE)



# to be used with re.split(), to split a text in words
splitWords = re.compile('\W+')