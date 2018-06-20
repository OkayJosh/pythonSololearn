## Decorators provides a way to modify other functions using other functions

def decor(func):
    def wrap():
        print("===================")
        func()
        print("===================")
    return wrap

def print_text():
    print("    Hello World    ")

decorated = decor(print_text)
decorated()

print_text = decor(print_text)
print_text()

# python provides support to wrap a function in a decorator by pre-pending the function defination with a decorator name and the @ symbol

@decor
def print_text():
    print("Hello world!")

print_text()