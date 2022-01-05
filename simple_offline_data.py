'''
Implement an algorithm that takes as input an array of distinct elements and a size, and returns
a subset of the given size of the array elements. All subsets should be equally likely. Return the
result in input array itself.
'''
from random import randint

def random_sampling(k, A):
    for i in range(k):
        # Generate a random index in [i, len(A) - 1]
        r = randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]

    return A[:k]
    # TC: bigO(k)

A = [3,7,5,11]
print(random_sampling(3, A))
