'''
Write a program which takes an array of n integers, where A[i] denotes the maximum you can
advance from index l, and returns whether it is possible to advance to the last index starting from
the beginning of the array.
'''

def can_reach_end(arr):
    # we keep track of furthest reach and last index
    furthest_reach_so_far, last_index = 0, len(arr)-1
    i = 0
    # run a loop until i is less than equal to furthest reach
    # and furthest reach is less than equal to last index
    while i <= furthest_reach_so_far and furthest_reach_so_far <= last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, arr[i]+i)
        i += 1
    # if furthest reach is greater or equal to last index that mean we traversed the whole array
    return furthest_reach_so_far >= last_index
    #TC: bigO(n)

a = [3,3,1,0,2,0,1]
print(can_reach_end(a))