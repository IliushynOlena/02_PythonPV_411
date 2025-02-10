#відкрити файл
#прочитати файл
#записти файл
#закрити файл

#абсолютний шлях
url = r'C:\Users\helen\Desktop\NewGroups\02_PythonPV_411\20_File\mytxt.txt'
#відносний шлях (відносно корінної папки проекту)
file = open('./20_File/mytxt.txt')

#read all text in the file 
#print(file.read())

#read one line
# print(file.readline().strip())
# print(file.readline().strip())
# print(file.readline().strip())

#read all text ---> return list
#print(file.readlines())

#read text size = 15
#print(file.read(15))

#file.close()


#open
with open(url) as file:
    line = file.read()
    print(line)
    print(type(line))
    #file.close()

# #перезепис інформації
# url_2 = "./20_File/write_file.txt"
# with open(url_2,'w') as file:
#     file.write("Lorem ipsum dolor sit amet")

lines = [
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
'Donec ac nunc convallis, sollicitudin tellus accumsan, dignissim augue.',
'In eleifend nisi eget ligula viverra, non posuere erat pharetra.',
'Nulla vitae justo finibus, pretium nisl et, laoreet dui.'
]
#дозапис інформації
url_2 = "./20_File/write_file.txt"
# counter = 1
# with open(url_2,'w') as file:
#     for line in lines :
#         file.write(f"{counter}.{line}\n")
#         counter+=1

# url_3 = "./20_File/write_file_new.txt"
# with open(url_3,'w') as file:
#     file.writelines(lines)

# def readFile(url_read):
#     with open(url_read) as file:
#         return file.read()
    
# def appFile(url_write, info):
#     with open(url_write,'w') as file:
#         file.write(info)

url_2 = "./20_File/write_file.txt"
url_3 = "./20_File/write_file_new.txt"
# text = readFile(url_2)
# appFile(url_3,text)

lines = []
with open(url_2) as file:
    lines = file.readlines()

with open(url_3,'a') as file:
    for line in lines[::-1]:
        #print(line.strip())
        file.write(line.strip()+ '\n')
        print(file.readable())
        print(file.writable())
