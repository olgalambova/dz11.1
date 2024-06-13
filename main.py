
def prime_generator(n):
    sieve = [True]*n
    primes = []
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return primes
print(prime_generator(10))


            


#from inspect import isgenerator

#gen = prime_generator(2, 10, isgenerator)
#assert isgenerator(gen) == True, 'Test0'
#assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
#assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
#assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')




