from colorama import Style, Back, Fore, init
from tqdm import tqdm
import time
import random
import tools


balance = 0

# initialize colorama
init()

def info():
    tools.clear()
    print(Fore.GREEN + "Welcome to PyLottery! To start, type 2 into the input prompt,")
    print("from there your ticket will generate, then after that your ticket will be compared")
    print("to the winning ticket. If you win, a cash price will be added to your balance,")
    print("which you can check in the menu by typing 3. If you lose, you can start over")
    print("again with a new ticket number.", '\n')

    print(Fore.YELLOW + "Press enter to return.", '\n')
    s = input(Fore.RESET + "||: ")

    if not s:
        main()
    else:
        main()
    

def get_balance():
    tools.clear()
    print(Fore.BLUE + "Balance:" + Fore.RESET + Back.RESET + " $" + str(balance))

    print(Fore.YELLOW + "Press enter to return.", '\n')
    s = input(Fore.RESET + "||: ")

    if not s:
        main()
    else:
        main()

def display_winning():
    ticket = []
    temp_ticket = []
    global balance

    tools.clear()
    ticket.clear()
    temp_ticket.clear()



    print(Fore.GREEN + "Generating Ticket...\n")

    
    for i in tqdm(range(int(7)), ncols = 60):
        time.sleep(0.06)
    
    for i in range(7):
        num = random.randint(0, 9)
        ticket.append(num)


    print('\n\n')
    print(Fore.WHITE + Back.LIGHTYELLOW_EX + "TICKET TIME".center(55))
    print(Back.RESET)

    odds = random.randint(0, 9)
    luck = random.randint(0, 9)
    if (odds == luck):
        temp_ticket = ticket
    else:
        for i in range(7):
            j = random.randint(0, 9)
            temp_ticket.append(j)
    
    time.sleep(0.2)

    print(Fore.RESET + "Your ticket:     " + Fore.BLUE + str(ticket))

    time.sleep(0.7)

    if (temp_ticket == ticket):
        wins = random.randint(0, 9999999)
        print(Fore.RESET + "Winning ticket: " + Fore.BLUE, temp_ticket, '\n')
        print(Fore.GREEN + "Congraduations!! You won: " + Fore.WHITE + Back.BLUE + "$" + str(wins) + "!")
        balance += wins
    else:
        print(Fore.RESET + "Winning ticket: " + Fore.YELLOW, temp_ticket, '\n')
        print(Fore.RED + "Sorry, tickets do not match :(")
    
    print(Fore.YELLOW + Back.RESET + "Press enter to play again, or 0 to return.", '\n')
    s = input(Fore.RESET + "||: ")

    if not s:
        display_winning()
    elif s == "0":
        main()
    else:
        display_winning()



def main():
    tools.clear()
    print(Fore.GREEN + """
  _____         _           _   _                  
 |  __ \       | |         | | | |                 
 | |__) |   _  | |     ___ | |_| |_ ___ _ __ _   _ 
 |  ___/ | | | | |    / _ \| __| __/ _ \ '__| | | |
 | |   | |_| | | |___| (_) | |_| ||  __/ |  | |_| |
 |_|    \__, | |______\___/ \__|\__\___|_|   \__, |
         __/ |                                __/ |
        |___/                                |___/ 
""")
    print("Welcome to Py Lottery! Please make a selection. \n")

    print(Fore.RESET + Back.YELLOW + "[1]:" + Back.RESET +  " Info")
    print(Fore.RESET + Back.RED + "[2]:" + Back.RESET +  " Check Winning")
    print(Fore.BLACK + Back.BLUE + "[3]:" + Fore.RESET + Back.RESET +  " Check Balance")
    print(Fore.BLACK + Back.WHITE + "[4]:" + Fore.RESET + Back.RESET +  " Exit")


    selection = input("||: ")

    if (selection == "1"):
        info()
    elif (selection == "2"):
        display_winning()
    elif (selection == "3"):
        get_balance()
    elif (selection == "4"):
        print(Fore.BLUE + "Thanks for playing!")
        exit(1)
    else:
        main()





if __name__ == '__main__':
    main()