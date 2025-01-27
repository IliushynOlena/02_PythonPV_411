
#numbers = [1,7,8,9,6,5]

# # # #start = 0; start <= end; start +=1
# for num in numbers:
#   #num = 0
#     print(num)


# print(numbers)
# #len(numbers) = 6
# for index in range(len(numbers)):#0 1 2 3 4 5 
#     numbers[index] = 0
#     print(f"[{index}] - value { numbers[index]}")

def showMessage():
    a = 5
    print(a)
    print(b)
    print("Hello")

b = 15
print(b)
# print(a)
showMessage()
showMessage()
showMessage()
showMessage()

def showGreetingToUser(name):
    print(f"Hello, {name}")


showGreetingToUser("Mukola")
showGreetingToUser("Ivan")
showGreetingToUser("Mark")
showGreetingToUser("Andriy")
# name = input("Enter name " )
# showGreetingToUser(name)

def summa(a,b):
    print(a + b)

summa(5,8)
summa(5,25)

def sum(a,b):
    res = a + b 
    return res
    

res = sum(5,5)
print(f"Res = {res}")
print(sum(78,12))

def sub(a,b):
    res = a - b 
    return res

def multy(a,b):
    res = a * b 
    return res

def div(a,b):
    if b == 0:
        return #break == return
    return a / b 


def calculator(a,b,op):
    if op == "+":
        return sum(a,b)
    if op == "-":
        return sub(a,b)
    if op == "*":
        return multy(a,b)
    if op == "/":
        return div(a,b)


result = calculator(5,5,'+')
print(f"Result = {result}")
result = calculator(5,5,'-')
print(f"Result = {result}")
result = calculator(5,5,'*')
print(f"Result = {result}")
result = calculator(5,5,'/')
print(f"Result = {result}")

def getOperation(user_input):
    if user_input.find('+') != -1:
        return '+'
    if user_input.find('-') != -1:
        return '-'
    if user_input.find('*') != -1:
        return '*'
    if user_input.find('/') != -1:
        return '/'


# user_input = input("Enter example (2+2)")
# op = getOperation(user_input)
# #    "2+2"
# a = float( user_input.split(op)[0])
# b = float(user_input.split(op)[1])
# result = calculator(a,b,op)
# print(f"Result = {result}")
import random
#(count, min, max) - required arguments 
def fillList(count, min, max):
    # my_list = [random.randint(min, max+1)      for i in range(count)]
    # print(my_list)
    # return my_list
    return [random.randint(min, max+1)      for i in range(count)]
#   (count=10, min=1, max=50) - default arguments
def fillList(count, min=1, max=50):
    return [random.randint(min, max+1)      for i in range(count)]


numbers = []
numbers = fillList(10, 1, 50)
print(numbers)

numbers = fillList()
print(numbers)

numbers = fillList(20)
print(numbers)

numbers = fillList(15,10)
print(numbers)

numbers = fillList(5,100,120)
print(numbers)

