""" Pytest Introduction, simple illustration of Pytest """

def my_add(x):
    """ Adds two numbers and returns the result """

    result = x + 11
    return result


def my_mul(x):
    """ Multiplies two numbers and returns the result """

    result = x * 11
    return result


def test_my_add():
    """ Function to test "my_add" function """

    assert my_add(11) == 22


def test_my_mul():
    """ Function to test "my_mul" function """

    assert my_mul(11) == 121


