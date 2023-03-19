#Forgetting to Indent
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
print(magician)

print("-------------")

# #Forgetting to Indent Additional Lines
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("-------------")

#Indenting Unnecessarily
message = "Hello Python world!"

  print(message)
print("-------------")

#Indenting Unnecessarily After the Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    print("Thank you everyone, that was a great magic show!")
# print("-------------")    

#Forgetting the Colon    
magicians = ['alice', 'david', 'carolina']
    for magician in magicians
print(magician)