'''
Write a program that takes two arrays representing integers, and retums an integer representing their product. For example, since 193707721.x -761838257287 = -147573952589676412927, if
the inputs are (1,9,3,7,0,7,7,2, 1) and <-7,6,1,8,3,8,2,5,7,2,8,7>, your function should refum
(-1, 4,7, 5,7,3, 9, 5, 2, 5,8,9, 6,7, 6, 4, 1., 2,9,2,7>.
'''

def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    n, m = len(num1), len(num2)
    # the number of digits to store the result is n+m 
    result = [0] * (n+m)
    # iterating through both the arrays in reverse
    for i in reversed(range(n)):
        for j in reversed(range(m)):
            result[i+j+1] += num1[i]*num2[j]
            result[i+j] += result[i+j+1] // 10
            result[i+j+1] %= 10

    # remove the leading zeroes 
    result = result[next((i for i, x in enumerate(result) if x!= 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]
    # TC: bigO(nm)
    


x = [1,9,3,7,0,7,7,2, 1]
y = [-7,6,1,8,3,8,2,5,7,2,8,7]
print(multiply(x, y))
