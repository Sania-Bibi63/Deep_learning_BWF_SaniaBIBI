#Tuples
# Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print("----------------")

# dimensions[0] = 250
#Looping Through All Values in a Tuple
for dimension in dimensions:
    print(dimension)
print("----------------")

#Writing over a Tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
print("----------------")
