'''
Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array
B having the property thatB[0] < B[1] >Bl2) < B[3] >8141< B[5] >....
'''

def rearrange(arr):
    for i in range(len(arr)):
        arr[i: i+2] = sorted(arr[i: i+2], reverse=i%2)

    return arr
    # TC: bigO(n)

a = [12,11.,13,9,12,8,14,1,3]
print(rearrange(a))