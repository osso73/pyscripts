#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 16/03/2020 21:19

backup_to_zip.py - Copies an entire folder and its contents into
a ZIP file whose filename increments.

@author: opujo
"""

import argparse
import datetime
import os
import zipfile
from pathlib import Path

BACK_FOLDER = r"C:\Cloud\Backups"


def command_line() -> argparse.Namespace:
    """setup argparse variables and help, return arguments"""

    desc = "Create a backup of a folder to a zip file. It can be compressed \
            or non compressed"
    epi = ""
    parser = argparse.ArgumentParser(description=desc, epilog=epi)

    parser.add_argument("folder", help="absolute path of folder to be backed up")
    parser.add_argument(
        "-d",
        "--dest",
        default=BACK_FOLDER,
        help=f"path where to store the archive. Default is: '{BACK_FOLDER}'",
    )
    parser.add_argument(
        "-c",
        "--compress",
        action="store_true",
        help="compress files, as oposed to just storing",
    )

    return parser.parse_args()


def backup_to_zip(arg_folder: str, arg_dest: str, compress: bool) -> None:
    """Back up the entire contents of "folder" into a ZIP file."""

    folder = Path(os.path.abspath(arg_folder))  # make sure folder is absolute
    dest = Path(os.path.abspath(arg_dest))  # make sure folder is absolute

    comp_type = zipfile.ZIP_DEFLATED if compress else None

    # create filename
    formatted_date = datetime.date.today().strftime("%y%m%d")
    suff = "a"
    while True:
        zip_filename = f"{folder.name}_{formatted_date}{suff}.zip"
        zip_filename = dest / zip_filename
        if not os.path.exists(zip_filename):
            break
        suff = chr(ord(suff) + 1)

    # Create the ZIP file.
    print(f"Creating {zip_filename}...")
    backup_zip = zipfile.ZipFile(zip_filename, "w")

    # to avoid storing the full path in .zip file, I change directory to the
    # parent, and use the child only
    os.chdir(folder.parent)

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, _, filenames in os.walk(folder.name):
        print(f"Adding files in {foldername}...", end="")

        # Add the current folder to the ZIP file.
        backup_zip.write(foldername)
        total_size = 0

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            try:
                full_name = os.path.join(foldername, filename)
                backup_zip.write(full_name, compress_type=comp_type)
                total_size += os.path.getsize(full_name)

            except PermissionError:
                print(f'\nFile "{full_name}" skipped - no permission.')

            except FileNotFoundError:
                print(
                    f'\nFile "{folder.parent}\\{foldername}\\{filename}" skipped - File not found: probably name too long?'
                )

        print(f" ({total_size/1024:,.0f} Kbytes)")

    backup_zip.close()
    print("Done.")


######################## MAIN ########################

if __name__ == "__main__":
    args = command_line()
    backup_to_zip(args.folder, args.dest, args.compress)
