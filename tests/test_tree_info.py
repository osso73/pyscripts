#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 23:03:59 2021

@author: osso73
"""


import os, sys
import pytest

from scripts import tree_info


@pytest.mark.parametrize("arg, depth", [
    ('c:\\', '-d 3'), ('.', None), ('../../python/', '-d 5'),
    (None, '-d 1')
    ])
def test_command_line_ok(arg, depth):
    sys.argv = sys.argv[:1]
    if arg:
        sys.argv.append(arg)
    if depth:
        sys.argv.append(depth)
        _, depth_num = depth.split()
        depth_num = int(depth_num)

    args = tree_info.command_line()

    if arg:
        assert args.starting == os.path.abspath(arg)
    else:
        assert args.starting == os.path.abspath('.')

    if depth:
        assert args.depth == depth_num
    else:
        assert args.depth == None


@pytest.mark.parametrize("arg, depth", [
    ('non-existing-folder', '-d 3'),
    ('..', 'parameter'),
    ])
def test_command_line_error(arg, depth):
    sys.argv = sys.argv[:1]
    sys.argv.append(arg)
    sys.argv.append(depth)

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        tree_info.command_line()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2



@pytest.mark.parametrize("num, flag, result", [
    (2340, False, '2.3 KB'),
    (5932326, False, '5.9 MB'),
    (2340, True, '2.3 KiB'),
    (5932326, True, '5.7 MiB'),
    (5932326000, True, '5.5 GiB'),
    ])
def test_approximate_size(num, flag, result):
    assert tree_info.approximate_size(num, flag) == result
