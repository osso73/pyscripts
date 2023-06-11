#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 23:03:59 2021

@author: osso73
"""


import sys

import pytest
from scripts import pyfind


@pytest.mark.parametrize("start, pattern", [("c:\\", "oriol"), ("c:/", "*.inil")])
def test_command_line_ok_base(start: str, pattern: str) -> None:
    """Test command_line function"""
    sys.argv = sys.argv[:1]
    sys.argv.append(start)
    sys.argv.append(pattern)

    args = pyfind.command_line()

    assert args.starting == start
    assert args.pattern == pattern


@pytest.mark.parametrize("opt", [("-re"), ("--regex"), (None)])
def test_command_line_ok_regex(opt: str) -> None:
    """Test command_line function"""
    sys.argv = sys.argv[:1]
    sys.argv.append("c:/windows")
    sys.argv.append("*.ini")

    if opt:
        sys.argv.append(opt)

    args = pyfind.command_line()

    if opt:
        assert args.regex == True
    else:
        assert args.regex == False


@pytest.mark.parametrize("opt", [("-nr"), ("--non-recursive"), (None)])
def test_command_line_ok_recursive(opt: str) -> None:
    """Test command_line function"""
    sys.argv = sys.argv[:1]
    sys.argv.append("c:/windows")
    sys.argv.append("*.ini")

    if opt:
        sys.argv.append(opt)

    args = pyfind.command_line()

    if opt:
        assert args.non_recursive is False
    else:
        assert args.non_recursive is True


@pytest.mark.parametrize("opt", [("-f"), ("--folder"), (None)])
def test_command_line_ok_folder(opt: str) -> None:
    """Test command_line function"""
    sys.argv = sys.argv[:1]
    sys.argv.append("c:/windows")
    sys.argv.append("*.ini")

    if opt:
        sys.argv.append(opt)

    args = pyfind.command_line()

    if opt:
        assert args.folder is True
    else:
        assert args.folder is False


@pytest.mark.parametrize(
    "opt, file",
    [
        ("-o", "action.log"),
        ("--output", "action.log"),
        ("-o", None),
        ("--output", None),
        (None, None),
    ],
)
def test_command_line_ok_output(opt: str or None, file: str or None) -> None:
    """Test command_line function"""
    sys.argv = sys.argv[:1]
    sys.argv.append("c:/windows")
    sys.argv.append("*.ini")

    if opt:
        sys.argv.append(opt)
        if file:
            sys.argv.append(file)

    args = pyfind.command_line()

    if opt:
        if file:
            assert args.output == file
        else:
            assert args.output == "<clip>"
    else:
        assert args.output == None


@pytest.mark.parametrize(
    "options",
    [
        ("-x windows"),
        (r"--exclude c:\cloud"),
        (r"-x windows --exclude c:\cloud"),
        (None),
    ],
)
def test_command_line_ok_exclude(options: str or None) -> None:
    """Test command_line function"""
    sys.argv = sys.argv[:1]
    sys.argv.append("c:/windows")
    sys.argv.append("*.ini")

    if options:
        opt = options.split()
        sys.argv += opt
        for n in opt:
            if n in ["-x", "--exclude"]:
                opt.remove(n)

    args = pyfind.command_line()

    if options:
        assert args.exclude == opt
    else:
        assert args.exclude == []


@pytest.mark.parametrize(
    "options", [("-e del"), (r"--exec del"), ("-e open"), (r"--exec open"), (None)]
)
def test_command_line_ok_exec(options: str or None) -> None:
    """Test command_line function"""
    sys.argv = sys.argv[:1]
    sys.argv.append("c:/windows")
    sys.argv.append("*.ini")

    if options:
        opt, command = options.split()
        sys.argv += [opt, command]

    args = pyfind.command_line()

    if options:
        assert args.exec == command
    else:
        assert args.exec == None


@pytest.mark.parametrize(
    "start, pattern, options",
    [
        (None, None, None),
        (None, "*.ini", None),
        ("C:\\", None, None),
        ("C:\\", "*.ini", "-g"),
        ("C:\\", "*.ini", "-e dir"),
    ],
)
def test_command_line_error(
    start: str or None, pattern: str or None, options: str or None
) -> None:
    """Test command_line function"""
    sys.argv = sys.argv[:1]
    for argument in [start, pattern, options]:
        if argument:
            sys.argv.append(argument)

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        pyfind.command_line()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


@pytest.mark.skip
def test_message():
    """Test function message."""
    pass


@pytest.mark.parametrize(
    "string, result",
    [
        ("*.ini", r"^.*\.ini$"),
        ("oriol", "^oriol$"),
        ("*win*", "^.*win.*$"),
        ("ho??a", "^ho..a$"),
    ],
)
def test_pattern_to_regex(string: str, result: str) -> None:
    """Test patter_to_regex function"""
    assert pyfind.pattern_to_regex(string) == result
