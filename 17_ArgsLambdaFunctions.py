
print("Hello")
print("Hello","red")
print("Hello","red",36)
print("Hello","red",361,45)
print("Hello","red",361,45,1,4)
print("Hello","red",361,45.25)

def sumAllNumbers(*args):
    print(args)
    #args[0]=1000 - error not allowed
    #get all elements
    for elem in args:
        print(elem,end=" ")
    print()
    #get element by index
    print(f"Element in index[4] = {args[4]}")
    print(f"Count Element [5] = {args.count(5)}")
    print(f"Index of element 5 = [{args.index(5)}]")
    print(f"Length  = {len(args)}")
    new_list = list(args)
    print(new_list)
    new_list[0] =1000
    print(new_list)
    return sum(args)

#(5, 5, 8, 9)  - cortege - don*t change - not allow add new element, delete element, change

summa_el= sumAllNumbers(5,5,8,9,78,9,6,36,25,41,5,5)
print(f"Summa elements = {summa_el}")


def showInfoStudent(name, age, *marks):
    print(f"Name : {name}")
    print(f"Age : {age}")
    print(f"Marks : {marks}")
    

showInfoStudent("Olga", 17,12,11,12,10,12,9,10)

#Lambda function
def sum(a,b):
    return a+b

def show(color):
    print(color)

print(sum(14,52))
show("white")

lambda_summa = lambda a,b:a+b
lambda_show = lambda color:print(color)
print(lambda_summa(3,3))
lambda_show("green")

#1
numbers = [1,5,7,89,6,58,14,25,23,11,12,14,17]

def doubleList(list):
    temp=[]
    for elem in list:
        temp.append(elem*2)
    return temp

print(numbers)
new_numbers = doubleList(numbers)
print(new_numbers)

#2.1
# line = input("Enter numbers : ").split(' ')
# line = [ int(el)  for el in line]
# print(line)

#2.2
# line = list( map(int,input("Enter numbers : ").split(' ')) )
# print(line)
#map - change all elements 
# def double(x):
#     return x*2

# numbers = [1,5,7,89,6,58,14,25,23,11,12,14,17]
# new_numbers = list(map(double,numbers))
# print(numbers)
# print(new_numbers)
#lambda function


numbers = [1,5,7,89,6,58,14,25,23,11,12,14,17]
new_numbers = list(map(lambda x:x*2,numbers))
print(numbers)
print(new_numbers)

numbers = [1,5,7,89,6,58,14,25,23,11,12,14,17]
new_numbers = list(map(lambda x:x*x,numbers))
print(numbers)
print(new_numbers)

#Filter
numbers = [1,5,7,89,6,58,14,25,23,11,12,14,17]
filtered_list = list(filter( lambda x:x%2==0,numbers))
print(numbers)
print(filtered_list)

numbers = [1,5,7,89,6,58,14,25,23,11,12,14,17]
filtered_list = list(filter( lambda x:x> 0 and x <= 10, numbers))
print(numbers)
print(filtered_list)

colors = ["red", "green","blue","yellow","pink","grey"]

# def checkColor(color):
#     if len(color)>= 4:
#         return True
#     else:
#         return False

# def checkColor(color):
#     return len(color)>= 4   
    
# new_colors = list(filter(checkColor, colors))
# print(colors)
# print(new_colors)

new_colors = list(filter(lambda color: len(color)>= 4   , colors))
print(colors)
print(new_colors)

new_colors = list(filter(lambda color: color[0]=='b'   , colors))
print(colors)
print(new_colors)












