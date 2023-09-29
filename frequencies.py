"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for val in items:
        val = str(val)
        if val in frequencies.keys():
            frequencies[val] = frequencies[val] + 1
        else:
            frequencies[val] = 1
    return frequencies
