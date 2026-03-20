from fast_module import fast_add

def test_add():
    assert fast_add(2, 3) == 5
    assert fast_add(-1, 1) == 0