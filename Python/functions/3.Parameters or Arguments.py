NOTE="""
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.

Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if 
your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.


"""

# This function expects 2 arguments, and gets 2 arguments:
def my_function2(name,loc):
    print(name," from ",loc)

my_function2('hareesh','ktc')
my_function2('kk','ktc')

# If you try to call the function with 1 or 3 arguments, you will get an error:
# This function expects 3 arguments, but gets only 2:

def my_function3(name,loc,pincode):
    print(name," from ",loc,pincode)

# my_function3('hareesh','ktc')#error code