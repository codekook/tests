import pytest

def main():
    test_hello()

def test_hello(stringinput):
    assert stringinput.isalpha()

if __name__ == "__main__":
    main()
