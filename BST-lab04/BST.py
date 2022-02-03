#code from bst we did in class made by Prof. German. My implementation is REMOVE 
class BST:
    def __init__(self, value, left, right):
        self.key = value # an integer 
        self.left = left # a subtree, a BST
        self.right = right # another subtree 

    def insert(self, value):
        if value < self.key:
            if self.left == None:
                self.left = BST(value, None, None) # test 
            else:
                self.left.insert(value)
        elif value > self.key:
            if self.right == None:
                self.right = BST(value, None, None) # test 
            else:
                self.right.insert(value)
        else:
            pass

    def getMaxLeft(self):
      if self.right:
        self.right.getMaxLeft()# is right is not none meants that its not the max of left subtree since  most right is always max
      else:
        return self.key #if none then we reached max so we return root of that subtree

    def remove(self, value):
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
        self.left = self.left.remove(value)
      elif value > self.key and self.right:
        self.right = self.right.remove(value)

      return self

    def removeNew(self, value):
      if value is self.key: #= position pointer at root so base case
        if self.left is None:
          return self.right # left is none so move one up to right
        elif self.right is None: 
          return self.left # right is none so move up to left
        
      if value < self.key and self.left:
         self.left = self.left.removeNew(value)
      elif value > self.key and self.right:
         self.right = self.right.removeNew(value)

      return self
        
        


    def show(self):
        if self.left == None: left = "."
        else: left = self.left.show()
        if self.right == None: right = "."
        else: right = self.right.show()
        return "( " + left + " " + str(self.key) + " " + right + " )"


    def display(self): #---------------------( display )---------------- 
        lines, *_ = self._display_aux() 
        for line in lines: 
          print(line)
          
          # method for understanding this function
          # print each first second and shifted lines in separate file or case with simulation data (refer to yp.py file)
          # follow each step and each variable 
    def _display_aux(self): 
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
          line = '%s' % self.key # the key
          width = len(line) #1
          height = 1 #depth of the tree
          middle = width // 2 #// divisional floor
          return [line], width, height, middle 
        # Only left child.
        if self.right is None:
          lines, n, p, x = self.left._display_aux() #list of lines, n = width, p = height, x = middle
          s = '%s' % self.key
          u = len(s) # width on the self
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
          second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' ' # '\\' means '\'
          shifted_lines = [u * ' ' + line for line in lines]
          return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left._display_aux() #[8], 1, 1, 0       #left LoL, width, height, mid
        right, m, q, y = self.right._display_aux() #[12], 2, 1, 1    #right LoL, width, height, mid
        s = '%s' % self.key #11
        u = len(s) #2
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        # lowest depth matters
        if p < q:
          left += [n * ' '] * (q - p)
        elif q < p:
          right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2 #max lowest depth is most relevant

# a = BST(9, BST(1, None, None), None)

# print(a.show())

# a.insert(8)

# a.display()

# a.insert(2)

# a.display()
# print("=====Remove=with=Promotion=====")

# for value in (7, 3, 6, 4, 5):
#     a.insert(value)
#     # print("------------")
#     # print(a.show())
#     # a.display()

# print(a.show())
# a.display()
# a = a.remove(7)
# print(a.show())
# a.display()
# a = a.remove(6)
# print(a.show())
# a.display()
# a = a.remove(2)
# print(a.show())
# a.display()




# b = BST(9, BST(1, None, None), None)

# # print(b.show())

# b.insert(8)

# # b.display()

# b.insert(2)

# # b.display()
# print("=====Remove=without=Promotion=====")

# for value in (7, 3, 6, 4, 5):
#     b.insert(value)
#     # print("------------")
#     # print(b.show())
#     # b.display()

# print(b.show())
# b.display()

# b = b.removeNew(7)
# print("remove 7")
# print(b.show())
# b.display()
# b = b.removeNew(6)
# print("remove 6")
# print(b.show())
# b.display()
# b = b.removeNew(2)
# print("remove 2")
# print(b.show())
# b.display()

b = BST(11, BST(8, None, None), None)
b.insert(6)
b.insert(7)
b.insert(10)
b.insert(6)
b.insert(12)
b.display()

c = BST(11, BST(8, None, None), BST(12, None, None))
# c.display()

# import random

# b = BST(50, None, None)
# for _ in range(50):
#     b.insert(random.randint(0, 100))
# b.display()