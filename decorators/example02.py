

def my_decorator_args(func):
    def change_args(*args, **kwargs):
        new_args = (int(x/2) for x in args)
        return func(*new_args, **kwargs)
    
    return change_args

@my_decorator_args
def add_one(a):
    return a + 1

print("Result = ", add_one(10))

