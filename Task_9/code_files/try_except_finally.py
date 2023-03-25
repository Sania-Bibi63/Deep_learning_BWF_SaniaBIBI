try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution complete.")
print("------------------------------")

# another example
try:
    # open file in read mode
    with open('new_file.txt', 'r') as file:
        # read the entire file
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found.")
except:
    print("An error occurred.")
finally:
    print("Execution complete.")
