class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(self.a , "+", self.b, "i")

# (self.a + n2.a) + (self.b + n2.b) * i
#  self.a       + self.b        i
    def add(self, n2):
        self.a = self.a + n2.a
        self.b = self.b + n2.b
        return self
    # (self.a + i*self.b) * (n2.a + i*n2.b)
    # (self.a * n2.a) + (self.a * i*n2.b) + (i*self.b * n2.a) + (self.b * n2.b)*-1
    # self.a = (self.a * n2.a) - (self.b * n2.b), self.b = (self.a * i*n2.b) + (i*self.b * n2.a)
    def multiply(self, n2):
        self.a = (self.a * n2.a) - (self.b * n2.b)
        self.b = (self.a * n2.b) + (self.b * n2.a)
        return self

complex_one = Complex(3, 2)
complex_two = Complex(5, 6)
complex_one.show()
complex_two.show()
# new_number = complex_one.add(complex_two) 
# new_number.show()#8 + 8i

new_number = complex_one.multiply(complex_two)
new_number.show() #3 + 28i



