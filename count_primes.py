'''
Given an integer n, return the number of prime numbers that are strictly less than n
'''
import math

def countPrimes(n: int) -> int:
    if n < 2:
        return 0
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if isPrime[i]:
            for multiple_of_i in range(i*i, n, i):
                isPrime[multiple_of_i] = False
                
    return sum(isPrime)

n = 10
res = countPrimes(n)
print(res)
