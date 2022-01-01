'''
Write a program which takes as input an array of digits encoding a nonnegative decimal integer
D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then
you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
langua ge that has finite-precision arithmetic.
'''
def plus_one(a):
    a[-1] += 1
    for i in reversed(range(1, len(a))):
        # run the loop until you see 10 in the position
        if a[i] != 10:
            break
        # if the ith position ele is 10 set it to 0 and 
        a[i] = 0
        # increment i-1th position element by 1
        a[i-1] += 1


    if a[0] == 10:
        # there is a carry out so we need one more digit to store the result
        # a slick way to do this is append a 0 at the end of the array
        # and update the first entry to 1
        a[0] = 1
        a.append(0)

    return a
    # TC: bigO(n)



A = [7, 7, 6]
print(plus_one(A))