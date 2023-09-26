import random
from typing import Coroutine

def welcome():
    print("!!Welcome to Tic Tac Toe Game!!")
    print("Rules for playing the game ----")
    print("Enter the number of the box in which you want your move to be played as shown below --")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")


def isWinner(board):
    # HorizontalCheck
    if (board["1"] == "X" and board["2"] == "X" and board["3"] == "X") or (board["1"] == "O" and board["2"] == "O" and board["3"] == "O"):
        return True
    if (board["4"] == "X" and board["5"] == "X" and board["6"] == "X") or (board["4"] == "O" and board["5"] == "O" and board["6"] == "O"):
        return True
    if (board["7"] == "X" and board["8"] == "X" and board["9"] == "X") or (board["7"] == "O" and board["8"] == "O" and board["9"] == "O"):
        return True
    
    # VerticalCheck
    if (board["1"] == "X" and board["4"] == "X" and board["7"] == "X") or (board["1"] == "O" and board["4"] == "O" and board["7"] == "O"):
        return True
    if (board["2"] == "X" and board["5"] == "X" and board["8"] == "X") or (board["2"] == "O" and board["5"] == "O" and board["8"] == "O"):
        return True
    if (board["3"] == "X" and board["6"] == "X" and board["9"] == "X") or (board["3"] == "O" and board["6"] == "O" and board["9"] == "O"):
        return True

    # CrossCheck
    if (board["1"] == "X" and board["5"] == "X" and board["9"] == "X") or (board["1"] == "O" and board["5"] == "O" and board["9"] == "O"):
        return True
    if (board["3"] == "X" and board["5"] == "X" and board["7"] == "X") or (board["3"] == "O" and board["5"] == "O" and board["7"] == "O"):
        return True


def compMove(board):
    computerposition = random.randint(1,9)
    while True:
        if computerposition in board and board[computerposition] == " ":
            board[computerposition] = "O"
        else:
            continue




def main():
    while True: 
        board = {"1" : " ",
        "2" : " ",
        "3" : " ",
        "4" : " ",
        "5" : " ",
        "6" : " ",
        "7" : " ",
        "8" : " ",
        "9" : " "}
        totalmoves = 0
        print(" {} | {} | {} ".format(board["1"],board["2"],board["3"]))
        print("---|---|---")
        print(" {} | {} | {} ".format(board["4"],board["5"],board["6"]))
        print("---|---|---")
        print(" {} | {} | {} ".format(board["7"],board["8"],board["9"]))
        playerposition = input("Enter the position : ")
        while totalmoves != 9 and isWinner(board) == True:
            if (playerposition in board) and (playerposition in board[playerposition] == " "):
                board[playerposition] = "X"
                break
        totalmoves += 1
    


welcome()
main()

























