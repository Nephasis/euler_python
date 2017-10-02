a = 2
b = 30
primes = []
i = 2
lgth = 0
# for i in range(a, b):
while i >= 2 and lgth < 10001:
    for z in range(2, i):
        if (i % z) == 0 or i == 1:
            break
    else:
        lgth += 1
        print (i, 'is prime and it is', lgth, 'prime')
    i += 1
