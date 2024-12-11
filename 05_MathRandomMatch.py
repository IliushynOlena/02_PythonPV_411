
# print(" 1 - add \n 2 - minus\n 3 - avg\n 4 - divede \n")

# key = int(input("Enter your choice : ")) 
# if key == 1:
#     print("+")
# elif key == 2:
#     print("-")
# elif key == 3:
#     print("avg")
# elif key == 4:
#     print("/")

# print(" [+] - add \n [-] - minus\n [*] - multy\n [/] - divede \n")
# choice = input("Enter your choice : ")
# if choice == '+':
#     print("+")
# elif choice == '-':
#     print("-")
# elif choice == '*':
#     print("avg")
# elif choice == '/':
#     print("/")

# number = int(input("Enter number : "))#50
# percentage = int(input("Enter percentage : ")) #10
# result =  number *percentage/100#5

a = 7
b = 9
c = 12
print(a,b,c)
print("a = ", a, "b = ", b, "c = ", c)
print("a =", a, ".", "b =", b,".", "c =", c, ".")
print("Numbers : a = {}. b = {}. c = {}.".format(a,b,c))
print("Numbers : a = {}. b = {}. c = {}.".format(b,c,a))
print("Numbers : a = {}. b = {}. c = {}.".format(c,a,b))
print(f"Numbers : a = {a}. b = {b}. c = {c}.")


#one line comment

'''
multy line comment
'''

my_variable = 10
AgeOfMan = 25
age_of_man = 12
n10umbers = 145

print(my_variable)

if my_variable == 10:
    pass
print(my_variable)


# print("Happy New Year")
# print("Happy New Year')
# print('Happy New Year')
# print('Happy New Year'
a = "Happy "
b = "New Year"
c = 2025
print(a+b)
#print(a+b+c)

num = 10 #initialization 
num = 12.3 # присвоєння
num == 12.3 # порівняння


#math and random 

import math
#sale
print(math.ceil(2.5)) # 3
print(math.floor(2.5)) # 2
print(math.pow(2,4)) # 16
print(math.sqrt(64)) # 8

number = 100
print(number)
import random

print(random.random())#0....1
print(random.random())#0....1
print(random.random())#0....1
print(random.random())#0....1
print(random.random())#0....1
print(random.randint(0,1))#0....1
print(random.randint(0,1))#0....1
print(random.randint(0,1))#0....1
print(random.randint(1,100))#0....1
print(random.randint(50,150))#0....1


#270 coins 1 kg
#200 coins 1 kg   500g > 
import math
price_for_one_kg = 270
price_sale = 200
gramm = int(input("Enter weight (gramm) : "))#700 g

kg = gramm /1000
print(f"Your weight of candies = {kg}")

if kg < 0.5:
    total = price_for_one_kg * kg
else:
    total = price_sale * kg

total = math.ceil(total)
print(f"Your total price : {total}")

day = int(input("Enter number of day [1-7] : "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Error number day")


day = int(input("Enter number of day [1-7] : "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Error number day")



print(" [+] - add \n [-] - minus\n [*] - multy\n [/] - divede \n")
choice = input("Enter your choice : ")
match choice:
    case '+':
        print("+")
    case '-':
        print("-")
    case  '*':
        print("avg")
    case '/':
        print("/")
    case _:
        print("Inncorect choice")

year = 2000
if year%400 == 0 or year%4 == 0 and year%100 != 0:
    pass

12321