class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    
    def area(self):
        result = self.dim1 + self.dim2
        print('The sum is : ', result)

class Triangle(Shape):

    def area(self):                          # over ride the Base 'area' methods

        super().area()                       # call base class area method using super method

        result = .5 * self.dim1 * self.dim2
        print('The triangle is : ', result)

class Rectengle(Shape):
    def area(self):                          # over ride the Base 'area' methods
        result = self.dim1 * self.dim2

        print('The Rectangle is : ', result)


t1 = Triangle(10,20)
t1.area()

r1 = Rectengle(10,20)
r1.area()

