#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_squares = 0
for i in range(1,101):
    sum_of_squares = sum_of_squares + i*i
a = sum_of_squares
square_of_sum = 0
for i in range(1,101):
    square_of_sum = square_of_sum + i
b = square_of_sum*square_of_sum
print(b-a)
