# Inheritance
# There are 3 types of inheritence

# 1. single inheritance (one base class and one child class)

# class person:
#     name = ''
#     address = ''

#     def display(self):
#         print(f'Your Name is {self.name} and address is {self.address}')

    
# class employee(person):
#     pass

# obj1 = employee()
# obj1.name = 'Jewel'
# obj1.address = 'Faridpur, Dhaka'
# obj1.display()

# obj2 = person()
# obj2.name = 'Faiza'
# obj2.address = 'Savar, Dhaka'
# obj2.display()

################# 2. Multiple inheritence (two or more base class and one child class)

# class Father:
    
#     def __init__(self, fname):
#         self.fname = fname
    
#     def display1(self):
#         print(f'Father name is {self.fname}')


# class Mother:
#     def __init__(self,mname):
#         self.mname = mname
    
#     def display2(self):
#         print(f'Mother Name is {self.mname}')

# class Child(Father, Mother):
#     def __init__(self, fname, mname, name):
#         Father.__init__(self, fname)
#         Mother.__init__(self, mname)
#         self.name = name
    
#     def display3(self):
#         print(f'Child Nmae is {self.name}')

# c1 = Child('Jewel','Fahima','Faiza')
# c1.display1()
# c1.display2()
# c1.display3()

######## 3. Multi Level Inheritence or hierarchical inheritance ( Grand Father --> Father --> Son )


