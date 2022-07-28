def sort_list(list, order):
  list_copy = list.copy()

  match order:
    case 'asc':
      while True:
        is_sorted = True
        for i in range(len(list_copy)-1):
          if list_copy[i] > list_copy[i + 1]:
            placeholder = list_copy[i]
            list_copy[i] = list_copy[i + 1]
            list_copy[i + 1] = placeholder

            is_sorted = False
        
        if is_sorted:
          break
    case 'desc':
      while True:
        is_sorted = True
        for i in range(len(list_copy)-1):
          if list_copy[i] < list_copy[i + 1]:
            placeholder = list_copy[i]
            list_copy[i] = list_copy[i + 1]
            list_copy[i + 1] = placeholder

            is_sorted = False

        if is_sorted:
          break
    case 'none':
      return list_copy
    case _:
      print('No such order.')
      return

  return list_copy



list1 = [1, 5, 4, 7, 8, 9, 6, 1, 4, 7, 9, 2, 4, 7, 9, 3, 1, 5]

print('asc:', sort_list(list1, order='asc'))
print('desc:', sort_list(list1, order='desc'))
print('none:', sort_list(list1, order='none'))