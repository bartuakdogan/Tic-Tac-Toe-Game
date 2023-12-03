import tkinter as tk
from tkinter import simpledialog
import random


def get_player_name():
    name = simpledialog.askstring("Player Name", "Enter your name: ")
    return name if name else "Player"

def check_winner(board):
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

# Function to check for a tie
def check_tie(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False 
    return True  


def player_move(row, col):
    if board[row][col] == "":
        board[row][col] = "X"
        update_board()
        if check_winner(board):
            game_completed("Player")
        elif check_tie(board):
            game_completed("Tie")
        else:
            computer_move()


def computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"
        update_board()
        if check_winner(board):
            game_completed("Computer")
        elif check_tie(board):
            game_completed("Tie")


def update_board():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[i][j])


def game_completed(winner):
    if winner == "Tie":
        result = "It's a Tie!"
    else:
        result = f"{winner} wins!"
    
    simpledialog.messagebox.showinfo("Game Over", result)

    
    for i in range(3):
        for j in range(3):
            board[i][j] = ""
            buttons[i][j].config(text="")


def start_game():
    global board, buttons

    player_name = get_player_name()

    
    board = [["" for _ in range(3)] for _ in range(3)]

    
    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    
    buttons = [[tk.Button(root, text="", font=("Helvetica", 16), width=5, height=2, command=lambda row=i, col=j: player_move(row, col)) for j in range(3)] for i in range(3)]

    
    for i in range(3):
        for j in range(3):
            buttons[i][j].grid(row=i, column=j)

    
    root.mainloop()


if __name__ == "__main__":
    start_game()
