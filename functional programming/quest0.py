### Recursion: The fundamental part of recursion is self reference

def factorial(x):
  ''''
    the base case act as the exit condition of the recursion
   ''''
    if x==1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))