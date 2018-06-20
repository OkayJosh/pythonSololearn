#### Generators are a type of iterable, like list or tuples.
## Unlike list, they don't allow indexing with arbitrary indices, but hey can still be iterated through with a for loops.

# they can be created using function and the yeild statements

def countdown():
    i = 5
    while i > 0:
        yield i
        i -=1

for i in countdown():
    print(i)

### The yield statement is used to define a generator, replacing the return of a function to provide 
# a result to its caller without destroying local variables