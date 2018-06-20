#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(4))

#lambda
## The below code creates an anonymous function and called it with argument
print((lambda x: x**2 + 5*x + 4)(-4))

## lambda function can be assign to variables, and used like normal functions.
double = lambda x: x*2
print(double(7))