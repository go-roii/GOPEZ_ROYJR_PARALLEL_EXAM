from string import ascii_uppercase

alphabet = ascii_uppercase


while True:
  num_input = input('Input a number: ')

  if num_input.isnumeric():
    if int(num_input) >= 0 and int(num_input) <= 35:
      num_input = int(num_input)
      break
    else:
      print('Only between 0 and 35!')
  else:
    print('Only numbers!')

  
if num_input < 10:
  print(num_input)
else:
  print(alphabet[num_input-10])