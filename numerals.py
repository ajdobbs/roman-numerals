#!/usr/bin/python
import sys

def roman_numeral_to_int(numeral):
    """ Function to convert an input roman numeral string to an integer.
        Some format checking is done on the input numeral, though it is
        not exhaustive. """

    # Check the argument is a non-zero length string derivative
    if (not isinstance(numeral, str)) or (len(numeral) == 0):
        print 'Argument not a non-zero string, aborting'
        return 0

    # Make a dict mapping single numerals to their decimal values
    values = {'I': 1, 'i': 1, 'V': 5, 'v': 5, 'X': 10, 'x': 10, 'L': 50,
         'l': 50, 'C': 100, 'c': 100, 'D': 500, 'd': 500, 'M': 1000, 'm': 1000}

    # Check the string contains no invalid characters
    if not all(s in values for s in numeral):
        print 'Invalid character supplied, use only I, V, X, L, C, D and M'
        return 0

    # Convert each character to a decimal and put in a list
    decimals = [values[s] for s in numeral]

    # Check the numeral was correctly formatted e.g. IIV is not allowed
    if any((z > y and y >= x) for x,y,z in zip(decimals, decimals[1:], decimals[2:])):
        print 'Incorrectly formatted numeral, aborting'
        return 0

    # Sum up the elements, make -ve if the element is less than the following element
    accumulator = sum([x if x >= y else -x for x, y in zip(decimals, decimals[1:])])
    accumulator += decimals[-1] # add the last element, which is always +ve

    return accumulator

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print 'Please enter a roman numeral as the only argument'
    else:
        args.pop(0)
        ans = roman_numeral_to_int(args[0])
        print ans
