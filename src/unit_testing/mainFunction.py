import math

def loop_multiply_imperfect(x ,y):

    return sum(y for _ in range(x))



def loop_multiply_improved(x ,y ): 

    if (x < 0 and y < 0) or (x >= 0 and y >= 0) :

        return sum(abs(y) for _ in range(abs(x)))

    elif x < 0 :

        return sum(x for _ in range (y))

    elif y < 0 :

        return sum(y for _ in range(x))

        

def length_of_integer(n):

    return int(math.floor(math.log10(n)) + 1)


















































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