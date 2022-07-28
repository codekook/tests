from ex4a import hello

def test_hello(monkeypatch, tmp_path):
    monkeypatch.setattr("sys.argv", ["ex4a.py", "chloe"])
    assert hello() == ("hello, chloe")
