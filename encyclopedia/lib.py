"""
Module Lib
    Created:    28 dec 2020
    Last up:     8 jan 2021

Interface:
    printx
"""

VERBOSE = 0

def printx(msg):
    """
    Print x
    """
    if VERBOSE:
        #print('\n *** printx')
        print(msg)
