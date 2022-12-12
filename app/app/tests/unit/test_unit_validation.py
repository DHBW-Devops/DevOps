from app.app.app import *

def test_validation_if_correct_names():
    validResult = name_is_valid("Korrekter Name")
    numberResult = name_is_valid("404 Not Found")

    assert validResult
    assert numberResult

def test_validation_if_false_names():
    emptyResult = name_is_valid("")
    faultyResult = name_is_valid("\'!?")

    assert not emptyResult
    assert not faultyResult
