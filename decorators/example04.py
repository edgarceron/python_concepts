
#Chaining decorators datatypes missmatch

def add_point_to_the_end(func):
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return x + "."
    return inner

def square_result(func):
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        return x ** 2
    return inner

@add_point_to_the_end
@square_result
def my_func():
    return 10


print(my_func())

# Output: Error because decorator expects a String like.