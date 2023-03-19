print("Lists")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print("---------------")
#Accessing Elements in a List
print(bicycles[0])

print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
print("------------------")
#Using Individual Values from a List
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

print("-----------------")
#Changing, Adding, and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
print("-------------------")
#Appending Elements to the End of a List

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
print("-------------------")
#Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
print("---------------------")

#Removing Elements from a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
print("---------------------")

#Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("---------------------")

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
print("---------------------")

#Popping Items from any Position in a List
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print("---------------------")
#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
print("---------------------")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
print("---------------------")

#Organizing a List
#Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
print("---------------------")

cars.sort(reverse=True)
print(cars)
print("---------------------")

#Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print("---------------------")
#Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

print("---------------------")
#Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
print("---------------------")

#Avoiding Index Errors When Working with Lists
motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles[3])
print(motorcycles[-1])
print("---------------------")
#motorcycles = []
#print(motorcycles[-1])