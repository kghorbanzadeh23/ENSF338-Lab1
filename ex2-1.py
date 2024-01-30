import sys
def do_stuff():
    if len(sys.argv) < 2:
        print("Please provide a digit in the command-line")
        return
    
    number = int(sys.argv[1])
    if number < 2:
        print('No')
    else:
        for i in range(2, number):
            if number % i == 0:
                print('No')
                return
        print('Yes')
# Test the function
do_stuff()

""""The function do_stuff, takes the string arguement from the command-line
and turns it into an integar. Then it'll check to see if the number provided is a prime number.

The error in this code is the assumption that at least one command-line argument is present,
with this assumption if the user enters no argument the code will return an IndexError
because sys.argv contains only one element.
"""