# for writing in file
file = open("new_file.txt", "w")
file.write("Hello Sania, here is the new file!\n")
file.close()

# for reading a file
file = open("new_file.txt", "r")
contents = file.read()
print(contents)
file.close()

