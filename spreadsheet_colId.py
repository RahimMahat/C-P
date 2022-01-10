'''
Implement a function that converts a spreadsheet column id to the corresponding integer, with" N'
corresponding to 1. For example, you should return 4 for "D" ,27 for " AN' ,702 for "ZZ" , elc. How
would you test your code?
'''

import functools

def ss_to_colId(col):
    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0
    )

col = 'RM'
print(ss_to_colId(col))
