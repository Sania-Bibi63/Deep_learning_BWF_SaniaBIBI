#Creating a dictionary:
my_dict = {'apple': 3, 'banana': 2, 'orange': 1}
# using dict() function
another_dict = dict(name='John', age=30, city='New York')

print("----------------")

#Accessing values
print(my_dict['apple'])  
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print("----------------")
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print("----------------")

#Changing values
my_dict['apple'] = 5
print(my_dict) 
print("----------------")

#Adding items
my_dict['grape'] = 4
print(my_dict)  
print("----------------")

#Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("----------------")

#Removing items
del my_dict['orange']
print(my_dict) 

my_dict.pop('banana')
print(my_dict)  # Output: {'apple': 5, 'grape': 4}

print("----------------")


#Dictionary methods
# keys()
print(my_dict.keys())  

# values()
print(my_dict.values()) 

# items()
print(my_dict.items())  
# get()
print(my_dict.get('apple')) 
print(my_dict.get('watermelon')) 

# update()
my_dict.update({'pear': 2, 'kiwi': 1})
print(my_dict) 
# clear()
my_dict.clear()
print(my_dict)  

# copy()
new_dict = another_dict.copy()
print(new_dict)  

# fromkeys()
fruit_dict = dict.fromkeys(['apple', 'banana', 'orange'], 0)
print(fruit_dict)  

print("----------------")


