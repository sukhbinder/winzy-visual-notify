import pytest
import winzy_visual_notify as w

from argparse import Namespace, ArgumentParser

def test_create_parser():
    subparser = ArgumentParser().add_subparsers()
    parser = w.create_parser(subparser)

    assert parser is not None

    result = parser.parse_args(['--text', 'hello'])
    assert result.text == ["hello"]
    assert result.character == "random"


def test_plugin(capsys):
    w.tell_plugin.hello(None)
    captured = capsys.readouterr()
    assert "Hello! This is an example ``winzy`` plugin." in captured.out
