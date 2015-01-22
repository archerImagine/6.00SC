import math

def yourAmount(money):
    int(input("enter amount to withdraw: "))


def returnCard():
    print("Returning card now, thanks :D ")
    global carryon
    carryon = False

def showmoney(money):
    money = int(money * 100)
    money = int(money / 100)
    maxwid = int((money // 10) * 10)
    print("Currunt money, ",money)
    print("Maximum withdrawal, ",maxwid)
    return mainmenu

def subtract(money):
    while amount % 10 != 0:
        amount = int(input("Enter amount to take out (multiple of 10): "))
        if amount % 10 != 0:
            print("Error, invalid amount. Please try again or press 0 to return")

        if money > amount:
            money = money - amount
            print("$",amount,"withdrawn. Please collect your money")
        else:
            print("Sorry, insufficient funds available")
        return money

def withdraw(money):
    menu = "How much cash would you like to withdraw.\n\
1 - $10\n\
2 - $20\n\
3 - $40\n\
4 - $60\n\
5 - $80\n\
6 - $100\n\
7 - Other Amount\n\
8 - Return to Main Menu\n\
9 - Return Card\n"

    option = 0

    while option < 1 or option > 9:
        option = int(input(menu))
        if option == 1:
            money = (subtract,10)
            return money
        elif option == 2:
            money = (subtract,20)
            return money
        elif option == 3:
            money = (subtract,40)
            return money
        elif option == 4:
            money = (subtract,60)
            return money
        elif option == 5:
            money = (subtract,80)
            return money
        elif option == 6:
            money = (subtract,100)
            return money
        elif option == 7:
            money = (subtract,yourAmount(money))
            return money
        elif option == 8:
            break
        elif option == 9:
            returnCard()
            return money

def deposit(money):
    menu ="""
If you want to deposit, how much would you like to deposit? type amount in
Enter 0 to return to main menu.
Enter 9 to return card\n
"""

    choice = int(input(menu))


    if choice == 9:
              returnCard()
    else:
        money = money + choice


    return money

def mainmenu(money):
    menu = """
Welcome\n\
1 - Display money
2 - Withdraw Funds
3 - Deposit Funds
9 - Return Card
Enter an option:
"""

    wrong = True

    while returnCard:
        choice = int(input(menu))
        if choice == 1:
            wrong = False
            money = showmoney(money)
        elif choice == 2:
            wrong = False
            money = withdraw(money)
        elif choice == 3:
            wrong = False
            money = deposit(money)
        elif choice == 9:
            returnCard()
        else:
            print("Invalid choice, please try again.")

        return money



money = 67.14
carryon = True
while carryon:
    money = mainmenu(money)