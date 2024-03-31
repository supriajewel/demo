# list and tuple
a = [1,2,3,4,5,6,7,8,9,10]


#print ("Type is: ",type(a))   # print the type

#print ("leangth is: ",len(a))   # print the type

#print("Print all the values: ",a)          # print all the value

#print("index vale of 2 is: ", a[2])        # print index wise the value

#print(a[-4])    # backword indexing and select the number 7

#print(a[-5:8])   # backword indexing with a range of value

# update a list (indexwise)
a = ['java','python','c','c++','go','dart']

#a[1] = 'python programming'   # update the value of 1 index

# delete from list (indexwise)

#del(a[4])  # delete the index value of 4

#a.remove('c')  # delete from list according to the value

#a.pop()     # delete from the last as per " first in last out"

#a.pop(1)     # delete as per index value

#a.clear()     # clear the list

#del a          # delete the list

# adding new value to a list
#a.append("java scripts")        # adding single value into the last index

#a.extend(['javascripts','swift','rubi'])  # adding multiple item into the list default index is the last one

#a.insert(1,'rubi')     # insert into the index as per index value

# adding two list togather into a third list
list1 = [1,7,5,4,6,3,2]
#list2 = [6,7,8,9,10]

#list3=list1+list2

#print(list3)        #print the all the value from list3

#print(list3 * 3)     # repeating a list into 3 times

# membership operator 
#print(3 in list1)     # for searching a specific value into the list and return boolean

# loop in a list

#for i in a:
#   print(i)

# other functions

#list4 = list1.copy()        # copy a list

#list4 = list(list1)        # copy a list with list function

# sorting a list 

#list1.sort()     # assending is default of sort function

#list1.sort(reverse=True)     # decending sort

#list5 = [1,3,2,9]

#list5.reverse()               # reverse a list 

# list comprehension with a range value

#nums = [x for x in range(1,10) if x%2 == 0] 

# alternatively we can do the above task with for loop
#nums = []
#for i in range(1,10):
#    if i % 2 == 0:
#       nums.append(i)
#print(nums)

#nums = [x for x in range(1,10) if x%2 == False]    # print all the even value of a range

#nums = [x for x in range(1,10) if x%2 == True]    # print all the odd value of a range
#print(nums)

# more comprrhensive example
#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist = [x for x in fruits if "a" in x]

# alternative way to do the above coding
#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist =[]

#for i in fruits:
#    if 'a' in i:
#        newlist.append(i)

#print(newlist)

########################  difference between list and tuple and their charecteristics ####################
#  1. both list and tuple are allow to access their value
#  2. both list and tuple are allow duplicate value
#  3. list is changeable means allowing insert, update, delete
#  4. Tuple is unchangeable means it doesn't allow insert, update, delete. it is containg fixed values


##### Tuple ######
##### unpacking Tuple ######

#fruits = ("apple", "banana", "cherry")

#(green, yellow, red) = fruits   # declare 3 veriables as green, yellow and red. assigning values for them from "fruits" tuple

#print(green, yellow, red)
# OR Print like a single variable
#print(green)
#print(yellow)
#print(red)

###### count() Method

#thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
#x = thistuple.count(5)
#print(x)

######## index() Method. it is finding the index position of a specific value in tuple #########
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(4)
print(x)
















