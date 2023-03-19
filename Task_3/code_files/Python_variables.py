
print("Python variables")

message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

mesage = "Hello Python Crash Course reader!"

print("----------------")
print("Strings")

name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)
print("----------------")

print("Numbers")
x = 2
y = 3

# Performing arithmetic operations
print("x + y =", x + y)  # addition
print("x - y =", x - y)  # subtraction
print("x * y =", x * y)  # multiplication
print("x / y =", x / y)  # division
print("x // y =", x // y)  # integer division
print("x % y =", x % y)  # modulo

# Incrementing and decrementing variables
x += 1  # equivalent to x = x + 1
y -= 0.5  # equivalent to y = y - 0.5
print("x =", x)
print("y =", y)

# Converting between types
z = "10"
print("int(z) =", int(z))
print("float(x) =", float(x))