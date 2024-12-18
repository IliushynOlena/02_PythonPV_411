import random
print("\t\tWelcome to the Game!!!!")
print("\t\tRock Scissors Paper!")

user = 0
bot = 0



while True:
    user_score = 0
    bot_score = 0
    for round in range(3):#0...1...2.
        print(f"------------------------------ Round {round + 1}--------------------------------")
        while True:
            user = input("\t [r] - rock\n\t [s] - scissors\n\t [p] - paper\n\tEnter your choose : ")
            user = user.lower()
            if user == 'r' or user == 's' or user == 'p':
                break
            else:
                print("Error. Incorrect choice .....")

        bot = random.choice("rsp")
        print("\t Bot \t User")
        print(f"\t [{bot}]\t [{user}]")

        if (user == 'r'and bot == 's') or (user == 's' and bot =='p') or (user == 'p' and bot =='r'):
            user_score +=1
        elif (bot == 'r'and user == 's') or (bot == 's' and user =='p') or (bot == 'p' and user =='r'):
            bot_score+=1

    if user_score> bot_score:
        print("\n\t======================== Congratulation ! User is winner !!!====================== ")
    elif bot_score > user_score:
        print("\n\t======================== Sorry ! Bot is winner !!! You lose ====================== ")
    else:
        print("========================= Draw ===========================")

    while True:
        user = input("Play again ? [y] - Yes. [n] - No. ---> ")
        user = user.lower()
        if user == 'y' or user =='n':
            break
        else:
            print("Error . Enter true choose --> ")

    if user =='n':
        print("Have a nice day! Goodbye!!! ")
        break




