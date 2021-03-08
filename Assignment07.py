# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Create a script to practice using the pickling function and elegant methods of failing.
# ChangeLog (Who,When,What):
# NHertlein,03.01.2021,Initial Release of Assignment07
# ---------------------------------------------------------------------------- #

import pickle  # Import the pickle module

# Declare variables
objFile = None  # Default file object
strFileName = 'ArnieQuotes.txt' # File
dicRow = {}  # row to load into list
lstArnie = []  # place to save the quotes

# ------------ Pickling example ------------ #
objFile = open(strFileName, "r")

for line in objFile:
    movie, quote = line.split(",")
    dicRow = {"Movie": movie.strip(), "Quote": quote.strip()}
    lstArnie.append(dicRow)

objFile.close()

# Display the list
print("\n******* Arnie Quotes From .txt **********")

for line in lstArnie:
    print(line["Movie"] + ", \"" + line["Quote"] + "\"")

input("\nPress ENTER to pickle!")

# pickle it! Smells like vinegar...
objFile = open('ArnieQuotes.dat', 'wb')
pickle.dump(lstArnie, objFile)
objFile.close()
print("\nSuccessfully pickled.")

input("\nPress ENTER to unpickle")

# unpickle
objFile = open('ArnieQuotes.dat', 'rb')
lstArnieBinary = pickle.load(objFile)
objFile.close()

# Display the list
print("\n******* Arnie Quotes From .dat **********")

for line in lstArnieBinary:
    print(line["Movie"] + ", \"" + line["Quote"] + "\"")

print("\nSuccessfully unpickled!\n")

# Error handling examples
try:
    strChoice = input("Did the silly quotes make you laugh? (y/n) - ")
    if strChoice.lower() != "y":
        raise Exception("This is not possible!")
except Exception as e:
    print()
    print(e)
    print("You need to watch more cheesy action movies")

while True:
    try:
        intChoice = int(input("\nHow would you rate this program on a scale of 1:10? - "))
        if intChoice <= 0:
            print("It's such a fine line between stupid and uh... clever. Try again.")
            continue
        elif intChoice < 11:
            raise Exception("Rating too low")
    except ValueError as e:
        print()
        print("Error: " + str(e))
        print("The authorities said, best leave it unsolved really.")
        print("You are supposed to enter an integer! Try again.")
        continue
    except Exception as e:
        print()
        print("Error: " + str(e))
        print("Wrong!! It goes to 11!")
        print("Input updated with proper value.")
        break

print("\nThat was from the where are they now folder......")
