'''
Implement an integer to string conversion function, and a string to integer conversion function,
For example, if the input to the first function is the integer 314,it should return the string "314" and
if the input to the second function is the string "314" it should return the integer 314. you can't use library funtion like int in python
'''
import functools, string
def int_to_string(x: int) -> str:
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    
    return ('-' if is_negative else '') + ''.join(reversed(s))

def string_to_int(s: str) -> int:
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c), 
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)
    

s = "777"
x = 777
print(string_to_int(s))
print(int_to_string(x))

