import pytest
import os

# fails on import of regex -- change original code to:
# from . import regex
from scripts.openURLs import parse_arguments

@pytest.mark.parametrize("raw_arguments, expected_limit, expected_path", [
    ({"--limit": "10", "--path": "~/Downloads"}, 10, "~/Downloads"),
    ({"--limit": "0", "--path": "/tmp"}, 0, "/tmp"),
])
def test_parse_arguments_with_limit(raw_arguments, expected_limit, expected_path):
    args = parse_arguments(raw_arguments)
    assert args["--limit"] == expected_limit

@pytest.mark.parametrize("raw_arguments, expected_limit, expected_path", [
    ({"--limit": "10", "--path": "~/Downloads"}, 10, os.path.expanduser("~/Downloads")),
    ({"--limit": "0", "--path": "/tmp"}, 0, "/tmp"),
])
def test_parse_arguments_with_path(raw_arguments, expected_limit, expected_path):
    args = parse_arguments(raw_arguments)
    assert args["--path"] == expected_path