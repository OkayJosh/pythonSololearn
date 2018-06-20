#### Generators: Due to the fact that they yield one item at a time, generators don't have the memory restriction of lists
# in fact they can be infinite


def infinite_seven():
    while True:
        yield 7

for i in infinite_seven():
    print(i)

### In short, generators allow you to declare a function that behaves like an iterator, i.e it can be used as a for loop