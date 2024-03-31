class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        area = .5 * self.base * self.height
        print('Area is : ',area)

a1 = Triangle(10,20)
a1.calculate_area()

a2 = Triangle(20,30)
a2.calculate_area()