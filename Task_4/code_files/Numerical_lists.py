#Making Numerical Lists
for value in range(1,5):
    print(value)
print("-------------------")
for value in range(1,6):
    print(value)  
print("-------------------")    

#Using range() to Make a List of Numbers  
numbers = list(range(1,6))
print(numbers)    
print("-------------------") 
even_numbers = list(range(2,11,2))

print(even_numbers)
print("-------------------") 
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
print("-------------------") 

#Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
print("-------------------") 

#List Comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)
print("-------------------") 

#Working with Part of a List
#Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print("-------------------") 

print(players[1:4])
print("-------------------") 
print(players[:4])
print("-------------------") 
print(players[2:])
print("-------------------") 
print(players[-3:])
print("-------------------") 

#Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("-------------------") 

#Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print("-------------------") 

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("-------------------") 






