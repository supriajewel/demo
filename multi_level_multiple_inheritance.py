### Multi level Inheritance

# class A:

#     def display1(self):
#         print("This is class 'A'")

# class B(A):

#     def display2(self):
#         print("This is class 'B' ")

# class C(B): 
#     def display3(self):
#         super().display1()        # we can also call display1() methods using super method
#         super().display2()        # we can also call display2() methods using super method
#         print("This is class 'C' ")


# #obj1 = C()
# #obj1.display1()    # we can also call display1() and diplay2() by using super method insite display3()
# #obj1.display2()
# #obj1.display3()

# obj1 = C()
# obj1.display3() 

### Multi level Inheritance

class A:
    def display(self):
        print("This is class 'A'")

class B:
    def display(self):
        print("This is class 'B' ")


class C(A,B):                         
    def display(self):
        pass

        #print("This is class 'C' ")      
    
        # Aa per priroty it will print display() of class C. But if we stop to call this then it will call the 
        # Class display() of class "A". Because we inharite Class "A" first.


obj1 = C()
obj1.display()                      ####  ERROR  ###### It is return nothing












