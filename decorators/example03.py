
# code for testing decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 
 
def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 
 
@decor1
@decor
def num(): 
    return 10
 
@decor
@decor1
def num2():
    return 10
   
print(num()) 
print(num2())
# Output
# 400
# 200

# The above example is similar to calling the function as –

# decor1(decor(num))
# decor(decor1(num2))