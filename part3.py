from part1 import squares_dict
from part2 import primes_dict

'''
Write a function that takes in two numbers, a and b. Output a list of all the "special numbers" between a and b, inclusive, in DESCENDING order. We define a number to be special if one minus the number is prime, and if one plus the number is a square.

Hint: if your range is set to a = 1, b = 1000, then the set of special numbers should be: [3, 8, 24, 48, 80, 168, 224, 360, 440, 728, 840] (of course, this should be in descending order when you output it)
'''

def special_numbers(a, b):
  sq_dict = squares_dict(a, b)
  pr_dict = primes_dict(a, b)