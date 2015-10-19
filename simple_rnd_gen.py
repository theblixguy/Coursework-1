# Simple random password generator written in Python
# Compiled and tested using Python 3.5.0
# Author: Suyash Srijan, student ID: 14076594, Coursework 1 U08008 Modern Computing Technology

# Import the choice function from the random library and the constants from the string library
from random import choice
from string import ascii_lowercase, digits

# Generate a random password that is 14 characters long using the random library and store
# it in a temporary variable
#
# We use random.choice() and pass it an a-z 0-9 sequence and using a for loop we select a 
# random item from the sequence and join it to the previous item until we have 14 items 
# to form a 14 character long password 

randompass = ''.join(choice(ascii_lowercase + digits) for i in range(14))

# Print the password to output
print(randompass)