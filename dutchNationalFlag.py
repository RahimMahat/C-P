'''
Write a program that takes an array A and an index i into A, and rearranges the elements such
that all elements less than A[r] (the "pivot") appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot.
'''
RED, WHITE, BLUE = range(3)

def dutch_flag_partition(a, pivot_index):
    # BRUTE-FORCE
    # pivot = a[pivot_index]
    # # first pass: group elements smaller than pivot
    # for i in range(len(a)):
    #     # loop for elements smaller than pivot
    #     for j in range(i+1, len(a)):
    #         if a[j] < pivot:
    #             a[i], a[j] = a[j], a[i]
    #             break
    # # second pass: group elements larger than pivot
    # for i in reversed(range(len(a))):
    #     if a[i] < pivot:
    #         break
    #     # look for larger elements stop when we reach an element less than pivot
    #     # since fist pass has moved them to the start of a
    #     for j in reversed(range(i)):
    #         if a[j] > pivot:
    #             a[i], a[j] = a[j], a[i]
    #             break
    # # now the TC: bigO(n^2), SC: bigO(1)

    # we can improvise the above algorithm to make it's time complexity bigO(n)
    # IMPROVISED
    pivot = a[pivot_index]
    smaller, larger = 0, len(a)-1
    # first pass: group elements smaller than pivot
    for i in range(len(a)):
        if a[i] < pivot:
            a[i], a[smaller] = a[smaller], a[i]
            smaller += 1
    # second pass: group elements larger than pivot
    for i in reversed(range(len(a))):
        if a[i] < pivot:
            break
        elif a[i] > pivot:
            a[i], a[larger] = a[larger], a[i]
            larger -= 1
    # The time complexity is bigO(n) and the space complexity is bigO(1).

    return a

A = [0,0,7,2,2,1,1]
ind = 3
print(dutch_flag_partition(A, ind))

