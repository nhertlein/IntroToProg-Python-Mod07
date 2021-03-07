# Files & Exceptions
**Dev:** *NHertlein*  
**Date:** *March 07, 2021*  

## Introduction
This document will illustrate the knowledge gained from the seventh lecture and the media portion of the third assignment. In addition, I will cover the creation of a Python script that shows how to pickle and unpickle data, and how to use exceptions to handle errors gracefully. The program will read in some great one liner quotes from Arnold Schwarzenegger. The list of quotes will then be pickled and unpickled and displayed to verify the process worked correctly. The next section of the script had an ability to induce problems to get errors based on the great “rockumentry” Spinal Tap. This assignment was a little different as it was open-ended I didn’t go off the rails too far. No particular reason for using Arnie quotes or Spinal Tap as inspiration. My assignment is late again :(

## Online Media to Research Pickling and Exception Handling
For the assignment we were asked to do some online research about pickling and exception handling. From the search results I went to a thread on pickling on the StackOverflow forums which I always find helpful. The link to the thread is [pickle - Understanding Pickling in Python - Stack Overflow](https://stackoverflow.com/questions/7501947/understanding-pickling-in-python) (external site) and I found it pretty helpful. There were some basic comments which are good for understanding the function, and as always there are the more technical answers which are good for understanding what is going on in the background of the module. The other place I looked for information on pickling is the actual [Python documentation pickle — Python object serialization — Python 3.9.2 documentation](https://docs.python.org/3/library/pickle.html) (external site). The official documentation is very detailed and was good to read after getting a better understanding from the class lecture as well as from the StackOverflow thread. My main takeaway is that pickling is a good way to store data in a format that not easily readable, but of course it is not encrypted so if you need that level of protection this is not the method to use.  

For exception handling research I used the same sources as I always find them helpful. [On StackOverflow I looked at the thread Manually raising (throwing) an exception in Python - Stack Overflow](https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python/24065533#24065533) (external site). This thread had a lot of good information on the right and wrong ways to use exceptions. From my experience exceptions are really important to keep the program from just crashing unexpectedly. The other important aspect is being able to tell the user what exactly went wrong so they can find/fix the bug or know what to change for the next time they run the script.

## Writing the Pickling Portion of the Script
For this week’s assignment I made a project in PyCharm in the Assignment07 folder of the C:\_PythonClass directory.  This assignment was a bit different in that it did not have a “starter” so I created a blank script and copied the header over from the previous assignments and filled it out.  

Under the header I imported the pickle module so it was available for use in the script. The first block of code I used for declaring variables. This script didn’t really need that due to length, but it’s still good practice (Listing 1).  
```
import pickle  # Import the pickle module

# Declare variables
objFile = None  # Default file object
strFileName = 'ArnieQuotes.txt' # File
dicRow = {}  # row to load into list
lstArnie = []  # place to save the quotes
```
##### Listing 1. Declaration of variables

The next section of the script was my example using the pickling function to save data in a binary format. For the example to work, we need to load in some data so I chose to load it in from a \*.txt file so I could compare with the \*.dat file output later. I used similar code to what we have used in the past to load in lines of data from a file, split it into categories, save it as a dictionary row, and then append to a list for reference (Listing 2). As mentioned previously for some reason I decided to load in cheesy one liner quotes from Arnold Schwarzenegger movies.
```
# ------------ Pickling example ------------ #
objFile = open(strFileName, "r")

for line in objFile:
    movie, quote = line.split(",")
    dicRow = {"Movie": movie.strip(), "Quote": quote.strip()}
    lstArnie.append(dicRow)

objFile.close()
```
##### Listing 2. Load in movie quotes from \*.txt file

Once the data was loaded into the script, it was a natural next step to display the contents to the user. The script pauses for the user to press enter to move to the next stage of the script, which is pickling the data just loaded in (Listing 3).
```
# Display the list
print("\n******* Arnie Quotes From .txt **********")

for line in lstArnie:
    print(line["Movie"] + ", \"" + line["Quote"] + "\"")

input("\nPress ENTER to pickle!")
```
##### Listing 3. Display data that was loaded in from the file and pause for user input

After the user hits enter, the script continues and the data is pickled. The first step in the pickling process is to create a file object we will want to save to. I used the “wb” option to open a file in the binary format and ensure that if data was already present in the file it would be replaced by the new content. Data is then saved to the file using the dump method of the pickle module. The file is then closed to prevent data leaks and the user is notified the operation was successful. The script pauses for the user to press enter to move to the next stage of the script, which is unpickling the data (Listing 4). The data saved into the \*.dat file format is not as easily human readable (Figure 1).
```
# pickle it! Smells like vinegar...
objFile = open('ArnieQuotes.dat', 'wb')
pickle.dump(lstArnie, objFile)
objFile.close()
print("\nSuccessfully pickled.")

input("\nPress ENTER to unpickle")
```
##### Listing 4. Pickle data into \*.dat binary file format


##### Figure 1. Data saved into \*.dat binary file format
