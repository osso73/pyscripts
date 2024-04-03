#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
New version of clp -- refactoring code, with several modifications: 
    - adding typings
    - using protocol class
    - mapping actions to functions

clip.py - Manipulates the clipboard

Created on Fri Mar  6 12:01:59 2020
@author: opujo
"""

import argparse
import logging
import re
from typing import Protocol

import pyperclip

import regex


class TextTransformer(Protocol):
    """Protocol class for transformer functions"""

    def __call__(self, original: str, *args: str) -> str:
        ...


def command_line() -> argparse.Namespace:
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

    parser.add_argument(
        "args", help="Arguments of the action, if any.", nargs="*", default=[]
    )

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


def custom(original: str) -> str:
    """remove first characters of each line before '. '"""
    lines = original.split("\n")
    lines_out = []
    for line in lines:
        pos = line.find(". ")
        if pos == -1:
            pos = -2
        lines_out.append(line[pos + 2 :])

    final = "\n".join(lines_out)
    return final


def create_md_toc(original: str) -> str:
    """
    Create Table of Contents from a markdown text.
    Will go through the original string, and detect any title (lines starting
    with #), and create an entry in with a anchor, so it can be used as ToC
    at the beginning of the document.
    """
    lines_in = original.split("\n")
    lines_out = []
    CHARS_TO_REMOVE = r"./'"

    for line in lines_in:
        if len(line) == 0 or not line.startswith("#"):
            continue
        level, _, title = line.partition(" ")
        newline = " " * 4 * (len(level) - 1) + "- [" + title + "](#"
        for char in title:
            if char in CHARS_TO_REMOVE:  # characters removed
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


def replace(original: str, string: str, new_string: str) -> str:
    """replace string by new_string"""
    final = original.replace(string, new_string)
    return final


def replace_regex(original: str, string: str, new_string: str) -> str:
    """replace string by new_string usign regular expressions"""
    regex = re.compile(string)
    final = regex.sub(new_string, original)
    return final


def to_regex(original: str) -> str:
    """convert text to regex text, escape all special characters"""
    replace_map = {
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
        if char in replace_map:
            final += replace_map[char]
        else:
            final += char
    return final


def bullets(original: str, bullet: str = "- ") -> str:
    """add bullets at the begining of the line"""
    lines = original.split("\n")
    for n, _ in enumerate(lines):
        lines[n] = bullet + lines[n].strip()
    final = "\n".join(lines)
    return final


def make_list(original: str) -> str:
    """convert lines to a list separated by commas"""
    final = replace(original, "\r\n", ", ")
    final = replace(final, "\n", ", ")
    return final


def date_format(original: str) -> str:
    """
    change date format from US (month/day) to EU (day/month)
    or viceversa. Just exchange date and month.
    """
    dateRegex = re.compile(r"(\d\d?)(\D)(\d\d?)(\D)(\d{2,4})")
    final = dateRegex.sub(r"\3\2\1\4\5", original)

    return final


def exchange_comas_dots(original: str) -> str:
    """exchange comas and dots of the original text"""
    final = ""
    for n in original:
        if n == ",":
            final += "."
        elif n == ".":
            final += ","
        else:
            final += n

    return final


def extract(original: str, expression: str) -> str:
    """
    Extract regex pattern from original. Currently
    available patterns (check regex.py):
        - phoneUSRegex
        - emailRegex
        - urlRegex
    """

    if expression.startswith("regex:"):
        if expression.endswith("phoneUS"):
            regex_expr = regex.phoneUSRegex
        elif expression.endswith("email"):
            regex_expr = regex.emailRegex
        elif expression.endswith("url"):
            regex_expr = regex.urlRegex
    else:
        regex_expr = re.compile(expression)

    match = regex_expr.findall(original)
    lst = list()
    for each in match:
        if isinstance(each, tuple):
            lst.append(each[0])
        else:
            lst.append(each)

    final = "\n".join(lst)
    return final


def capitalize(original: str) -> str:
    """
    Change capitalisation of text. Maintains uppercase
    after a dot.
    """
    sentences = original.split(".")
    cap_sent = []
    for each in sentences:
        cap_sent.append(each.capitalize())

    return ".".join(cap_sent)


def exit_error(msg: str) -> None:
    """exit the program, typing information string"""
    print(msg)
    print("Please type clip.py --help for information on usage.")
    exit(0)


def validate_arguments(args: argparse.Namespace) -> None:
    """Ensure the right arguments are passed. If not, print error message"""
    action = args.action.lower()

    if action.startswith("replace") and len(args.args) != 2:
        exit_error(f"'{args.action}' function needs 2 arguments")

    elif action == "extract" and not args.args:
        exit_error(f"'{args.action}' function needs 1 argument.")

    elif action == "bullets" and len(args.args) > 1:
        exit_error(
            f"'{args.action}' function can have only 1 argument, or no arguments."
        )

    elif args.args and action != "bullets":
        exit_error(f"'{args.action}' function cannot have any argument.")


def get_mapping() -> dict[str, TextTransformer]:
    """Create dictionary of functions, mapping action with the function"""
    mapping = {
        "comas-dots": exchange_comas_dots,
        "list": make_list,
        "to-regex": to_regex,
        "capitalize": capitalize,
        "bullets": bullets,
        "date": date_format,
        "replace": replace,
        "replace-regex": replace_regex,
        "extract": extract,
        "md-toc": create_md_toc,
        "custom": custom,
    }
    return mapping


################################## MAIN #################################
def main():
    """Main function of the program"""

    # define logging, based on command line argument
    args = command_line()

    logging.basicConfig(
        level=eval(f"logging.{args.logging}"),
        format=" %(asctime)s - %(levelname)s - %(message)s",
    )

    logging.debug(f"arguments: {args}")
    text_in = pyperclip.paste()
    logging.debug(f"input text: {text_in}")
    validate_arguments(args)

    execute = get_mapping()
    action = args.action.lower()
    text_out = execute[action](text_in, *args.args)

    pyperclip.copy(text_out)

    logging.info(f"Ok, {args.action} done.")


if __name__ == "__main__":
    main()
