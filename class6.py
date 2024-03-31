#create a list having dictonar
# Find the average salary 
# prind the name of all employees

employees = [
   {
        "id" : 101,
        "name": "jewel",
        "position": "system eng",
        "salary": 70000
    },
   {
        "id" : 102,
        "name": "fahima",
        "position": "dba",
        "salary": 50000
    },
   {
        "id" : 103,
        "name": "faiza",
        "position": "software eng",
        "salary": 60000
    }
    
    ]

#total_sal =0
#cnt = 0

#for i in employees:
#    total_sal += i['salary']
#    cnt +=1

#Both way are correct
#print('The average salary of all employees is: ',total_sal/len(employees))
#print('The average salary of all employees is: ',total_sal/cnt)

# print all employees name

#print('The name of all employees are : ')

#for i in employees:
#    print( i['name'])

# create a list and update from employees dictonary
#emp_names = []

#for i in employees:
#    emp_names.append(i['name'])
#print(emp_names)

###################    short cut way by using list comprhension    #########################
#total_sal =sum([i['salary'] for i in employees])
#print ('Average salary is : ',total_sal/len(employees))

#emp_names = [i['name'] for i in employees]
#print('The name of all employees are : ', emp_names)

##############################                ####################################

##############################     Function   #################################### 

#def add():
#    a = int(input('Please enter first value: '))
#   b = int(input('Please enter second value: '))
#    print(a+b)

#add()

# function with require arguments

#def addition(x,y):
#    z=x+y
#    print(z)

#addition(2,6)

# function with required arguments
#def display(fname:str, lname:str):
#   msg = 'Hello,  {} {}'.format(fname,lname)
#    print (msg)

#display('jewel','munshi')

# function with default arguments

def display(fname:str, lname:str, mname=None):
   if mname == None:
      msg = 'Hello,  {0} {1}'.format(fname,lname,mname)
      print (msg)
   else:
      msg = 'Hello,  {0} {2} {1}'.format(fname,lname,mname)
      print (msg)

fname = input('Enter your first Name: ')
mname = input('Enter your Middle Name: ')
lname = input('Enter your Last Name: ')

display(fname,lname,mname)











