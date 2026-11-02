import math

def loop_multiply(x ,y):

    return sum(y for _ in range(x))


'''

sum(iterable , start = 0)

Ex 1 :

numbers = [10, 20, 30, 40]

result = sum(numbers)

print(result)


Ex 2: 

numbers = [10, 20, 30]

result = sum(numbers, 5)

print(result)   / Here result will be 65 because calculation started from 5 since start = 5

'''




# uv run python -m unittest mytest ( to run the unittest)