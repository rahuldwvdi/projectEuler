#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

for i in range(3, 1000):
    for j in range (i + 1, 1000):
        k = i**2 + j**2
        k = k**0.5
        if i + j + k == 1000:
            print(i,j,int(k))
            prod = i * j * k
            break
print(int(prod))
            
