'''
Write a program that takes as input a permutation, and returns the next permutation under dictionary ordering. If the permutation is the last permutation, return the empty array. For example, if
the input is (1,0,3,2) your function should return <1.,2,0,3>. If the input is (3,2,1,0), return ().
'''

def next_permutation(perm):
    # find the first entry from the right which is smaller than the 
    # entry immediately after it.
    inverstion_point = len(perm) - 2
    while inverstion_point >= 0 and perm[inverstion_point] >= perm[inverstion_point+ 1 ]:
        inverstion_point -= 1

    if inverstion_point == -1:
        return []   # perm is the last permutation

    # swap the smallest entry after index inverstion_point that is greater than perm[inverstion_point].
    # since entries in perm are in decreasing order, the first entry that is greater than perm[inverstion_point]
    # is the entry to swap with
    for i in reversed(range(inverstion_point + 1, len(perm))):
        if perm[inverstion_point] < perm[i]:
            perm[inverstion_point], perm[i] = perm[i], perm[inverstion_point]
            break
    # entries in perm must appear in decreasing order after inversion_point
    # so we simply reverse these entries to get the smallest dictionary order
    perm[inverstion_point + 1:] = reversed(perm[inverstion_point + 1:])
    return perm
    # TC: bigO(n)

perm = [1,0,3,2]
print(next_permutation(perm))