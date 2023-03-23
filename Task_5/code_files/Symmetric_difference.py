A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }

# returns all items to result variable except the items on intersection
result = A.symmetric_difference(B)
print(result)

# Output: {'a', 'b', 'e'}

print("-------------------------")


A = {'Python', 'Java', 'Go'}
B = {'Python', 'JavaScript', 'C' }

# returns the symmetric difference of A and B to result variable
result = A.symmetric_difference(B)

print(result)