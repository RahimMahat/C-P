'''
Design an algorithm that creates uniformly random permutations of [0, 1,.. .,n - 1]. You are given
a random number generator that returns integers in the set [0,1, . . . ,n - l] with equal probability;
use as few calls to it as possible.
'''
from random import randint

def random_sampling(k, A):
    for i in range(k):
        r = randint(i, len(A) - 1)
        A[r], A[i] = A[i], A[r]


def random_permutation(n):
    permutation = list(range(n))
    random_sampling(n, permutation)
    return permutation
    # TC: bigO(n)

    

n = 7
print(random_permutation(n))
