import random

def welcome():
    print()
    print("===========================================")
    print("       🎮 Number Guessing Game             ")
    print("===========================================")
    print()
    print("📋Instructions:")
    print("- The computer will choose a number.")
    print("- You must guess it in the fewest attempts.")
    print("- Your score will be saved to a file.")
    print("Let's begin!\n")

def replay():
    print()
    print("1 Replay")
    print("0 Exit")

    while True:
        replay_choice = input("Enter your choice: ")

        if replay_choice == '1':
            return True
        elif replay_choice == '0':
            print("~ Exit ~")
            return False
        else:
            print("Invalid Input")
            print()

def levels():
    print("🎚️ Levels:- ")
    print("1 Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard   (1 to 200)")

    while True:
        level_choice = input("Enter level (1, 2 or 3): ")

        if level_choice == "1":
            return 50
        elif level_choice == "2":
            return 100
        elif level_choice == "3":
            return 200
        else:
            print("~ Invalid Input ~")
            print()

def game(Level):
    op_num = random.randint(1,Level) #Random Number
    attempts = 0

    print()
    print("~ Let's Start ~")

    while True:
        try:
            user_num = int(input("Enter: ")) # Number chosen by a user

            attempts += 1

            if user_num < op_num:
                print("~ Low! ~")
            elif user_num > op_num:
                print("~ High! ~")
            else:
                print(f"~ 🎉 Correct!~")
                print(f"You guessed it in {attempts}")
                break

        except ValueError:
            print("Invalid Input")

def main():
    welcome()          #intro
    Level = levels()       #choice of level

    game(Level)

    while True:
        if replay(): 
            print()     #replay choice
            Level = levels()
            game(Level)
        else:
            break
        
main()