import pytest

#Create a parser
def pytest_addoption(parser):
    parser.addoption("--stringinput", action="append", default=[], help="list of stringsinputs to pass to test functions.  Must input pytest -q --stringinput='name' followed by test_ex4a.py")

#Create the test function
def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))
