from app.app.app import *
import pytest

def test_validation():
    validResult = name_is_valid("Korrekter Name")
    numberResult = name_is_valid("404 Not Found")
    emptyResult = name_is_valid("")
    faultyResult = name_is_valid("\'!?")

    assert validResult
    assert numberResult
    assert not emptyResult
    assert not faultyResult
