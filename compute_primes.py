'''
Write a program that takes an integer argument and returns all the primes between 1 and that
integer. For example, if the input is 18, you should return (2,3,5,7,11,13,17)
'''

def generate_primes(n):
    if n < 2:
        return []
    size = (n - 3) // 2 + 1
    primes = [2]    # stores the primes from 1 to n
    # is prime represents (2i + 3) is prime or not
    # initially set each to true, then use sieving to eliminate the nonprimes
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            # sieving from p^2, where p^2 = (4i^2 + 12i + 9).
            # the index in is prime is (2i^2 + 6i + 3) because is_prime represents 2i + 3
            # note that we need to use long for j, because p^2 might overflow
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False

    return primes

print(generate_primes(18))
