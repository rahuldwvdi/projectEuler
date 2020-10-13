#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math
n = 600851475143
lst = []
if n>0:
    while(n%2==0):
        n = n/2
        lst.append(2)
    for i in range(3, int(math.sqrt(n)),2):
        if n%i==0:
            n = n/i
            lst.append(i)
print(lst)
max_prime_factor = max(lst)
print(max_prime_factor)