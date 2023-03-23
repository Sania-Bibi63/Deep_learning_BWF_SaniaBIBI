fruits = ['apple', 'banana', 'cherry']

for i, fruit in enumerate(fruits):
    print(i, fruit)
print("---------------------------")    

pets = ('cat', 'dog', 'hamster')

for i, pet in enumerate(pets, start=1):
    print(f'Pet {i}: {pet}')
