from pypidev import Hello


def test_hello():
    hello = Hello("test")
    assert "Hello, test!" == hello.get()
