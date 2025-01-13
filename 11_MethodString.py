'''
line = "Lorem ipsum dolor "
print(line)
print(id(line))
line += "!!!"
print(line)
print(id(line))

print(line[0])
print(line[1])
print(line[2])
print(line[-1])
#print(line[50])

print(len(line))
#[start = 0 : end = -1 ]
#[start = 0 : end = len(line) ]
print(line[0:len(line)])
print(line[2:5])
print(line[2:-1])
print(line[-10:-1])
print(line[:8])
print(line[:-9])
print(line[5:])
print(line[10:])
print(line[0])
print(line[ : ])

#[start = 0 : end = len(line): step = 1 ]
#step >= 0 ---------------------------> 
print(line[0:21:1])
print(line[0:21:2])
print(line[::1])
print(line[::2])
#step < 0 <--------------------------
print(line[::-1])
print(line[5::2])
print(line[-1::-1])
print(line[-1::2])
print(line[:len(line):1])
print(line[:len(line):2])
print(line[:len(line):3])
print(line[:len(line):-1])
'''
#methods string 
numbers = "123458787"
letters = "skdnslkdhgskdgh"
line = "Lorem ipsum .dolor"
word = "Fruit Apple"
message = "BANANA"
letterDigit = "gdf2gd5f4g65df"

#перевіряє рядок на наявність тільки букв і цифр
print("=================== isalnum()====================")
print(f"\t{numbers} -------> {numbers.isalnum()}")
print(f"\t{letters} -------> {letters.isalnum()}")
print(f"\t{line} -------> {line.isalnum()}")
print(f"\t{word} -------> {word.isalnum()}")
print(f"\t{message} -------> {message.isalnum()}")
print(f"\t{letterDigit} -------> {letterDigit.isalnum()}")
print("=================================================")

#перевіряє рядок на наявність тільки букв
print("=================== isalpha()====================")
print(f"\t{numbers} -------> {numbers.isalpha()}")
print(f"\t{letters} -------> {letters.isalpha()}")
print(f"\t{line} -------> {line.isalpha()}")
print(f"\t{word} -------> {word.isalpha()}")
print(f"\t{message} -------> {message.isalpha()}")
print(f"\t{letterDigit} -------> {letterDigit.isalpha()}")
print("=================================================")

#перевіряє рядок на наявність тільки цифр
print("=================== isdigit()====================")
print(f"\t{numbers} -------> {numbers.isdigit()}")
print(f"\t{letters} -------> {letters.isdigit()}")
print(f"\t{line} -------> {line.isdigit()}")
print(f"\t{word} -------> {word.isdigit()}")
print(f"\t{message} -------> {message.isdigit()}")
print(f"\t{letterDigit} -------> {letterDigit.isdigit()}")
print("=================================================")

#перевіряє рядок на наявність тільки пробіли
print("=================== isspace()====================")
print(f"\t{numbers} -------> {numbers.isspace()}")
print(f"\t{letters} -------> {letters.isspace()}")
print(f"\t{line} -------> {line.isspace()}")
print(f"\t{word} -------> {word.isspace()}")
print(f"\t{message} -------> {message.isspace()}")
print(f"\t{letterDigit} -------> {letterDigit.isspace()}")
print("=================================================")

#перевіряє рядок на наявність тільки маленький літер (літери нижнього регістру)
#інші символи ,які не є алфавітними не враховуються

print("=================== islower()====================")
print(f"\t{numbers} -------> {numbers.islower()}")
print(f"\t{letters} -------> {letters.islower()}")
print(f"\t{line} -------> {line.islower()}")
print(f"\t{word} -------> {word.islower()}")
print(f"\t{message} -------> {message.islower()}")
print(f"\t{letterDigit} -------> {letterDigit.islower()}")
print("=================================================")

#перевіряє рядок на наявність тільки великих літер (літери верхнього регістру)
#інші символи ,які не є алфавітними не враховуються
print("=================== isupper()====================")
print(f"\t{numbers} -------> {numbers.isupper()}")
print(f"\t{letters} -------> {letters.isupper()}")
print(f"\t{line} -------> {line.isupper()}")
print(f"\t{word} -------> {word.isupper()}")
print(f"\t{message} -------> {message.isupper()}")
print(f"\t{letterDigit} -------> {letterDigit.isupper()}")
print("=================================================")

#перевіряє рядок на наявність великої букви на початку кожного слова(літери верхнього регістру)
print("=================== istitle()====================")
print(f"\t{numbers} -------> {numbers.istitle()}")
print(f"\t{letters} -------> {letters.istitle()}")
print(f"\t{line} -------> {line.istitle()}")
print(f"\t{word} -------> {word.istitle()}")
print(f"\t{message} -------> {message.istitle()}")
print(f"\t{letterDigit} -------> {letterDigit.istitle()}")
print("=================================================")


