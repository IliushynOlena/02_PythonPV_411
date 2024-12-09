'''
login = "admin"

login = 'user'
print(login)


a,b,c = 1, 3 ,5
print(a,b,c)

a = b =c = 2# <-------------------
print(a,b,c)

print("1 == 1:", 1 == 1)   #True      
print("1 == 2:", 1 == 2)   #False     
print("1 != 1:", 1 != 1)    #False     
print("1 != 2:", 1 != 2)    #True    
print("1 > 1:", 1 > 1)      #False    
print("1 > 2:", 1 > 2)      #False    
print("2 > 1:", 2 > 1)      #True    
print("1 < 1:", 1 < 1)      #False    
print("1 < 2:", 1 < 2)      #True    
print("2 < 1:", 2 < 1)      #False    
print("1 >= 1:", 1 >= 1)    #True    
print("1 >= 2:", 1 >= 2)     #False   
print("2 >= 1:", 2 >= 1)    #True    
print("1 <= 1:", 1 <= 1)    #True    
print("1 <= 2:", 1 <= 2)    #True    
print("2 <= 1:", 2 <= 1)    #False      

print(bool(""))
print(bool(0))
print(bool(0.00))
print(bool(None))
print(bool("It step"))
print(bool(5))
print(bool(-10))


# and
competent = True
responsible = False
print(competent and responsible)

# or
competent = False
responsible = False
print(competent or responsible)

# not
competent = False
print(not competent)

age = int(input("Enter age : "))

#if age >= 18 and age <= 125:
if 18 <= age <=  125:
    print("Welcome to my game!!!")
else:
    print("You are too younger.... Goodbye!!!")
'''
'''
day = int(input("Enter number of day [1-7] : "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Error number day")
'''

login = input("Enter login ")

if login == "admin":
    password = input("Enter password : ")
    if password == "qwerty":
        print("Welcome !!!!")
    else:
        print("Error password")
elif login == 'exit':
   print("Goodbye!")
else:
   print("Error")
#number %2 == 0
#number %2 == 1