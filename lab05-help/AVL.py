class BST:
    def __init__(self, value, left = None, right = None):
        self.key = value # an integer 
        self.left = left # a subtree, a BST
        self.right = right # another subtree 
    def insert(self, value): #-----------------( insert )-----------------
        if self.key == value:
            return self
        elif self.key < value:
            if self.right is None: 
                self.right = BST(value, None, None)
            else: 
                self.right.insert(value)
        else:
            if self.left is None: 
                self.left = BST(value, None, None)
            else: self.left.insert(value)

    def remove(self, value):
        if value == self.key: #= position pointer at root so base case
            if self.left == None:
                return self.right # left is none so move one up to right
            elif self.right is None: 
                  return self.left # right is none so move up to left
            else:
                newNode = self.left.key # if children exist the find largest of left side like in class and promote to root of subtree
                self.key = newNode
                self.left = self.left.remove(newNode) 
        if value < self.key and self.left:
            self.left = self.left.remove(value)
        elif value > self.key and self.right:
            self.right = self.right.remove(value)
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

a = BST(2, BST(3, None, None), BST(5, None, None))
a.display()

class AVL(BST):

    def getDepth(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left == None:
            return 1 + self.right.getDepth()
        elif self.right == None:
            return 1 + self.left.getDepth()
        else:
            return 1 + max(self.left.getDepth(), self.right.getDepth())
    
    def getBalance(self):
        if self.left == None and self.right == None:
            return 0
        elif self.left == None:
            return 0 - self.right.getDepth()
        elif self.right == None:
            return self.left.getDepth()
        else:
            return self.left.getDepth() - self.right.getDepth()
    
    def insert(self, value):
        if self.key == value:
            return self
        elif self.key < value:
            if self.right is None: 
                self.right = AVL(value, None, None)
            else: 
                self.right.insert(value)
        else:
            if self.left is None: 
                self.left = AVL(value, None, None)
            else: self.left.insert(value)

# b = AVL(4)
# b.display()
# b.insert(5)
# b.insert(7)
# b.display()
# print()

    def l_rotation(self, left, right):
        
        return AVL(right.key, AVL(self.key, left, right.left), AVL(right.right.key, right.right.left, right.right.right))
    
    def lr_rotation(self, left, right):
        
        return AVL(right.left.key, AVL(self.key, left, right.left.left), AVL(right.key, right.left.right, right.right))

    def r_rotation(self, left, right):
        
        return AVL(left.key,  AVL(left.left.key, left.left.left, left.left.right), AVL(self.key, left.right, right))
    
    def rl_rotation(self, left, right):
        
        return AVL(left.right.key, AVL(left.key, left.left, left.right.left), AVL(self.key, left.right.right, right))

    def fourForms(self):
        if self.left == None:
            depl = 0
            lesi = None
        else:
            depl = self.left.getDepth()
            lesi = self.left.fourForms()
        if self.right == None:
            depr = 0
            resi = None
        else:
            depr = self.right.getDepth()
            resi = self.right.fourForms()
        if depl - depr < -1:
            if resi.getBalance() > 0:
                return self.lr_rotation(lesi, resi)  
            else:
                return self.l_rotation(lesi, resi)
        elif depl - depr > 1:
            if lesi.getBalance() < 0:
                return self.rl_rotation(lesi, resi)  
            else:
                return self.r_rotation(lesi, resi)
                
        return AVL(self.key, lesi, resi)
        
arr = [2, 3, 5, 4, 6, 7]
a = AVL(1)
print("==========AVL Implementation==========")
for x in arr:
	print("Inserting...", x)
	a.insert(x)
	a = a.fourForms()
	a.display()
a.remove(2)
a.display()
a.remove(4)
a.display()
    
