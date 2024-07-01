import pytest
from greedy_coin import make_change  # Replace 'your_module' with the name of the module containing your make_change function

def test_make_change_exact():
    assert make_change(1.00) == {500: 0, 200: 0, 100: 1, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    assert make_change(5.00) == {500: 1, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

def test_make_change_mixed():
    assert make_change(12.73) == {500: 2, 200: 1, 100: 0, 50: 1, 20: 1, 10: 0, 5: 0, 2: 1, 1: 1}
    assert make_change(0.99) == {500: 0, 200: 0, 100: 0, 50: 1, 20: 2, 10: 0, 5: 1, 2: 2, 1: 0}

def test_make_change_zero():
    assert make_change(0) == {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

def test_make_change_large():
    assert make_change(123.45) == {500: 24, 200: 1, 100: 1, 50: 0, 20: 2, 10: 0, 5: 1, 2: 0, 1: 0}

def test_make_change_no_groszy():
    assert make_change(20.00) == {500: 4, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    assert make_change(10.00) == {500: 2, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

if __name__ == '__main__':
    pytest.main()
