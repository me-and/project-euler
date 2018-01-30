from itertools import count

from sequence import MonatonicIncreasingSequence

triangles = MonatonicIncreasingSequence((i * (i + 1)) // 2 for i in count(1))
squares = MonatonicIncreasingSequence(i ** 2 for i in count(1))
pentagons = MonatonicIncreasingSequence(n * (3 * n - 1) // 2 for n in count(1))
hexagons = MonatonicIncreasingSequence(n * (2 * n - 1) for n in count(1))
heptagons = MonatonicIncreasingSequence(n * (5 * n - 3) // 2 for n in count(1))
octagons = MonatonicIncreasingSequence(n * (3 * n - 2) for n in count(1))

cubes = MonatonicIncreasingSequence(i ** 3 for i in count(1))
