# Definition and Calling
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b



# Call the function and print the result
result = add_numbers(3, 4)
print(result)  



#Docstrings
def greet(name):
    """Print a greeting for the given name."""
    print(f"Hello, {name}!")
print("-------------------")


# Call the function and print the docstring
greet("Alice")
help(greet)
print("-------------------")

# Passing Arguments
def power(base, exponent=2):
    """Raise base to the given exponent (default 2)."""
    return base ** exponent



# Call the function with default and non-default arguments
print(power(3))      
print(power(2, 3))   




