#Followed my pseudocode 
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

class AVL(BST):

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
	  
	def balance(self):
		if self.left == None and self.right == None: 
			return 0
		elif self.left == None: 
			return 0 - self.right.depth()
		elif self.right == None: 
			return self.left.depth()
		else: 
			return self.left.depth() - self.right.depth()

	def formOne(self, right, left): # where b is right of root, a is root, c is rr, 1 is l, 2 is rl, 3 is rrl, 4 is rrr
	  return AVL(right.key, AVL(self.key, left, right.left), AVL(right.right.key, right.right.left, right.right.right))

    def formTwo(self, right, left): # where b is lr, a is l, c is root, 1 is ll, 2 is lrl, 3 is lrr, 4 is r
	  return AVL(left.right.key, AVL(left.key, left.left, left.right.left), AVL(self.key, left.right.right, right))

	def formThree(self, right, left): # where b is RL, a is root, and c is l, 1 is r, 2 is rll, 3 is rlr, 4 is lll so follow the path where self is root reSi is right and leSi is left since traversal
	  return AVL(right.left.key, AVL(self.key, left, right.left.left), AVL(right.key, right.left.right, right.right))
	
	def formFour(self, right, left): # where b is l, c is root, a is ll, 4 is r, 3 is lr, 2 is llr, 1 is lllr
		return AVL(left.key, AVL(left.left.key, left.left.left, left.left.right), AVL(self.key, left.right, right))

	def fourTreeTrans(self):
		if self.left == None: #set node to left side and depth starts 0 base case
			depl = 0
			leSi = None
		else: # traversal/depth tracker
			leSi = self.left.fourTreeTrans()
			depl = leSi.depth()
		if self.right == None: #set node to right side and depth starts 0 base case
			depr = 0
			reSi = None
		else: # traversal/depth tracker
			reSi = self.right.fourTreeTrans()
			depr = reSi.depth()
		if depl - depr < -1: #balance of tree calc this is for right
			if reSi.balance() > 0: # form 3 
				return self.formThree(reSi, leSi)
			else: # form 1
				return self.formOne(reSi, leSi)
		elif depl - depr > 1: # balance of tree for left
			if leSi.balance() < 0: # form 2 
				return self.formTwo(reSi, leSi)
			else: # form 4 
				return self.formFour(reSi, leSi)
		return AVL(self.key, leSi, reSi)

#now for testing case Im going to use the pseudocode test we made since the pseudocode was used here
arr = [2, 3, 5, 4, 6, 7]
a = AVL(1)

# print("==========Normal BST Implementation without left and right Shifts==========")
# for x in arr:
# 	print("Inserting... ", x)
# 	a.insert(x)
# 	a.display()

print("==========AVL Implementation==========")
for x in arr:
	print("Inserting...", x)
	a.insert(x)
	a = a.fourTreeTrans()
	a.display()

print("==========DELETE==========")
for y in arr:
	print("Deleting...", y)
	a.remove(y)
	a = a.fourTreeTrans()
	a.display()