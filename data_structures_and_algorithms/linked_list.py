class Node:
  """
  An object for storing a single node of a linked list.
  Models two attributes - data and the link to the next node in the list.
  """
  data = None
  next_node = None

  def __init__(self, data):
    self.data = data

  def __repr__(self):
    return "<Node data: %s>" % self.data

class LinkedList:
  """
  Singly linked list
  """

  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None
  
  def size(self):
    """
    Returns the number of nodes in the list
    Takes O(n) time
    """
    current = self.head
    count = 0

    while current:
      count += 1
      current = current.next_node

    return count
  
  def add(self, data):
    """
    Prepend a node containing data (data) to the beginning of the list
    Adds new Node containing data at head of the list
    Takes O(1) time
    """
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

  def search(self, key):
    """
    Search for the first node containing data that matches the key (In this linked list 'key' would be the value to find)
    Return the node or `None` if not found
    Takes O(n) time
    """

    current = self.head

    while current:
      if current.data == key:
        return current
      else:
        current = current.next_node

    return None
  
  def insert(self, data, index):
    """
    Insert a new Node containing data at index position
    Insertion takes O(1) time but finding the node at the insertion point takes O(n) time
    Takes overall O(n) time
    """

    if index == 0:
      self.add(data)

    if index > 0:
      newNode = Node(data)

      position = index
      current = self.head

      while position > 1:
        current = current.next_node
        position -= 1

      prev_node_to_the_new_node = current
      next_node_to_the_new_node = current.next_node

      prev_node_to_the_new_node.next_node = newNode
      newNode.next_node = next_node_to_the_new_node

  def remove(self, key):
    """
    Remove node containing data that matches the key (key = value to find)
    Return the node or `None` if key (key = value to find) doesn't exist
    Takes O(n) time
    """

    current = self.head
    prev_node_to_the_to_be_deleted_node = None
    found = False

    while current and not found:
      if current.data == key and current is self.head:
        found = True
        self.head = current.next_node
      elif current.data == key:
        found = True
        prev_node_to_the_to_be_deleted_node.next_node = current.next_node
      else:
        prev_node_to_the_to_be_deleted_node = current
        current = current.next_node

    return current
  
  def node_at_index(self, index):
    """
    Returns the node at specified index
    Takes O(n) time
    """

    if index == 0:
      return self.head

    current = self.head
    position = 0

    while position < index:
      current = current.next_node
      position += 1

    return current
    
  def __repr__(self):
    """
    Return a string representation of the list
    Takes O(n) time
    """
    
    nodes = []
    current = self.head

    while current:
      if current is self.head:
        nodes.append("[Head: %s]" % current.data)
      elif current.next_node is None:
        nodes.append("[Tail: %s]" % current.data)
      else:
        nodes.append("[%s]" % current.data)

      current = current.next_node

    return '->'.join(nodes)


# N1 = Node(10)
# print(N1)

# N2 = Node(20)
# N1.next_node = N2

# print(N1.next_node)