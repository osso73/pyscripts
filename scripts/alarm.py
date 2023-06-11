#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 11/04/2020 11:22

alarm.py - A simple countdown script that launches an alarm.

@author: opujo
"""
import argparse
import datetime
import subprocess
import time

CAR = "#"  # character to print the message
TEMP_FILE = r"c:\windows\temp\_msg.txt"
SOUND = r"C:\Windows\Media\alarm01.wav"  # this file always exist on Windows
EXIT_HELP_MSG = "Type alarm --help for more detailed information."


def command_line() -> argparse.Namespace:
    """setup argparse variables and help, return arguments"""

    desc = "Sets an alarm at a certain time, or after a certain time."
    epi = ""
    parser = argparse.ArgumentParser(description=desc, epilog=epi)

    parser.add_argument(
        "-m",
        "--message",
        default="Time up!",
        help='Message to display, at the end of time. Put in "" if it \
                contains spaces.',
    )
    parser.add_argument(
        "-w",
        "--wait",
        metavar="TIME",
        nargs="*",
        help="Amount of time to wait. Use format: HH:MM:SS, or a number \
                followed by s for second, m for mintues, h for hours. \
                Several numbers can be provided: -w 5h 30m 15s.",
    )
    parser.add_argument(
        "-a",
        "--at",
        help="Time at which the alarm will be \
                launched. Use format: HH:MM:SS",
    )

    return parser.parse_args()


def exit_error(msg: str) -> None:
    """prints msg and exits the program"""

    print(msg, EXIT_HELP_MSG, sep="\n")
    exit(-1)


def validate_args(args: argparse.Namespace) -> None:
    """Validate the arguments are valid"""

    if not (args.wait or args.at):
        exit_error("You need to provide at least one time argument.")

    if args.wait and args.at:
        exit_error("Only one of the --wait and --at arguments should be provided.")

    if args.at:
        try:
            _ = datetime.time.fromisoformat(args.at)
        except ValueError:
            exit_error("After --at you should provide a valid time.")

    if args.wait:
        if ":" in args.wait[0]:
            try:
                _ = datetime.time.fromisoformat(args.wait[0])
            except ValueError:
                exit_error("After --wait you should provide a valid time.")

        else:
            for each in args.wait:
                if not each[-1].lower() in ["h", "m", "s"]:
                    exit_error("After --wait you should provide a valid time.")
                try:
                    _ = int(each[:-1])
                except ValueError:
                    exit_error("After --wait you should provide a valid time.")


def get_time_left(
    wait: list[str] or None, at: str or None
) -> tuple[datetime.timedelta, datetime.datetime]:
    """Calculate the time left for the alarm, based on the arguments"""
    now = datetime.datetime.now()
    if wait:
        if ":" in wait[0]:
            t = datetime.time.fromisoformat(wait[0])
            time_left = datetime.timedelta(
                hours=t.hour, minutes=t.minute, seconds=t.second
            )
        else:
            time_left = datetime.timedelta()
            for arg in wait:
                last = arg[-1]
                num = int(arg[:-1])
                if last == "s":
                    time_left += datetime.timedelta(seconds=num)
                elif last == "m":
                    time_left += datetime.timedelta(minutes=num)
                else:
                    time_left += datetime.timedelta(hours=num)

        final_time = now + time_left

    else:
        t = datetime.time.fromisoformat(at)
        final_time = datetime.datetime(
            now.year, now.month, now.day, t.hour, t.minute, t.second
        )
        time_left = final_time - now

    return time_left, final_time


def count_down(time_left: datetime.timedelta, final_time: datetime.datetime) -> None:
    """
    Countdown until alarm is triggered. Print the remaining
    seconds on screen. Capture interruption by user.
    """
    try:
        while time_left.total_seconds() > 0:
            print(f"Time left: {time_left}", end="\r")
            time.sleep(min(1, time_left.total_seconds()))
            time_left = final_time - datetime.datetime.now()

    except KeyboardInterrupt:
        print("\nInterrupted by user")


def trigger_alarm(message: str) -> None:
    """Trigger alarm: play an alarm sound and show message"""
    subprocess.Popen(["start", SOUND], shell=True)
    with open(TEMP_FILE, "wt", encoding="utf_8") as f:
        f.write(CAR * (20 + len(message) + 2) + "\n")
        f.write(CAR * 10 + f" {message} " + CAR * 10 + "\n")
        f.write(CAR * (20 + len(message) + 2) + "\n")
    subprocess.Popen(["notepad", TEMP_FILE], shell=True)
    print("\n\n" + message)


def main():
    """Main program"""
    args = command_line()
    validate_args(args)

    time_left, final_time = get_time_left(args.wait, args.at)

    print(f"{args.message} - Final time: {final_time}.")
    count_down(time_left, final_time)
    trigger_alarm(args.message)


if __name__ == "__main__":
    main()
