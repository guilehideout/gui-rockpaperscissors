from random import choice

choices = ["Rock", "Paper", "Scissors"]

def ComputerChoice():
    return choice(choices)

def WhoWon(user_choice, comp_choice):
    if ((user_choice == 'Rock' and comp_choice == "Scissors")
        or (user_choice == 'Paper' and comp_choice == "Rock")
        or (user_choice == 'Scissors' and comp_choice == "Paper")):
        return "You won!"
    elif ((user_choice == 'Rock' and comp_choice == "Paper")
        or (user_choice == 'Paper' and comp_choice == "Scissors")
        or (user_choice == 'Scissors' and comp_choice == "Rock")):
        return "Computer wins!"
    else:
        return "Same choices!"