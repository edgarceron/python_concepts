
# Standarizing output
# All text should end with a point.
# All text should have the date and time (DD/MM/AAAA HH:MM:SS) of its execution
# All text should start with an uppercase letter

import datetime

def add_point_to_the_end(func):
    def inner(*args, **kwargs):
        message = func(*args, **kwargs)
        return message + "."
    
    return inner

def start_with_uppercase(func):
    def inner(*args, **kwargs):
        message = func(*args, **kwargs)
        message = str(message[0]).upper() + message[1:]
        return message
    return inner

def put_date_and_time(func):
    def inner(*args, **kwargs):
        message = func(*args, **kwargs)
        date_text = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return date_text + " " + message
    return inner

@add_point_to_the_end
@put_date_and_time
@start_with_uppercase
def message1():
    return "this is message one"
@add_point_to_the_end
@put_date_and_time
@start_with_uppercase
def message2():
    return "this is message two"
@add_point_to_the_end
@put_date_and_time
@start_with_uppercase
def message3():
    return "33"

print(message1())
print(message2())
print(message3())
