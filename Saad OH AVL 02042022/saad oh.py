#Followed my pseudocode 
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
	  
	def balance(self): #returns the balance calculations based on depth
		if self.left == None and self.right == None: 
			return 0
		elif self.left == None: 
			return 0 - self.right.depth()
		elif self.right == None: 
			return self.left.depth()
		else: 
			return self.left.depth() - self.right.depth()
	#the 4 different transformation forms
	def formOne(self, right, left): # where b is right of root, a is root, c is rright right, 1 is l, 2 is rl, 3 is rrl, 4 is rrr
	  return 

    def formTwo(self, right, left): # where b is lr, a is l, c is root, 1 is ll, 2 is lrl, 3 is lrr, 4 is r
	  return 

	def formThree(self, right, left): # where b is RL, a is root, and c is l, 1 is r, 2 is rll, 3 is rlr, 4 is lll so follow the path where self is root reSi is right and leSi is left since traversal
	  return 
	
	def formFour(self, right, left): # where b is l, c is root, a is ll, 4 is r, 3 is lr, 2 is llr, 1 is lllr
		return 

	def fourTreeTrans(self):
		if self.left == None: #set node to left side and depth starts 0 base case
			
		else: # recursion/update depth 
			
		if self.right == None: #set node to right side and depth starts 0 base case
			
		else: # recursion/update depth 
			
		if depl - depr < -1: #balance of tree calc this is for right
			if reSi.balance() > 0: # form 3 
				return 
			else: # form 1
				return 
		elif depl - depr > 1: # balance of tree for left
			if leSi.balance() < 0: # form 2 
				return 
			else: # form 4 
				return 
		return #default

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