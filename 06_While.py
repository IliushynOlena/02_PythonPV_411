'''
day = 5
month = 2
year = 1900
print(f"{day}/{month}/{year}")
day+= 1

fullDays = 0

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    fullDays = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    fullDays = 30
elif month == 2:
    if year %400 == 0 or (year %4 == 0 and year %100 != 0):
        fullDays = 29
    else:
        fullDays = 28
# 32       31
if day > fullDays :
    month +=1 #2 --> 3
    day = 1

if month > 12:
    year += 1
    month = 1

print(f"{day}/{month}/{year}")
'''

print("*")
print("Hello world")
# 3! = 1 * 2 * 3
#5! = 1*2*3*4*5

#1 ...5 summa = 1+ 2 + 3 + 4 + 5 
#counter = 5
#start = 1
#end  = 15
# 1 - 15 1 2 3 4 5 6
# 15 - 1 15 16 17 


i = 0
while  i < 10:
    i+=1
    print(i , "Hello world")
# 1.....10
i = 1
while i <= 10:
    print(i, end=" ")
    i+=1
print()

# вивести всі числа від 10 до 0
i = int(input("Enter number : "))
while i >= 0:
    print(i, end=" ")
    #8 # 8
    i-=1
# i = i - 1
# i -= 1
#print(10- 1)

number = int(input("Enter number : "))
if number < 0 or number > 10:
    print("Error")
else:
    i = 1
    while i <= 10:
        print(f"{number} * {i} = {number * i}")
        i+=1
    else:
        print("="*30)
