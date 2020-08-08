"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when 
  # trying to open "foo.txt"

# YOUR CODE HERE
# open returns a file object, with 2 arguments: filename and mode
# r for read only



# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

bar = open("bar.txt", "w") # w for only writing
bar.write("Let's go \n")
bar.write("learn some \n")
bar.write("Python!")
bar.close()