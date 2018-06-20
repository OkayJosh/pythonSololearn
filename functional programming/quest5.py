## The function map takes a function and an iterable as arguments, and returns a new iterable
# with the function applied to each argument

def add_five(x):
    return x + 5

nums = [11,22,33,44,55]
results = list(map(add_five,nums)) ## to convert the result into a list we use the list explicitly
print(results)

#### you could have archived the results more easily using the lambda syntax

nums = [11,22,33,44,55]
results = list(map(lambda x: x + 5,nums)) ## to convert the result into a list we use the list explicitly
print(results)