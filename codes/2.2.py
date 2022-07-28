from math import sqrt

def num_input(message):
  while True:
    num = input(message)

    if num.isnumeric():
      return int(num)
    else:
      print('Only numbers!')

    

side_a = num_input('Input side a: ')
side_b = num_input('Input side b: ')
side_c = num_input('Input side c: ')

print()
if side_c == sqrt(side_a**2 + side_b**2):
  print('A right triangle!')
else:
  print('Not a right triangle')