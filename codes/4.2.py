class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def push_node(self, data):
    node = Node(data)

    if self.head == None:
      self.head = node
    else:
      self.tail = node
      current_node = self.head

      while current_node:
        if current_node.next == None:
          current_node.next = node
          break

        current_node = current_node.next


  def print_list(self):
    current_node = self.head

    while current_node:
      print(current_node.data)
      current_node = current_node.next

  def count_list(self, ref_head):
    current_node = ref_head or self.head

    i = 0
    while current_node:
      i += 1
      current_node = current_node.next

    return i

  def sum_of_lastN_nodes(self, ref_head, N):
    current_node = self.head

    while current_node.data != ref_head:
      current_node = current_node.next

    node_count = self.count_list(current_node)
    sum = 0

    for i in range(node_count, 0, -1):
      if i <= N:
        # print(current_node.data, end='')
        sum += current_node.data

        # if i > 1:
        #   print(' + ', end='')
        # if i == 1:
        #   print(' = ', end='')
      current_node = current_node.next
    # print(sum)

    return sum
      

class Node:

  def __init__(self, data):
    self.data = data
    self.next = None



link_list = LinkedList()

link_list.push_node(5)
link_list.push_node(10)
link_list.push_node(6)
link_list.push_node(4)
link_list.push_node(1)
link_list.push_node(12)

print(link_list.sum_of_lastN_nodes(6, 3))