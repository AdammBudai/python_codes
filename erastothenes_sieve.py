# program for determining the number of primes in the set 2..n where n is written in a file given as a program argument provided on standard input.

import sys

def sito(n):
    is_prime = [False,False] + [True]*(n-1)
    prime_numbers = []
    for i in range(2,n+1):
        if is_prime[i] == True:
            prime_numbers.append(i)
            for j in range(i**2,n+1,i):
                is_prime[j] = False
    return len(prime_numbers)

for line in sys.stdin:
    if len(line.strip().split()) > 0:
        line = int(line)
        print(sito(line))
        break
