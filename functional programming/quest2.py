## pure function: has no side effect and returns a value based on their arguments

def pure_function(x,y):
    temp = x + 2*y
    return temp / y + 2*x

##impure function 
some_list = []

def impure(arg):
    some_list.append(arg)