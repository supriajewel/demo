# loops in python

#a = ["abdul","baten","chouduri","denmark","england"]

#for b in a:
#for b in a[2:]:
#for b in a[:3]:
#for b in a[3:5]:

# print the reverse value
#for b in a[::-1]:
#for b in a[3::-1]:
#for b in a[4:1:-1]:

#print a range of number where 0 is the startung, 9 is the ending value (n-1) and 2 is the increment
#for b in range(0,9,2):
#for b in range(7,0,-1):   #reverse print

#passing a value to range function for loop execution
#n = int(input('Please enter a value :'))

#for b in range(1,n):

#bd = "bangladesh"
#cnt = 0

#for b in bd:
    #cnt += 1
    
    #print(b)
#print(cnt)
#print(len(bd))

# create a dictonary
student = [
    {
        "id":203, 
        "name":"jewel", 
        "age": 45
    },
    {
        "id":204, 
        "name":"faiza", 
        "age": 7
    },
    {
        "id":205, 
        "name":"fahima", 
        "age": 35
    }
]

#print(student[1])

# FIND THE AVERAGE AGE FROM A DICTONARY
  
  # FIND THE AGE FIRST FROM DICTONARY
#age = student[1]['age']
#print(age)

#tot_age = sum(i['age'] for i in student)     # total age calculation (advance)

#-----------------------
#tot_age=0

#for i in student:
#    tot_age +=i['age']

#print("Total age is: ",tot_age)
#print("Average age is: ", tot_age/len(student))
#--------------------------

# while loop
#i = 0
#while i<3:
#    print("JEWEL")
#   i +=1

# sum from 1 to given number and print

n = int(input("please provide a number to sum them : "))
i = 0
total = 0

while i<=n:
    total = total + i
    i +=1
print(total)



