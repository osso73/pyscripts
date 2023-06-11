#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 19/03/2020 09:13

find.py - Emulates unix/linux find: finds a file within the hierarchy of 
folders. Basic usage, not all the options of unix find are implemented.
       
@author: opujo
"""

import argparse
import os
import re
import subprocess

import pyperclip


def command_line() -> argparse.Namespace:
    """setup argparse variables and help, return arguments"""

    desc = "Emulates unix/linux find: finds a file within the hierarchy of \
    folders. Basic usage, not all the options of unix find are implemented."
    epi = ""
    parser = argparse.ArgumentParser(description=desc, epilog=epi)

    parser.add_argument(
        "starting",
        help="Absolute path of folder to \
                        start the query from",
    )
    parser.add_argument(
        "pattern",
        help="Pattern to search for. By default it \
                        is considered a patern such as used by ls or dir \
                        commands; but it can be a regular expression if used \
                        with parameter -re",
    )
    parser.add_argument(
        "-re", "--regex", action="store_true", help="<pattern> is a regular expression"
    )
    parser.add_argument(
        "-nr",
        "--non-recursive",
        action="store_false",
        help="Flag to avoid searching in recursive folders. \
                        If this flag is not present, it will search recursively \
                        by default.",
    )
    parser.add_argument(
        "-i", "--ignorecase", action="store_true", help="Search ignoring case."
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="FILE",
        nargs="?",
        default=None,
        const="<clip>",
        help="Save the output to a file. If no \
                        FILE is specified, the output will be saved to the \
                        clipboard.",
    )
    parser.add_argument(
        "-x",
        "--exclude",
        metavar="PATH",
        action="append",
        default=[],
        help="String to be excluded from search. \
                        Does not need to be a complete path, can be any part. \
                        Case insensitive. This argument can be added several \
                        times to exclude multiple strings.",
    )
    parser.add_argument(
        "-f",
        "--folder",
        action="store_true",
        help="Make the search on folders instead of filenames",
    )
    parser.add_argument(
        "-e",
        "--exec",
        choices=["del", "open"],
        help="Execute a command on files found: \ndel to \
                        delete the file (does not work on folders)\n open \
                        to open a file mgr on that folder.",
    )

    args = parser.parse_args()

    return args


def message(string: str):
    """Prints the string, and saves it to output list"""
    global output

    print(string)
    output.append(string)


def pattern_to_regex(string: str) -> str:
    """transform pattern to regex. Replace special characters"""
    replace = {
        "*": ".*",
        "?": ".",
        ".": r"\.",
        "[": r"\[",
        "]": r"\]",
        "^": r"\^",
        "$": r"\$",
        "+": r"\+",
        "{": r"\{",
        "}": r"\}",
        "\\": r"\\",
        "|": r"\|",
        "(": r"\(",
        ")": r"\)",
    }
    tmp = ""
    for char in string:
        if char in replace:
            tmp += replace[char]
        else:
            tmp += char
    return "^" + tmp + "$"


def main() -> None:
    """Main function"""
    args = command_line()
    total_found = 0
    global output

    output = []

    if not args.regex:
        args.pattern = pattern_to_regex(args.pattern)

    if args.ignorecase:
        regex = re.compile(args.pattern, re.IGNORECASE)
    else:
        regex = re.compile(args.pattern)

    # start recursive search
    message(f'Searching "{args.pattern}" at "{args.starting}":')
    for foldername, _, files in os.walk(args.starting):
        # check if folder has to be skipped from search
        skip = False
        for string in args.exclude:
            if string.lower() in foldername.lower():
                skip = True
        if skip:
            continue

        relative_foldername = os.path.relpath(foldername, args.starting)

        if args.folder:  # search folder
            mo = regex.search(os.path.basename(foldername))
            if mo:
                total_found += 1
                if args.exec == "open":
                    message(f"opening folder... {foldername}")
                    subprocess.Popen(["explorer", "/select,", foldername])
                else:
                    message(f"{relative_foldername}")

        else:  # search within files of current folder
            for file in files:
                mo = regex.search(file)
                if mo:
                    fullname = os.path.join(foldername, file)
                    total_found += 1
                    if args.exec == "open":
                        message(f"opening file... {fullname}")
                        subprocess.Popen(["explorer", "/select,", fullname])
                    elif args.exec == "del":
                        message(f"deleting file... {fullname}")
                        os.unlink(fullname)
                    else:
                        message(f"{relative_foldername}\\{file}")

        # if recursive is False, it will stop at the first iteration
        if not args.non_recursive:
            break

    message(f"\n{total_found} matches found.\n")

    if args.output:
        out = "\n".join(output)
        if args.output.lower() == "<clip>":
            pyperclip.copy(out)
        else:
            with open(args.output, "wt") as file_out:
                file_out.write(out)


if __name__ == "__main__":
    main()