#перетворює всі літери до нижнього регістру
print("=================== lower()====================")
print(f"\t{numbers} -------> {numbers.lower()}")
print(f"\t{letters} -------> {letters.lower()}")
print(f"\t{line} -------> {line.lower()}")
print(f"\t{word} -------> {word.lower()}")
print(f"\t{message} -------> {message.lower()}")
print(f"\t{letterDigit} -------> {letterDigit.lower()}")
print("=================================================")


#перетворює всі літери до верхнього регістру
print("=================== upper()====================")
print(f"\t{numbers} -------> {numbers.upper()}")
print(f"\t{letters} -------> {letters.upper()}")
print(f"\t{line} -------> {line.upper()}")
print(f"\t{word} -------> {word.upper()}")
print(f"\t{message} -------> {message.upper()}")
print(f"\t{letterDigit} -------> {letterDigit.upper()}")
print("=================================================")

#перетворює першу букву створеної змінної типу стрінг до верхнього регістру
print("=================== capitalize()====================")
print(f"\t{numbers} -------> {numbers.capitalize()}")
print(f"\t{letters} -------> {letters.capitalize()}")
print(f"\t{line} -------> {line.capitalize()}")
print(f"\t{word} -------> {word.capitalize()}")
print(f"\t{message} -------> {message.capitalize()}")
print(f"\t{letterDigit} -------> {letterDigit.capitalize()}")
print("=================================================")


#перетворює першу букву кожного слова до верхнього регістру
print("=================== title()====================")
print(f"\t{numbers} -------> {numbers.title()}")
print(f"\t{letters} -------> {letters.title()}")
print(f"\t{line} -------> {line.title()}")
print(f"\t{word} -------> {word.title()}")
print(f"\t{message} -------> {message.title()}")
print(f"\t{letterDigit} -------> {letterDigit.title()}")
print("=================================================")

#змінює регістр букв на протилежний
print("=================== swapcase()====================")
print(f"\t{numbers} -------> {numbers.swapcase()}")
print(f"\t{letters} -------> {letters.swapcase()}")
print(f"\t{line} -------> {line.swapcase()}")
print(f"\t{word} -------> {word.swapcase()}")
print(f"\t{message} -------> {message.swapcase()}")
print(f"\t{letterDigit} -------> {letterDigit.swapcase()}")
print("=================================================")


#методи пошуку елементів у рядку   ------>
#якщо елементу не знайдено - вернеться -1
line = "Lorem ipsum .dolor lorem ipsum dolor lorem ipsum dolorLorem ipsum .dolor lorem ipsum dolor lorem ipsum dolor!"
print(f"Find str\"dolor\" in index {line.find("dolor")} ")
print(f"Find str\"dolor\" in index {line.find("dolor",14)} ")
print(f"Find str\"dolor\" in index {line.find("dolor",32)} ")
print(f"Find str\"dolor\" in index {line.find("dolor",50)} ")
print(f"Find str\"dolor\" in index {line.find("dolor",68)} ")
print(f"Find str\"dolor\" in index {line.find("dolor",86)} ")
print(f"Find str\"dolor\" in index {line.find("dolor",104)} ")

index = -1
while True:
    index= line.find("dolor", index+1)
    if index == -1:
        break
    print(f"Find str\"dolor\" in index {index} ")

#методи пошуку елементів у рядку   <----------------------
print(f"Find str\"dolor\" in index {line.rfind("dolor")} ")

#методи пошуку елементів у рядку   ------> 
#якщо елементу не знайдено - вернеться помилка, яка зламає програму
print(f"Find str\"dolor\" in index {line.index("dolor")} ")
print(f"Find str\"dolor\" in index {line.rindex("dolor")} ")

# повертає точну кількість елементів вказаних в дужках 
print(f"\t{line} -------> {line.count("dolor")}")
print(f"\t-------> {line.replace("dolor", "red")}")
print(line)

print(line.startswith("L"))
print(line.startswith("l"))
print(line.startswith("L",8))
print(line.endswith("!"))
print(line.endswith("a", 2,6))
print(line.endswith(" ", 2,6))
print(line.endswith("i", 2,6))

message = "Python 2025"
print(message)
print(message.center(50))
print(message.center(50,'*'))
print(message.center(5))
print(message.ljust(50))
print(message.ljust(50,'#'))
print(message.ljust(5))
print(message.rjust(50))
print(message.rjust(50,'#'))
print(message.rjust(5))

message = "                    Python 2025!                  "       
print(message.lstrip())              
print(message.rstrip())              
print(message.strip())   
message = "@                    Python 2025!                  @"       
print(message.lstrip('@'))              
print(message.rstrip('@'))              
print(message.strip('@'))  
number = "+123"
print(number.zfill(6))

#"dkjhgkldsdfh6df5h6+df5h+df6h5df+6h L joegjoejgpw 65 465 4"