from make_triangle import make_triangle

def test_make_triangle():
    expected = '@'
    actual = '\n'.join(make_triangle(1))
    assert actual == expected