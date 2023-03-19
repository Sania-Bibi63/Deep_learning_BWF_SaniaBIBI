#Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print("---------------------")    

# Doing More Work Within a for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("---------------------") 

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("---------------------") 

#Doing Something After a for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")
print("---------------------") 

