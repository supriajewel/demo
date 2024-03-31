class phone:
    def __init__(self):
        print('I am from Phone class')


class sumsung(phone):
    #pass                                      ## it will just print the phone method
    
    def __init__(self):                       ## It is just overriding phone's (BASE) constractor

       super().__init__()                    ## we can also call the phone(BASE) constractor
        
       print('I am from Sumsung Class')


p = sumsung()
