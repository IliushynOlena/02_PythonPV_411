#5! = 5 * 4 * 3 * 2 * 1
# def factorial(x):
#     dob = 1
#     for i in range(1,x+1):
#         dob *= i
#     return dob
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello")

# f = factorial(5)
# print(f"Factorial = {f}")

# def modifyName(userName):
#     newName1 = userName.upper()
#     newName2 = userName.lower()
#     return newName1, newName2

# name = input("Enter name : ")
# print(modifyName(name))

# nameUpper, nameLower = modifyName(name)
# print(nameUpper)
# print(nameLower)


# def checkLog(userLog):
#     if userLog =='admin':
#         print("Hello")
#         return userLog.upper()
#         print("Hello")
#     elif userLog == 'user':
#         return userLog.lower()
#     else:
#         return "Wrong login!"

# print(checkLog("admin"))
# print(checkLog("user"))
# print(checkLog("student"))


# def average(*numbers):
#     summa= 0
#     count = 0
#     print(numbers)
#     for elem in numbers:
#         summa+= elem
#         count+=1

#     return summa/count

# print(average(1,2,3))
# print(average(1,2,3,4,5,6))
# numbers = [1,2,3,4,5,6,7,8,9]
# print(average(*numbers))

#Recursion....
# def sayHello():
#     print("Hello")
#     sayHello()

# sayHello()

#5! = 5 * 4 * 3 * 2 * 1
#for i in range(1,x+1): ---> 1 2 3 4 5
def factorial(x):# 5
    dob = 1 # 1
    for i in range(1,x+1):
        dob *= i# 1 * 1 = 1. 1 * 2 = 2. 2 * 3 = 6. 6 * 4 = 24. 24 * 5 = 120.
    return dob

f = factorial(5)
print(f"Factorial = {f}")

def factorial(x):#1
    if x == 0 or x == 1:
        return x
    # 5 * 4 * 3 * 2 * 1
    return x * factorial(x-1)

print( factorial(5))

#"madam"
def isPalindrom(word): #"madam"   "ada" "d"
    # if word == word[::-1]:
    #     return True
    # else:
    #     return False
    if len(word) == 0:
        return True
    else:
        if word[0] == word[-1]: # m == m  #a==a
            return isPalindrom(word[1:-1])#"ada" True and True and True
        else:
            return False

word = "madam"
print(isPalindrom(word))




