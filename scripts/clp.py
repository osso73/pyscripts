#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
clip.py - Manipulates the clipboard

Created on Fri Mar  6 12:01:59 2020
@author: opujo
"""

import argparse
import logging
import re

import pyperclip

import regex


def command_line():
    """setup argparse variables and help, return arguments"""

    desc = "Manipulates the clipboard"

    epi = """The following actions are implemented (alphabetical order):
        'bullets': adds '- ' at the beginning of each line of clipboard. An
        argument can be added if you want a different character than '- '.

        'capitalize': changes capitalisation of text, all lowercase except first
        letter and after a dot.

        'comas-dots': exchanges commas by dots. Useful to re-format numbers.

        'date': will change dates from US format (month/day/year) to EU format
        (day/month/year) or viceversa, keeping the same separator. Note year
        must be included.

        'extract': will search for a pattern within the contents of clipboard,
        and return a list of matches found. Needs as argument the regular
        expression to search for. Built-in regex can be used as well, using as
        argument "regex:name", where name is one of the follwing:
            - phoneUS: regex for US phones
            - email: regex for email addresses
            - url: regex for URLs.

        'list': converts clipboard to a comma-separated list. Each line is an
        element of the list

        'md-toc': the contents of the clipboard is a full markdown note. This
        action will create a table of contents by analyzing the headers
        contained in the clipboard.

        'replace': will replace one string by another. The two strings are
        mandatory arguments.

        'replace-regex': same as replace, but the search string is a regular
        expression. Special codes for \\1, \\2, etc. can be used in the
        replacement string to use the groups of the search string.

        'to-regex': transforms text from clipboard to a regex string by
        escaping all the special characters.

        'custom': will run a custom action. This requires you to edit the
        source program, to make the modification as needed.
    """
    parser = argparse.ArgumentParser(
        description=desc,
        epilog=epi,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "action",
        help="Action to be done. See below for a list \
                        of the possible actions and description of each.",
        choices=[
            "comas-dots",
            "list",
            "replace",
            "bullets",
            "replace-regex",
            "extract",
            "capitalize",
            "date",
            "md-toc",
            "to-regex",
            "custom",
        ],
        metavar="ACTION",
    )

    parser.add_argument("args", help="Arguments of the action, if any.", nargs="*")

    parser.add_argument(
        "-l",
        "--logging",
        metavar="LEVEL",
        default="CRITICAL",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set debugging level to LEVEL. Possible values are: \
                        'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.",
    )

    return parser.parse_args()


def custom(original):
    """
    remove first characters of each line before '. '
    """
    lines = original.split("\n")
    lines_out = list()
    for line in lines:
        pos = line.find(". ")
        if pos == -1:
            pos = -2
        lines_out.append(line[pos + 2 :])

    final = "\n".join(lines_out)
    return final


def create_md_toc(original):
    """
    Create Table of Contents from a markdown text.
    Will go through the original string, and detect any title (lines starting
    with #), and create an entry in with a anchor, so it can be used as ToC
    at the beginning of the document.
    """
    lines_in = original.split("\n")
    lines_out = list()
    CHARS_TO_REMOVE = r"./'"

    for line in lines_in:
        if not len(line) or not line.startswith("#"):
            continue
        level, _, title = line.partition(" ")
        newline = " " * 4 * (len(level) - 1) + "- [" + title + "](#"
        for char in title:
            if char in r"./":  # characters removed
                continue
            elif char.isalnum():  # letters are kept, but lowercase
                newline = newline + char.lower()
            else:  # any other character replaced by '-'
                if (
                    newline[-1] not in "-#"
                ):  # avoid repeating '-' or being first character after #
                    newline = newline + "-"
        while newline[-1] == "-":  # eliminate last charcter as '-'
            newline = newline[:-1]

        newline = newline + ")"
        lines_out.append(newline)

    final = "\n".join(lines_out)
    return final


def replace(original, string, new_string):
    """
    replace string by new_string
    """
    final = original.replace(string, new_string)
    return final


def replace_regex(original, string, new_string):
    """
    replace string by new_string usign regular expressions
    """
    regex = re.compile(string)
    final = regex.sub(new_string, original)
    return final


def to_regex(original):
    """
    convert text to regex text, escape all special characters
    """
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
    final = ""
    for char in original:
        if char in replace:
            final += replace[char]
        else:
            final += char
    return final


def bullets(original, bullet="- "):
    """
    add bullets at the begining of the line
    """
    lines = original.split("\n")
    for n in range(len(lines)):
        lines[n] = bullet + lines[n].strip()
    final = "\n".join(lines)
    return final


def make_list(original):
    """
    convert lines to a list separated by commas
    """
    final = replace(original, "\r\n", ", ")
    final = replace(final, "\n", ", ")
    return final


def date_format(original):
    """
    change date format from US (month/day) to EU (day/month)
    or viceversa. Just exchange date and month.
    """
    dateRegex = re.compile(r"(\d\d?)(\D)(\d\d?)(\D)(\d{2,4})")
    final = dateRegex.sub(r"\3\2\1\4\5", original)

    return final


def exchange_comas_dots(original):
    """
    exchange comas and dots of the original text
    """
    final = ""
    for n in original:
        if n == ",":
            final += "."
        elif n == ".":
            final += ","
        else:
            final += n

    return final


def extract(original, expression):
    """
    Extract regex pattern from original. Currently
    available patterns (check regex.py):
        - phoneUSRegex
        - emailRegex
        - urlRegex
    """
    match = expression.findall(original)
    lst = list()
    for each in match:
        lst.append(each[0]) if type(each) == tuple else lst.append(each)

    final = "\n".join(lst)
    return final


def capitalize(original):
    """
    Change capitalisation of text. Maintains uppercase
    after a dot.
    """
    sentences = original.split(".")
    cap_sent = list()
    for each in sentences:
        cap_sent.append(each.capitalize())

    return ".".join(cap_sent)


def exit_error(string):
    """
    exit the program, typing information string
    """
    print(string)
    print("Please type clip.py --help for information on usage.")
    exit(0)


################################## MAIN #################################
def main():
    """Main function of the program"""
    args = command_line()

    # define logging, based on command line argument
    logging.basicConfig(
        level=eval(f"logging.{args.logging}"),
        format=" %(asctime)s - %(levelname)s - %(message)s",
    )

    logging.debug(f"arguments: {args}")

    text_in = pyperclip.paste()
    logging.debug(f"input text: {text_in}")
    action = args.action.lower()

    if action == "comas-dots":
        text_out = exchange_comas_dots(text_in)
    elif action == "list":
        text_out = make_list(text_in)
    elif action == "to-regex":
        text_out = to_regex(text_in)
    elif action == "capitalize":
        text_out = capitalize(text_in)
    elif action == "bullets":
        bullet = args.args[0] if args.args else "- "
        text_out = bullets(text_in, bullet)
    elif action == "date":
        text_out = date_format(text_in)
    elif action == "replace":
        if len(args.args) != 2:
            exit_error("'replace' function needs 2 arguments.")
        text_out = replace(text_in, *args.args)
    elif action == "replace-regex":
        if len(args.args) != 2:
            exit_error("'replace-regex' function needs 2 arguments.")
        text_out = replace_regex(text_in, *args.args)
    elif action == "extract":
        if not args.args:
            exit_error("'extract' function needs 1 argument.")
        if args.args[0].startswith("regex:"):
            if args.args[0].endswith("phoneUS"):
                regex_expr = regex.phoneUSRegex
            elif args.args[0].endswith("email"):
                regex_expr = regex.emailRegex
            elif args.args[0].endswith("url"):
                regex_expr = regex.urlRegex
        else:
            regex_expr = re.compile(args.args[0])
        text_out = extract(text_in, regex_expr)
    elif action == "md-toc":
        text_out = create_md_toc(text_in)
    elif action == "custom":
        text_out = custom(text_in)
    else:
        exit_error("Wrong action.")

    pyperclip.copy(text_out)

    print(f"Ok, {args.action} done.")


if __name__ == "__main__":
    main()
