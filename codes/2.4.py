divisible_by_3_list = []
divisible_by_4_list = []
divisible_by_5_list = []


for i in range(1, 51):
  if i % 3 == 0:
    divisible_by_3_list.append(i)
  if i % 4 == 0:
    divisible_by_4_list.append(i)
  if i % 5 == 0:
    divisible_by_5_list.append(i)


print(f'''
divisible by
3: {divisible_by_3_list}
4: {divisible_by_4_list}
5: {divisible_by_5_list}
''')