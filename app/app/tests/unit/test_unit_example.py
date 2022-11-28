from app.app.app import *
import pytest

def test_add():
    result = add(2, 3)

    assert result == 5
