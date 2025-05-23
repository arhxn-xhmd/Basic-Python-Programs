from functools import reduce

num = int(input('Enter the number of which you want to find the factorial : '))
numbers = []

for i in range(0, num) :
    numbers.append(i + 1)

factorial = reduce(lambda x, y : x * y, numbers)

print(f'The factorial of {num} is {factorial}')