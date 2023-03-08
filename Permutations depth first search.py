import numpy as np
from itertools import permutations

def fluboxing_permutations(a, n):
    return [p for p in permutations(range(n))
        if all(a[i, j] > a[j, i] for i, j in zip(p, p[1:]))]

n = 5
a = np.random.random([n, n])
print(fluboxing_permutations(a, n))