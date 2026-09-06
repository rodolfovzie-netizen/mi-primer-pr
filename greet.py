def greet(name):
    """Return a friendly greeting for the given name."""
    if not name:
        return "Hola, invitado!"
    return f"Hola, {name}!"


if __name__ == "__main__":
    print(greet("Mundo"))
