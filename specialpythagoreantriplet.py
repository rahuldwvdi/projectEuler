for i in range(3, 1000):
    for j in range (i + 1, 1000):
        k = i**2 + j**2
        k = k**0.5
        if i + j + k == 1000:
            print(i,j,int(k))
            prod = i * j * k
            break
print(int(prod))
            