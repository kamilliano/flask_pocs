import pytest

import lib.code


def mocked_append_text(a, b):
    return "hello mocked!"


def test_append_text():
    assert lib.code.append_text("foo", " bar") == "foo bar"


def test_append_with_mock(monkeypatch):
    monkeypatch.setattr('lib.code.append_text', mocked_append_text)
    from app import index
    assert index() == "hello mocked!"
