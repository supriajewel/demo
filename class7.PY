# Required parameter function
# declare a list and update them from input value

# contacts = [

# ]

# def display(name:str, email:str, message:str):
#     contacts.extend({name,email,message})

# name = input('Enter your name: ')

# if name:
#     email = input('Enter your email: ')
#     if email:
#        message = input('Please enter your message: ')
#        if message:
#             display(name,email,message)
#             print(contacts)
#        else:
#            print('This address is require.')
#     else:
#         print('Email fild is require.')
# else:
#     print('This Name fiels is Require.')



# function with default parameter
# declare a list and update them from input value

# contacts = [

# ]

# def display(name:str,phone:str,message:str,email=None):   #### all the default value must be place at the end of the parameter list
#     contacts.extend({name,phone,message,email})

# name = input('Enter your name :')

# if name:
#     phone = input('Please enter Your phone Number: ')
#     if phone:
#         message = input('Enter your Message: ')
#         if message:
#             email = input('Enter your email: ')
#             display(name,phone,message,email)
#             print(contacts)
#         else:
#             print('Message is required.')
#     else:
#         print('Phone is Required.')
# else:
#     print('Name field is required.')


# variable leangth arguments which works with tuple ( it support any number of arguments)

# def add(*args):
#     sum = 0
#     for i in args:
#         sum +=i
    
#     print(sum)

# add(2,3,5,6)
# add(2,3,5,6,7,8,9,10)
# add(2,3,5,6,7,8,9,10,11,12,17)

#function with keyworded arguments


contacts = [

]

def display(**kwargs):         ### working with dictonary
    contacts.append(kwargs)

name = input('Enter your name :')

if name:
    phone = input('Please enter Your phone Number: ')
    if phone:
        message = input('Enter your Message: ')
        if message:
            email = input('Enter your email: ')
            display(name=name,phone=phone,message=message,email=email)
            print(contacts)
        else:
            print('Message is required.')
    else:
        print('Phone is Required.')
else:
    print('Name field is required.')