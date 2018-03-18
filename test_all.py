import pytest
from flask import url_for
import lib.code



# stub function to be called instead of lib.code.append_text
def patched_append_text(a, b):
    return "hello mocked!"

#test lib.code.append_text
def test_append_text():
    assert lib.code.append_text("foo", "bar") == "foo bar"

#monkeypatch the internal function inside api route
def test_index_with_patching(monkeypatch, client):
    monkeypatch.setattr('lib.code.append_text', patched_append_text)
    res = client.get(url_for('api'))
    assert res.get_data(as_text=True) == "hello mocked!"


def test_api(client):
    # given conftest.py has been set up
    # https://github.com/pytest-dev/pytest-flask/issues/7
    res = client.get(url_for('api'))
    assert res.status_code == 200
    assert res.get_data(as_text=True) == "hello calling function from route"
