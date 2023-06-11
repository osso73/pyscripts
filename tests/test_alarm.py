#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 03 12:18:59 2022

@author: osso73
"""

import sys
from datetime import datetime, time, timedelta

import pytest
from scripts import alarm


def time_to_delta(timeobj: time) -> timedelta:
    """Return time as a timedelta"""
    return timedelta(hours=timeobj.hour, minutes=timeobj.minute, seconds=timeobj.second)


class TestCommandLine:
    """
    All tests for command_line function:
    - message is well parsed
    - wait is well parsed: test with different lists, etc.
    - at is well parsed
    """

    @pytest.mark.parametrize("option", ["-m", "--message"])
    @pytest.mark.parametrize("msg", ["Hola", "S'ha acabat el temps", "Time!!"])
    def test_command_line_message(self, option: str, msg: str) -> None:
        """Test command_line function message argument"""
        sys.argv = sys.argv[:1]
        sys.argv.append(option)
        sys.argv.append(msg)

        args = alarm.command_line()
        assert args.message == msg

    @pytest.mark.parametrize("option", ["-w", "--wait"])
    @pytest.mark.parametrize(
        "wait",
        [
            ["13:51"],
            ["15m", "30s"],
            ["Oriol", "Pujol", "Romanyà"],
        ],
    )
    def test_command_line_wait(self, option: str, wait: list[str]) -> None:
        """Test command_line function wait argument"""
        sys.argv = sys.argv[:1]
        sys.argv.append(option)
        for element in wait:
            sys.argv.append(element)

        args = alarm.command_line()
        assert args.wait == wait

    @pytest.mark.parametrize("option", ["-m", "--message"])
    @pytest.mark.parametrize("at", ["24:58", "14:23:56", "any time!!"])
    def test_command_line_at(self, option: str, at: str) -> None:
        """Test command_line function at argument"""
        sys.argv = sys.argv[:1]
        sys.argv.append(option)
        sys.argv.append(at)

        args = alarm.command_line()
        assert args.message == at


class TestExitError:
    """
    Tests for exit_error function. Tests included:
    - message is printed, Tested with different types of variables.
    - error code is -1.
    """

    @pytest.mark.parametrize(
        "msg",
        [
            "Hello",
            "Goodbye",
            234,
            False,
        ],
    )
    def test_exit_error_message(self, msg: str, capsys) -> None:
        """Test exit_error function prints message in output."""
        with pytest.raises(SystemExit):
            alarm.exit_error(msg)
        captured = capsys.readouterr()
        assert captured.out == f"{msg}\n{alarm.EXIT_HELP_MSG}\n"

    def test_exit_error_exit_code(self) -> None:
        """Test exit_error function gives exit code == -1"""
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            alarm.exit_error("msg")
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == -1


class TestValidateArgs:
    """
    Tests validate_args function. Tests included:
    - no SystemExit is raised if arguments are correct
    - if none wait and at exist, get error message
    - if both wait and at exist, get error message
    - at argument is a valid time, if it exists
    - wait argument is valid, if it exists

    for later -- not yet implemented:
    - at time must be later than now
    """

    @pytest.mark.parametrize(
        "cli",
        [
            "--at 15:30",
            "--wait 5s",
            "--wait 05:00",
            "--wait 3h 25m 5s",
            "--wait 25m",
        ],
    )
    def test_validate_args_ok(self, cli: str) -> None:
        """Test that no SystemExit is raised if arguments are correct"""
        sys.argv = sys.argv[:1]
        for element in cli.split():
            sys.argv.append(element)

        args = alarm.command_line()
        alarm.validate_args(args)
        assert True  # only works if no exitcode

    @pytest.mark.parametrize(
        "cli",
        ["--message test", ""],
    )
    def test_validate_args_no_wait_no_at(self, cli: str, capsys) -> None:
        """Test SystemExit is raised if no wait, and no at"""
        sys.argv = sys.argv[:1]
        for element in cli.split():
            sys.argv.append(element)

        args = alarm.command_line()
        with pytest.raises(SystemExit):
            alarm.validate_args(args)

        captured = capsys.readouterr()
        msg = "You need to provide at least one time argument."
        assert captured.out == f"{msg}\n{alarm.EXIT_HELP_MSG}\n"

    @pytest.mark.parametrize("cli", ["--at 5:00 --wait 5s", "--wait 5s --at 5:00"])
    def test_validate_args_wait_and_at(self, cli: str, capsys) -> None:
        """Test SystemExit is raised if both wait and at are present"""
        sys.argv = sys.argv[:1]
        for element in cli.split():
            sys.argv.append(element)

        args = alarm.command_line()
        with pytest.raises(SystemExit):
            alarm.validate_args(args)

        captured = capsys.readouterr()
        msg = "Only one of the --wait and --at arguments should be provided."
        assert captured.out == f"{msg}\n{alarm.EXIT_HELP_MSG}\n"

    @pytest.mark.parametrize(
        "cli",
        ["--at wrong", "--at 135", "--at 27:30", "--at 11:87", "--at 1:35"],
    )
    def test_validate_args_at_error(self, cli: str, capsys) -> None:
        """Test SystemExit is raised at arguments are wrong"""
        sys.argv = sys.argv[:1]
        for element in cli.split():
            sys.argv.append(element)

        args = alarm.command_line()
        with pytest.raises(SystemExit):
            alarm.validate_args(args)

        captured = capsys.readouterr()
        msg = "After --at you should provide a valid time."
        assert captured.out == f"{msg}\n{alarm.EXIT_HELP_MSG}\n"

    @pytest.mark.parametrize(
        "cli",
        [
            "--wait wrong",
            "--wait 13 23 23",
            "--wait hours",
            "--wait 5.0s",
            "--wait 1:30",
        ],
    )
    def test_validate_args_wait_error(self, cli: str, capsys) -> None:
        """Test SystemExit is raised at arguments are wrong"""
        sys.argv = sys.argv[:1]
        for element in cli.split():
            sys.argv.append(element)

        args = alarm.command_line()
        with pytest.raises(SystemExit):
            alarm.validate_args(args)

        captured = capsys.readouterr()
        msg = "After --wait you should provide a valid time."
        assert captured.out == f"{msg}\n{alarm.EXIT_HELP_MSG}\n"


class TestGetTimeLeft:
    """
    Tests for function get_time_left. It includes:
    - at tests: gives the correct result
    - wait tests: gives the correct result
    """

    @pytest.mark.parametrize("at_time", ["20:24", "23:15:30"])
    def test_get_time_left_at(self, at_time: time):
        """Test at parameters"""
        now = datetime.now()
        left, final = alarm.get_time_left(None, at_time)

        assert final.time() == time.fromisoformat(at_time)
        assert final.date() == now.date()
        assert left == final - now

    @pytest.mark.parametrize(
        "params, wait_time",
        [
            (["02:00"], "02:00:00"),
            (["00:30:50"], "00:30:50"),
            (["1h"], "01:00:00"),
            (["1h", "30m"], "01:30:00"),
            (["1h", "10m", "30s"], "01:10:30"),
        ],
    )
    def test_get_time_left_wait(self, params: list[str], wait_time: str):
        """Test wait parameters"""
        now = datetime.now()
        left, final = alarm.get_time_left(params, None)

        h = time.fromisoformat(wait_time)
        wait_delta = timedelta(hours=h.hour, minutes=h.minute, seconds=h.second)
        wait_delta = time_to_delta(h)

        assert left == wait_delta
        assert final == now + left


@pytest.mark.slow
class TestCountDown:
    """
    Tests for function count_down. Tests included:
    - validate the execution time corresponds with time_left
    """

    @pytest.mark.parametrize(
        "left_time",
        [
            "00:00:03",
            "00:00:01",
            "00:00:05",
        ],
    )
    def test_count_down(self, left_time):
        """Validate the amount of time it takes to execute"""
        left = time.fromisoformat(left_time)
        left = time_to_delta(left)
        start_time = datetime.now()
        final = start_time + left
        alarm.count_down(left, final)
        end_time = datetime.now()
        delta = end_time - start_time
        assert left - delta < timedelta(microseconds=10)


class TestTriggerAlarm:
    """
    Tests for function trigger_alarm. Unclear how to test the
    subprocess.Popen function, but at least I can test the output
    on stdout. Tests included:
    - check that message passed is written on screen
    """

    @pytest.mark.parametrize("msg", ["Hola", "Time up!", "Testing message..."])
    def test_trigger_alarm(self, msg: str, capsys) -> None:
        """Check msg is written on screen"""
        alarm.trigger_alarm(msg)
        captured = capsys.readouterr()
        assert msg in captured.out


@pytest.mark.slow
class TestMain:
    """
    Tests for main function. These are integration test,
    they test the program end-to-end. They test the application works
    under different arguments. The following tests are included:
    - arguments --wait
        * alarm is triggered after expected time
        * message on screen is correct
    - arguments --at
        * alarm is triggered after expected time
        * message on screen is correct
    """

    @pytest.mark.parametrize("option", ["-w", "--wait"])
    @pytest.mark.parametrize("seconds", [2, 1])
    def test_main_wait_time_ok(self, seconds: int, option: str) -> None:
        """Argument with wait triggers alarm after the wait time"""
        sys.argv = sys.argv[:1]
        for arg in [option, f"{seconds}s"]:
            sys.argv.append(arg)

        start = datetime.now()
        alarm.main()
        end = datetime.now()
        delta = (end - start) - timedelta(seconds=seconds)
        assert delta < timedelta(microseconds=100_000)

    @pytest.mark.parametrize("option", ["-m", "--message"])
    @pytest.mark.parametrize("msg", ["testing...", "Time!"])
    def test_main_wait_message_ok(self, msg: str, option: str, capsys) -> None:
        """Argument with wait triggers alarm after the wait time"""
        sys.argv = sys.argv[:1]
        for arg in ["-w", "1s", option, msg]:
            sys.argv.append(arg)

        alarm.main()

        captured = capsys.readouterr()
        assert msg in captured.out

    @pytest.mark.parametrize("option", ["-a", "--at"])
    @pytest.mark.parametrize("seconds", [2, 1])
    def test_main_at_time_ok(self, seconds: int, option: str) -> None:
        """Argument with wait triggers alarm after the wait time"""
        wait_time = timedelta(seconds=seconds)
        start = datetime.now()
        at_time = start + wait_time
        sys.argv = sys.argv[:1]
        for arg in [option, f"{at_time.time().isoformat()}"]:
            sys.argv.append(arg)
        alarm.main()
        end = datetime.now()
        delta = (end - start) - wait_time
        assert delta < timedelta(microseconds=100_000)

    @pytest.mark.parametrize("option", ["-m", "--message"])
    @pytest.mark.parametrize("msg", ["testing...", "Time!"])
    def test_main_at_message_ok(self, msg: str, option: str, capsys) -> None:
        """Argument with wait triggers alarm after the wait time"""
        at_time = datetime.now() + timedelta(seconds=1)
        sys.argv = sys.argv[:1]
        for arg in ["-a", f"{at_time.time().isoformat()}", option, msg]:
            sys.argv.append(arg)
        alarm.main()
        captured = capsys.readouterr()
        assert msg in captured.out
