"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("\n", "Number of arguments: ", len(sys.argv), "\n")

for x in sys.argv:
  print("Argument: ", x, "\n")
# Print out the OS platform you're using:
# YOUR CODE HERE
print("Get OS platform you're using: ", sys.platform, "platform: ", sys.platform, "\n")
# Print out the version of Python you're using:
# YOUR CODE HERE
print("python version: ", sys.version, "\n")


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
pid = os.getpid()
print("Current Process ID: ", pid, "\n")

# Print the current working directory (cwd):
# YOUR CODE HERE
cwd = os.getcwd()
print("This is the current working directory: ", cwd, "\n")

# Print out your machine's login name
# YOUR CODE HERE
print("Here's the machine login name: ", os.getlogin(), "\n")