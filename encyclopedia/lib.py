#!/usr/bin/env python3
"""
Module Lib
    Created:    28 dec 2020
    Last up:    11 jan 2021

Interface:
    printx
    trace

Inspect
    import inspect
    print(inspect.getsource(printx))
"""
from functools import wraps
import warnings

VERBOSE = 0

def printx(msg):
    """
    Print for debugging purposes
    """
    if VERBOSE:
        warnings.warn('Printx !!!')
        print(msg)

# ------------------------------------------------------------------------------
#                              Decorator
# ------------------------------------------------------------------------------
def trace(func):
    """
    Trace for debugging purposes
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        #print(f'{func.__name__}({args!r}, {kwargs!r}) '
        #      f'-> {result!r}')
        return result
    return wrapper
