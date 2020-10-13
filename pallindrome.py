#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
pallinlist = []
for i in range(900,1000):
    for j in range(900,1000):
        prod = i * j
        prod = str(prod)
        if prod == prod[::-1]:
            pallinlist.append(int(prod))
print(pallinlist)
print(max(pallinlist))
            
