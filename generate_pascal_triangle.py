'''
Write a program which takes as input a nonnegative integer n and returns the first n rows of Pascal's
triangle.

'''

def generate_pascal_triangle(n):
    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            # set the entry to the sum of above two adjacent entries
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    return result
    #TC: bigO(n^2), SC: bigO(n^2)

print(generate_pascal_triangle(7))
