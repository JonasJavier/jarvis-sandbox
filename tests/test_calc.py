from calc import add


def test_add():
    assert add(2, 3) == 5


def test_add_negative_and_zero():
    assert add(-2, 3) == 1
    assert add(0, 0) == 0
