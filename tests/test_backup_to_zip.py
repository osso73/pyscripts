#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 03 12:18:59 2022

@author: osso73
"""

import datetime
import sys
import zipfile
from pathlib import Path
from typing import Callable

import pytest
from scripts import backup_to_zip


class TestCommandLine:
    """All tests for command_line function"""

    @pytest.mark.parametrize("folder", ["c:\\", "oriol", r"c:\windows", r"C:\user"])
    def test_command_line_ok_base(self, folder: str) -> None:
        """Test command_line function positional arguments"""
        sys.argv = sys.argv[:1]
        sys.argv.append(folder)

        args = backup_to_zip.command_line()

        assert args.folder == folder

    def test_command_line_error_no_folder(self):
        """Test command_line function, giving error if no positional arguments"""
        sys.argv = sys.argv[:1]

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            backup_to_zip.command_line()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 2

    @pytest.mark.parametrize(
        "arguments",
        [
            r"C:\ -d C:\Windwos\Temp",
            r"c:\ --dest c:\Windows\Temp",
            r"C:\ -D C:\Windwos\Temp",
            r"c:\ --DEST c:\Windows\Temp",
            r"C:\ -c",
            r"C:\ -C",
            r"C:\ --compress",
            r"C:\ --COMPRESS",
            r"c:\ --dest c:\Windows\Temp -c",
        ],
    )
    def test_command_line_ok_options(self, arguments: str) -> None:
        """Test command_line function when giving options"""
        sys.argv = sys.argv[:1]
        for argument in arguments.split():
            sys.argv.append(argument)

    @pytest.mark.parametrize(
        "option",
        [
            "--d",  # missing folder
            "-o",  # wrong option
            "--wrong_option",
            r"c:\Win",
        ],
    )
    def test_command_line_error_options(self, option: str) -> None:
        """Test command_line function, giving error in case of wrong options"""
        sys.argv = sys.argv[:1]
        sys.argv.append(r"C:\Windows")
        sys.argv.append(option)

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            backup_to_zip.command_line()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 2


class TestBackupToZip:
    """
    All tests for backup_to_zip function. The following features are tested:
    - backup file is created, with correct name
    - backup file has correct name with multiple names
    - backup file is a valid zip file
    - backup file contains the two data files
    - file sizes are the same as the original
    - compressed file sizes are the same as original if not using -c flag
    - compressed file sizes are smaller than original if using -c flag
    """

    @pytest.fixture(scope="class")
    def generate_data(self, tmp_path_factory: Path) -> tuple[Path, tuple[Path, Path]]:  # type: ignore
        """Create folders and files to be backed up"""

        def create_file(path: Path, filename: str, contents: str) -> Path:
            """create a file with the name and contents provided"""
            file = path / filename
            file.write_text(contents)
            return file

        data_folder = tmp_path_factory.mktemp("data")
        first = create_file(data_folder, "file_1.txt", "aeiou" * 1000)
        second = create_file(data_folder, "file_2.txt", "qwerty" * 5000)

        yield data_folder, (first, second)

        first.unlink()
        second.unlink()

    @pytest.fixture
    def get_backup_name(self) -> Callable:
        """Build name of backup file"""

        def _get_backup_name(backup: Path, data: Path, seq: str = "a") -> Path:
            """Function to build name of backup file"""
            now = datetime.date.today().strftime("%y%m%d")
            backup_folder = backup / f"{data.name}_{now}{seq}.zip"
            return backup_folder

        return _get_backup_name

    def test_backup_to_zip_name_single(self, generate_data, get_backup_name, tmp_path):
        """
        Test backup_to_zip: file created is named correctly for a single name.
        Expected to be named as: <dir_name>_<date><seq>, where <date> is in
        format yymmdd, and <seq> is a small letter, starting with a, then b, etc.
        """
        data_folder, _ = generate_data
        backup_to_zip.backup_to_zip(data_folder, tmp_path, False)
        backup_name = get_backup_name(tmp_path, data_folder)
        assert backup_name.exists()
        assert backup_name.is_file()

    def test_name_multiple(self, generate_data, get_backup_name, tmp_path):
        """
        Test backup_to_zip: file created is named correctly for a single name.
        Expected to be named as: <dir_name>_<date><seq>, where <date> is in
        format yymmdd, and <seq> is a small letter, starting with a, then b, etc.
        """
        data_folder, _ = generate_data
        backup_to_zip.backup_to_zip(data_folder, tmp_path, False)
        backup_to_zip.backup_to_zip(data_folder, tmp_path, False)
        backup_to_zip.backup_to_zip(data_folder, tmp_path, False)

        for seq in ["a", "b", "c"]:
            backup_name = get_backup_name(tmp_path, data_folder, seq)
            assert backup_name.exists()
            assert backup_name.is_file()

    def test_valid_zip(self, generate_data, get_backup_name, tmp_path):
        """Test backup_to_zip: file created is valid zip file"""
        data_folder, _ = generate_data
        backup_to_zip.backup_to_zip(data_folder, tmp_path, False)
        backup_name = get_backup_name(tmp_path, data_folder)
        assert zipfile.is_zipfile(backup_name)

    def test_data_files_are_in_zip(self, generate_data, get_backup_name, tmp_path):
        """Test backup_to_zip: data files exist in zip file"""
        data_folder, data_files = generate_data
        backup_to_zip.backup_to_zip(data_folder, tmp_path, False)
        backup_name = get_backup_name(tmp_path, data_folder)
        backup = zipfile.ZipFile(backup_name)
        for file in data_files:
            f = file.relative_to(file.parents[1])
            assert f.as_posix() in backup.namelist()

    def test_data_files_have_correct_size(
        self, generate_data, get_backup_name, tmp_path
    ):
        """Test backup_to_zip: data files exist in zip file"""
        data_folder, data_files = generate_data
        backup_to_zip.backup_to_zip(data_folder, tmp_path, False)
        backup_name = get_backup_name(tmp_path, data_folder)
        backup = zipfile.ZipFile(backup_name)
        for info in backup.infolist():
            if info.filename.endswith("file_1.txt"):
                assert info.file_size == 5000
            elif info.filename.endswith("file_2.txt"):
                assert info.file_size == 30000
            else:  # the list can only contain the two files, and the folder
                assert info.is_dir()

    def test_data_files_have_correct_size_not_compressed(
        self, generate_data, get_backup_name, tmp_path
    ):
        """Test backup_to_zip: compressed size is the same as original size"""
        data_folder, _ = generate_data
        backup_to_zip.backup_to_zip(data_folder, tmp_path, False)
        backup_name = get_backup_name(tmp_path, data_folder)
        backup = zipfile.ZipFile(backup_name)
        for info in backup.infolist():
            if not info.is_dir():
                assert info.compress_type == 0
                assert info.compress_size == info.file_size

    def test_data_files_have_correct_size_compressed(
        self, generate_data, get_backup_name, tmp_path
    ):
        """Test backup_to_zip: compressed size is smaller than original size"""
        data_folder, _ = generate_data
        backup_to_zip.backup_to_zip(data_folder, tmp_path, True)
        backup_name = get_backup_name(tmp_path, data_folder)
        backup = zipfile.ZipFile(backup_name)
        for info in backup.infolist():
            if not info.is_dir():
                # assert info.compress_type > 0
                assert info.compress_size < info.file_size
