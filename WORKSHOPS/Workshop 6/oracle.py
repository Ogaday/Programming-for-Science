import random

__save__ = random.random()*100

def oracle(guess):
    """
    Return True if my hidden number is greater than guess, and False otherwise
    """
    global __save__
    return guess < __save__

def reveal():
    """
    Reveal the saved hidden number
    """
    global __save__
    return __save__

