'''
Write a function that takes in two numbers a, b, and c, and creates a dictionary where all the keys are numbers between a and b, and the values are the square of the keys. Using this dictionary, output whether c is a SQUARE of a value between a and b, inclusive.

For this, you should use the separate function squares_dict to ouput the dictionary, so you can use the squares_dict function in part 3.

E.g.: if a = 3, b = 5, c = 16, 3*3 = 9 <= 16 <= 5*5 = 25, so output True

if a = 6, b = 10, c = 101, 6*6 = 36 <= 101 </= 10*10 = 100, so output False
'''

def squares_dict(a, b):
  dict = {}
  for i in range(a, b + 1):
    dict[i] = i * i
  return dict

def squares(a, b, c):
  sq_dict = squares_dict(a, b)
  #return true if c is in between a and b squared
  return (min(sq_dict[a], sq_dict[b]) <= c and c <= max(sq_dict[b], sq_dict[a]))