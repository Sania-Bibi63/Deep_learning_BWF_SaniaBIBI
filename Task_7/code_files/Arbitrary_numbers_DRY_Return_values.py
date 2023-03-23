def add_numbers(x, y):
    return x + y
#  arbitrary number of arguments 
def add_numbers(*args):
    return sum(args)
result = add_numbers(3, 4)
print(result)


#  "Don't Repeat Yourself"
def print_twice(text):
    print(text)
    print(text)



# returns multiple values
def get_name_and_age():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

name, age = get_name_and_age()