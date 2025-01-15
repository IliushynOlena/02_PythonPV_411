str_1 = "123"
str_2 = "234"
str_3 = "Lorem 21 ipsum dolor"

import re
# . ^ $ * + ? [] {} () \ |
print("======================== re.search(pattern,str)=====================")
print(f"\t{str_1} ---> \t {re.search('1',str_1)}")
print(f"\t{str_2} ---> \t {re.search('1',str_2)}")
print(f"\t{str_3} ---> \t {re.search('1',str_3)}")
print("--------------------------------------------------")
print(f"\t{str_1} ---> \t {re.search('12',str_1)}")
print(f"\t{str_2} ---> \t {re.search('12',str_2)}")
print(f"\t{str_3} ---> \t {re.search('12',str_3)}")
print("--------------------------------------------------")
print(f"\t{str_1} ---> \t {re.search('123',str_1)}")
print(f"\t{str_2} ---> \t {re.search('123',str_2)}")
print(f"\t{str_3} ---> \t {re.search('123',str_3)}")
print("--------------------------------------------------")
print(f"\t{str_1} ---> \t {re.search('[123]',str_1)}")
print(f"\t{str_2} ---> \t {re.search('[123]',str_2)}")
print(f"\t{str_3} ---> \t {re.search('[123]',str_3)}")

print("--------------------------------------------------")
print(f"\t{str_1} ---> \t {re.search('[0-9]',str_1)}")
print(f"\t{str_2} ---> \t {re.search('[0-9]',str_2)}")
print(f"\t{str_3} ---> \t {re.search('[0-9]',str_3)}")

print("--------------------------------------------------")
print(f"\t{str_1} ---> \t {re.search('[a-z]',str_1)}")
print(f"\t{str_2} ---> \t {re.search('[a-z]',str_2)}")
print(f"\t{str_3} ---> \t {re.search('[a-z]',str_3)}")
#True = 1. False = 0
print(bool("")) #False
print(bool(0))  #False
print(bool(0.00))#False
print(bool(None))#False
print(bool("It step"))#True
print(bool(5))#True
print(bool(-10))#True

# symbol = input("Enter one letter : ")
# match = re.search('[a-z]', symbol)

# #match = Match.... None
# if match:
#     print("This is letter ...")
# else:
#     print("This is not letter")


# symbol = input("Enter one letter : ")
# match = re.search('[a-zA-Z]', symbol)

# #match = Match.... None
# if match:
#     print("This is letter ...")
# else:
#     print("This is not letter")
print("--------------------------------------------------")
print(f"\t{str_1} ---> \t {re.search('[a-zA-Z]{5}',str_1)}")
print(f"\t{str_2} ---> \t {re.search('[a-zA-Z]{5}',str_2)}")
print(f"\t{str_3} ---> \t {re.search('[a-zA-Z]{5}',str_3)}")

print("--------------------------------------------------")
print(f"\t{str_1} ---> \t {re.search('[a-zA-Z]{6}',str_1)}")
print(f"\t{str_2} ---> \t {re.search('[a-zA-Z]{6}',str_2)}")
print(f"\t{str_3} ---> \t {re.search('[a-zA-Z]{6}',str_3)}")


print("--------------------------------------------------")
print(f"\t{str_1} ---> \t {re.search('[a-zA-Z]+',str_1)}")
print(f"\t{str_2} ---> \t {re.search('[a-zA-Z]+',str_2)}")
print(f"\t{str_3} ---> \t {re.search('[a-zA-Z]+',str_3)}")

print("--------------------------------------------------")
print(f"\t{str_3} ---> \t {re.search('Lorem',str_3)}")
print(f"\t{str_3} ---> \t {re.search('Lorem',str_3).group()}")
print(f"\t{str_3} ---> \t {re.search('Lorem',str_3).group(0)}")

print("--------------------------------------------------")
print(f"\t{str_3} ---> \t {re.search('\w+',str_3)}")
print(f"\t{str_3} ---> \t {re.findall('\w+',str_3)}")
print(f"\t{str_3} ---> \t {re.findall('\w+',str_3)[0]}")
print(f"\t{str_3} ---> \t {re.findall('\w+',str_3)[1]}")
print(f"\t{str_3} ---> \t {re.findall('\w+',str_3)[2]}")
print(f"\t{str_3} ---> \t {re.findall('\w+',str_3)[3]}")
match = re.findall('\w+',str_3)
for elem in match:
    print(elem)

print(f"\t{str_3} ---> \t {re.sub('\w+',"white",str_3)}")
print(f"\t{str_3} ---> \t {re.sub('\w{3}',"white",str_3)}")

    # \d - Визначає символи цифр. 
    # \D - Визначає любий символ, який не є цифрою. 
    # \w - Визначає любий символ цифри, букви або нижнє підкреслення. 
    # \W - Визначає любий символ, який не є цифрою, буквою або нижнім підкресленням.. 
    # \s - Визначає любий недрукований символ, включаючи пробіл. (таб і перехід на новий рядок)
    # \S - Визначає любий символ, крім символів табуляции, нового рядка и повернення каретки.
    # .  - Визначає любий символ крім символа нового рядка.  
    # \. - Визначає символ крапки.

    #   КВАНТИФИКАТОРЫ
    # ^ - з початку рядка. 
    # $ - з кінця рядка. 
    # * - нуль і більше входжень підшаблону в сторці.  
    # + - одне і більше  входжень підшаблону в сторці.  
    # ? - нуль чи одне  входження підшаблону в сторці.    

phone_number = input("Enter phone number : ")
pattern = "\+380\d{2}\-\d{3}\-\d{2}\-\d{2}"

match = re.search(pattern, phone_number).group(0)
print(match)
