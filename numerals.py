#!/usr/bin/python
import sys

def roman_numeral_to_int(numeral):
    """ Function to convert an input roman numeral string to an integer. """

    # Check the argument is a non-zero length string derivative
    if not isinstance(numeral, str):
        print 'Argument not a string, aborting'
        return 0
    if len(numeral) == 0:
        print 'String is empty, aborting'
        return 0

    # Make a dict mapping single numerals to their decimal values
    values = {'I': 1, 'i': 1, 'V': 5, 'v': 5, 'X': 10, 'x': 10, 'L': 50,
         'l': 50, 'C': 100, 'c': 100, 'D': 500, 'd': 500, 'M': 1000, 'm': 1000}

    # Check the string contains no invalid characters
    for s in numeral:
        if not s in values:
            print 'Invalid character supplied, ',
            print 'please use only I, V, X, L, C, D and M'
            return 0

    # Perform the conversion, looping over each character in the string
    accumulator = 0
    i = 0
    while i < len(numeral):
        # Are we on the last character (i.e. we can't peep ahead)?
        if i == len(numeral) - 1:
            accumulator += values[numeral[i]]
            break
        # Check if we need to do a subtraction e.g. for IX = 9
        if values[numeral[i]] < values[numeral[i+1]]:
            accumulator += values[numeral[i+1]] - values[numeral[i]]
            i += 1 # Skip the next character as we have already used it
        # Otherwise just add the decimal value to the accumulator
        else:
            accumulator += values[numeral[i]]
        i += 1
        print str(i) + ' ' + str(accumulator)

    return accumulator

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print 'Please enter a roman numeral as the only argument'
    else:
        args.pop(0)
        ans = roman_numeral_to_int(args[0])
