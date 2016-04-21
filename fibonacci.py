def fibonacci(a=1, b=2):
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
