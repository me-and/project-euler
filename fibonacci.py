def fibonacci(a=1, b=1):
    yield a
    while True:
        yield b
        a, b = b, a + b
