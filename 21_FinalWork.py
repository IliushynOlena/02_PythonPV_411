import json
def addUser():
    id = int(input("Enter id : "))
    name = input("Enter name : ")
    return {'id':id,'name':name}


def createList(number):
    users = []
    for i in range(number):
        users.append(addUser())
    return users

def writeUsers(users):
    with open('users.json','w') as file:
        file.write(json.dumps(users))

def readUsers():
    with open('users.json') as file:
        return json.loads(file.read()) 

def printAllUsers(users):
    for i in range(len(users)):
        print(i+1, users[i])

while True:
    choice = int(input('''
            1. Fill database on the start
            2. Add new user
            3. Delete user
            4. Print all users
            5. Sort users
            0. Exit
            '''))
    if choice == 1:
        number = int(input("Enter count users to add : ")) #4
        users = createList(number)
        writeUsers(users)
    if choice == 0:
        print("Bye bye.....")
        break
    if choice == 2:
        users = readUsers()
        users.append(addUser())
        writeUsers(users)
    if choice == 4:
        users = readUsers()
        printAllUsers(users)
    if choice == 5:
        users = readUsers()
        users.sort(key= lambda x:x['id'])
        print(users)




