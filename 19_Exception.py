# # #4. Напишіть функцію, яка підраховує суму цифр числа. 
# # # Наприклад: число 1357, сума 1 + 3 + 5 + 7 = 16.

# #1236654564564654
# #1357%10 = 7
# #1357//100 = 135%10 = 5
# #1357//1000 = 13%10 = 3
# #1357//1000 = 1

# def sumRecursion(number):

#     #1234%10 = 4
#     #1234//10 = 123

#     #123%10 = 3
#     #123//10 = 12

#     #12%10 = 2
#     #12//10 = 1

#     #1%10 = 1
#     #1//10 = 0
#     # 4 + 3 + 2 + 1 + 0
#     if number == 0:
#         return 0
#     return number%10 + sumRecursion(number//10)

# print(sumRecursion(1234))
# print(sumRecursion(123456))
# print(sumRecursion(1234789))

# number_1 = None
# number_2 = None
# while number_1 == None or number_2== None:
#     try:
#         number_1 = int(input("Enter number : ")) 
#         number_2 = int(input("Enter number : ")) 
#         print(f"Number = {number_1/number_2 }")
    
#     except ValueError:
#         print("Error type ")
#     except ZeroDivisionError:
#         print("division by zero. You need study math!!!")
#     except Exception:
#         print("Some unknown Error")


# try:
#     age = int(input("Enter age : ")) 
#     if age < 0:
#         raise Exception("Age error. Age < 0")
#     if age > 200:
#         raise Exception("Age error. Age > 200")
#     print(f"Age = {age }")
# except ValueError:
#     print("Error type ")
# except Exception as exception:
#     print(exception) 
#     print(type(exception).__name__) 
# else:
#     print("It is Ok")
# finally:
#     print("Finally work always")


colors = ['red','green','blue','pink','black',"white"]
try:
    index = int(input("Enter position of color : "))
    print(colors[index])
except ValueError:
    print("Value Error")
except IndexError:
    print("list index out of range")