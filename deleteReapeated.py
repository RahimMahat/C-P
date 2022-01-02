'''
Write a program which takes as input a sorted array and updates it so that all duplicates have been
removed and the remaining elements have been shifted left to fill the emptied indices. Return the
number of valid elements. Many languages have library functions for performing this operationyou cannot use these functions.
'''

def delete_duplicates(a):
    if not a:
        return 0
    
    write_index = 1
    for i in range(1, len(a)):
        # if element before write index-1 and element at ith position are not same
        if a[write_index-1] != a[i]:
            # shift the unrepeated elements position to the left
            a[write_index] = a[i]
            # and increment write index once we shift
            write_index += 1

    return write_index

a = [1,1,1,1,2,3,3,5,5,7,7,7]
print(delete_duplicates(a))