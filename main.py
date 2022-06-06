import traceback
import part1
import part2
import part3

if __name__ == "__main__":
  part = input("Which part? (1, 2, or, 3)").strip()
  while part not in ("1", "2", "3"):
    print("Invalid input!")
    part = input("Which part? (1, 2, or, 3)").strip()
  if part == "1":
    try:
      in1 = input("Input a number (a):")
      while not in1.isnumeric():
        in1 = input("That's not a number. Try inputting a number:")
      in1 = int(in1)
      in2 = input("Input another number (b):")
      while not in2.isnumeric():
        in2 = input("That's not a number. Try inputting a number:")
      in2 = int(in2)
      in3 = input("Input another number (c):")
      while not in3.isnumeric():
        in3 = input("That's not a number. Try inputting a number:")
      in3 = int(in3)
      out = part1.squares(in1, in2, in3)
      print("Your output from part 1:", out)
    except:
      print("Your program in part 1 has an error!")
      traceback.print_exc()
  elif part == "2":
    try:
      in1 = input("Input a number (a):")
      while not in1.isnumeric():
        in1 = input("That's not a number. Try inputting a number:")
      in1 = int(in1)
      in2 = input("Input another number (b):")
      while not in2.isnumeric():
        in2 = input("That's not a number. Try inputting a number:")
      in2 = int(in2)
      in3 = input("Input another number (c):")
      while not in3.isnumeric():
        in3 = input("That's not a number. Try inputting a number:")
      in3 = int(in3)
      out = part2.primes(in1, in2, in3)
      print("Your output from part 2:", out)
    except:
      print("Your program in part 2 has an error!")
      traceback.print_exc()
  else:
    try:
      in1 = input("Input a number (a):")
      while not in1.isnumeric():
        in1 = input("That's not a number. Try inputting a number:")
      in1 = int(in1)
      in2 = input("Input another number (b):")
      while not in2.isnumeric():
        in2 = input("That's not a number. Try inputting a number:")
      in2 = int(in2)
      out = part3.special_numbers(in1, in2)
      print("Your output from part 3:", out)
    except:
      print("Your program in part 3 has an error!")
      traceback.print_exc()