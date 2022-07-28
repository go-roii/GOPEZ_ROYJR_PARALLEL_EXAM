import random

random_list = random.sample(range(100, 999), 100)
odd_list = []
even_list = []
divisible_by_nine_list = []
prime_list = []
contains_nine_list = []

for element in random_list:
  if element % 2 != 0:
    odd_list.append(element)
  else:
    even_list.append(element)

  if element % 9 == 0:
    divisible_by_nine_list.append(element)

  numOfDivisor = 0
  for j in range(1, element+1):
    if element % j == 0:
      numOfDivisor += 1
  if numOfDivisor == 2:
    prime_list.append(element)

  if '9' in str(element):
    contains_nine_list.append(element)
  

print(f'''a. All elements in the list
{random_list}
''')

print(f'''b. All numbers grouped by odd and even numbers
odd numbers: {odd_list}
even numbers: {even_list}
''')

print(f'''c. All numbers divisible by 9
{divisible_by_nine_list}
''')

print(f'''d. All prime numbers
{prime_list}
''')

print(f'''e. All numbers that contains the digit 9 (e.g 29, 91, 393, 961)
{contains_nine_list}
''')
