import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def distanceTo(self, p2):
        length = math.sqrt((self.x-p2.x)**2+(self.y-p2.y)**2)
        return length


a = Point(3, 2)
b = Point(-1, 5)
print(a) # prints: (3, 2)
# print("I have two point objects: " + str(a) + " " + str(b))
# # I have two point objects: (3, 2) (-1, 5)
howFar = a.distanceTo(b)
print(howFar) # prints 5


a = Point(0, 0)
b = Point(1, 1)
print("Distance from " + str(a) + " to " + str(b) + " is: " + str(a.distanceTo(b)))

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def distanceBet(self):
        length = self.p1.distanceTo(self.p2) 
        return length

line = Line(a, b)
length = line.distanceBet()
print("length of the line is ", length) #1.41

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def area(self):
        a = self.p1.distanceTo(self.p2)
        b = self.p2.distanceTo(self.p3)
        c = self.p3.distanceTo(self.p1)
        s = (a + b + c)/2
        area = math.sqrt(s * (s-a) * (s-b) * (s-c))
        return area

a = Point(3, 2)
b = Point(-1, 5)
c = Point(0, 0)
triangle = Triangle(a, b, c)
print(triangle.area()) #8.5

class LinkedList:
    def __init__(self, value, rest):
        self.first = value # value of the head
        self.rest = rest #empty or itself
    def show(self):
        if self.rest == None:
            return str(self.first) + " ."
        else:
            return str(self.first) + " " + self.rest.show()

a = LinkedList(9, LinkedList(-2, None)) #(9 (-2 empty))

print(a.show()) # 9 -2 . 

class Queue:
    def __init__(self):
        self.data = None
    def show(self):
        if self.data == None:
            return "front: ."
        else:
            return "front: " + self.data.show()
    def add(self, value):
        if self.data == None:
            self.data = LinkedList(value, None)
        else:
            morgan = self.data
            while morgan.rest != None:
                morgan = morgan.rest
            morgan.rest = LinkedList(value, None)
        


a = Queue()
print(a.show()) # front: .
a.add(3)
a.add(5)
a.add(-1)
print(a.show()) # front: 3 5 -1 . 


class Tree:
    def __init__(self, value, left, right):
        (self.value, self.left, self.right) = (value, left, right)


    def show(self):
        if self.left == None:
            left = " . "
        else:
            left = self.left.show()
        if self.right == None:
            right = " . "
        else:
            right = self.right.show()
            # return "(" + left + " " + str(self.value) + " " + right + ")"
        return "(" + str(self.value) + " " + left + " " + right + ")"
    
    def add(self, value):
        if value < self.value:
            if self.left == None:
                self.left = Tree(value, None, None)
            else:
                self.left.add(value)
        elif value > self.value:
            if self.right == None:
                self.right = Tree(value, None, None)
            else:
                self.right.add(value)
        else:
            self.value = value

    

a = Tree (5, None, None)
print(a.show())

a = Tree (1, a, None)
print(a.show())

a = Tree(2, Tree(4, None, None), a)
print(a.show())



b = Tree(2, None, None)
print(b.show())
b.add(5)
b.add(1)
b.add(3) 
print(b.show())
