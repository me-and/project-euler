from sequence import MonatonicIncreasingSequence


def fibonacci_gen(a=1, b=1):
    yield a
    while True:
        yield b
        a, b = b, a + b


# Strictly this is a lie, as the sequence is monatonic non-decreasing with
# a=b=1, but not monatonic increasing.  Thankfully it being monatonic increasing
# after the first two elements is sufficient for everything to work.
fibonacci = MonatonicIncreasingSequence(fibonacci_gen())
