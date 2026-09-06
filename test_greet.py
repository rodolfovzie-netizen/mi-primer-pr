from greet import greet


def test_greet_with_name():
    assert greet("Ana") == "Hola, Ana!"
