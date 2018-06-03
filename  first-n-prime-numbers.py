import time
start_time = time.time()

def PrimesPrint(input):
    primes = range(0, input + 1)  # makes a list of 0 to input
    for i in range(2, input+1): # ignores 0 and 1 as they are not prime, O(n)
        if primes[i] == 0:
            continue
        for j in range(i ** 2, input + 1, i): # sets all the non_prime numbers to 0's, O(log n)
            primes[j]=0
    for p in primes:
        if p>1: # since all the not prime numbers are 0, anything >1 are all prime, ignoring 1
            print p

# O(n) * O(log(n)) = O(nlog(n))
PrimesPrint(100)

print ("hi")
print ("sexy")