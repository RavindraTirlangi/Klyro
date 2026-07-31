import pytest  # noqa: F401

from klyro.run_cmd import run_cmd


def test_run_cmd_echo():
    command = "echo Hello, World!"
    exit_code, output = run_cmd(command, use_shell=True)

    assert exit_code == 0
    assert output.strip() == "Hello, World!"


def test_run_cmd_argument_list_avoids_shell():
    exit_code, output = run_cmd(["git", "--version"])

    assert exit_code == 0
    assert output.startswith("git version")
