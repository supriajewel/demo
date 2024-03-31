# File Handling operation  ( Read)

# alternative way to open a file as follow
#with open('demo.txt', 'r') as file:
#    pass


#file = open('demo.txt', 'r')  # where r is the default value

#val = file.read()             # read and store them into a variable
#print(val)                    # print the content
#print(file.read())            # also we can print directly

#val = file.readable()         # check is it readable or not

#val = file.readline()        # its read only first line

#val = file.readlines()        # read all the lines and store theam into a list

#val = len(file.readlines())    # print how many lines into the file
#print(val)   


# File Handling operation  ( write )

#file = open('demo.txt', 'w')            # if file not found then it will create a new file with the given name

#val = file.writable()                   # its retrun that is it writable or not

#file.write('my phone number is 01777776740')        # it will overwrite all hole file
#file.writelines(['hello ', 'jewel ', 'how are yo?'])     # it received iterable object or multiple objects

# File Handling operation  ( append )

#file = open('jewel.txt', 'a')           # if file not found then it will create a new file with the given name

#file.write(' hello')
#file.write(' jewel')

# File Handling operation  ( delete )

#file.close()                            # close the file first. if it is open

# import os
# os.remove('jewel.txt')


################### exception handeling ###################

# syntax error

# x = 4
# y=0

# z = x/y              # this will provide error "division by zero"

# print(z)

################### exceptopn handling syntax   #############################3
# try:
#     pass

# except:
#     pass

#############################################################################

try:
    x = int(input('Please enter the first value: '))
    y=int(input('Please enter the second value: '))
    z = x/y
    
    print(z)

# except ZeroDivisionError as e:                   # buid in error code "ZeroDivisionError"
#     #err = str(e).title()
#     #print(err)
#     print(e)                                   # we can also simple print any custom message

#     ### if the input value given string rather then integer then it will generate value error. we can handle them with another exption

# except ValueError as v:
#     #err = str(v).title()
#     print(v)

# the best way to hanle the error

except Exception as e:                           # we can also catch the error with exception procedure and print for all error
    print(e)

else:                        # else block will work when try block is successful
    print('Right execution')   

finally:
    print('Thank, try again')       # this block will execute both success and error process






