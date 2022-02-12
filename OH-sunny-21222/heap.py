class Heap:
  def __init__(self, key):
    self.key = key
    self.right = None
    self.left = None
  def size(self):
    if self.left == None and self.right == None:
      return 1
    elif self.left == None:
      return 1 + self.right.size()
    elif self.right == None:
      return 1 + self.left.size()
    else: 
      return 1 + self.right.size() + self.left.size()
  def depth(self):
    if self.left == None and self.right == None:
      return 1
    elif self.left == None:
      return 1 + self.right.depth()
    elif self.right == None:
      return 1 + self.left.depth()
    else: 
      return 1 + max(self.right.depth(), self.left.depth())

  def insert(self, value):
    path = "{0:b}".format(self.size() + 1)
    # print(self.size() + 1, "---> ", path)
    self.helper(path[1:], value)

  def helper(self, path, value):
    if path == "1":
      self.right = Heap(value)
    elif path == "0":
      self.left = Heap(value)
    else:
      nextStep = path[0]
      if nextStep == '0':
        self.left.helper(path[1:], value)
      else:
        self.right.helper(path[1:], value)
      
  def remove(self, value, path):
      if value == self.key: #= position pointer at root so base case
        if self.left == None:
          return self.right # left is none so move one up to right
        elif self.right is None: 
          return self.left # right is none so move up to left
        else:
          newNode = self.left.getMaxLeft() # if children exist the find largest of left side like in class and promote to root of subtree
          self.key = newNode
          self.left = self.left.remove(newNode) # 
          print("hit")
      
      if value < self.key and self.left:
        path = path + str(0)
        self.left = self.left.remove(value, path)
      elif value > self.key and self.right:
        path = path + str(1)
        self.right = self.right.remove(value, path)
      #self.remHelper(path)
      return self
  def remHelper(self, path):
    if path == "1":
      self.right = None
    elif path == "0":
      self.left = None
    else:
      nextStep = path[0]
      if nextStep == '0':
        self.left.remHelper(path[1:])
      else:
        self.right.remHelper(path[1:])

  
  def display(self):
    lines, *_ = self._display_aux()
    for line in lines:
      print(line)
  def _display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if self.right is None and self.left is None:
      line = '%s' % self.key
      width = len(line)
      height = 1
      middle = width // 2
      return [line], width, height, middle
    # Only left child.
    if self.right is None:
      lines, n, p, x = self.left._display_aux()
      s = '%s' % self.key
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
      second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
      shifted_lines = [line + u * ' ' for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
    # Only right child.
    if self.left is None:
      lines, n, p, x = self.right._display_aux()
      s = '%s' % self.key
      u = len(s)
      first_line = s + x * '_' + (n - x) * ' '
      second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
      shifted_lines = [u * ' ' + line for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
    # Two children.
    left, n, p, x = self.left._display_aux()
    right, m, q, y = self.right._display_aux()
    s = '%s' % self.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
      left += [n * ' '] * (q - p)
    elif q < p:
      right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2



#so value to be inserted cehck base cases for recusrion
#going to track insertion based on memory location (0110)
#convert size to binary for memory location then insert at that location

    
import random

# b = Heap(100)
# b.display()
# for _ in range(99, 40, -1):
#   input("----------------( now inserting " + str(_) + " )--")
#   b.insert(_)
#   b.display()

b = Heap(6)
b.insert(4)
b.insert(3)
b.insert(1)
b.display()
b.remove(1, "")
b.display()