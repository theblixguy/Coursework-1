# Complex random password generator written in Python
# Compiled and tested using Python 3.5.0
# Author: Suyash Srijan, student ID: 14076594, Coursework 1 U08008 Modern Computing Technology

# Import the stuff we need
from string import ascii_uppercase, ascii_lowercase, digits
from random import choice
import re

# Define our function which finds two or more consecutive characters in a string
#
# We use the re (regular expression) library to find instances of consecutive characters
# () is a capturing group, the dot captures a character and the \1 checks if the next
# character is the same as the one in the captured group
# If there are two consecutive characters then the function returns true, otherwise false

def consecutive(password):
	contains_consecutive = False
	if re.search(r'(.)\1', password):
		contains_consecutive = True
	return contains_consecutive

# Define our function to generate a random password
#
# We use a really simple algorithm to generate a random password. We take advantage of the 
# uppercase, lowercase and digits constants found in the string library and we choose one element 
# from each of them (the password is supposed to have one uppercase, one lowercase and one digit at least)
# so the first part does that, and then we pick any item from the constants to fill in the remaining characters
# we need for our password
#
# The password isn't supposed to have two consecutive characters so we use our consecutive function (def above)
# to check if the password contains consecutive characters and generate a new password if it does (and repeat until
# the password doesn't contain consecutive characters). This isn't the most efficient way to generate passwords without
# consecutive characters but it does the job

def generateRandomPass():
	allowed_types = ascii_uppercase, ascii_lowercase, digits
	password = [choice(x) for x in allowed_types] + [choice(choice(allowed_types)) for _ in range(14 - len(allowed_types))]
	final_pass = ''.join(password)
	if consecutive(final_pass):
		generateRandomPass()
	return final_pass

# Print the generated password

print (generateRandomPass())