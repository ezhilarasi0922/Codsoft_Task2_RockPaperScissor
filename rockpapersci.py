import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score

    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result_label.config(text=f"Computer chose {computer_choice}. It's a tie!")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result_label.config(text=f"Computer chose {computer_choice}. You win!")
        user_score += 1
    else:
        result_label.config(text=f"Computer chose {computer_choice}. You lose!")
        computer_score += 1

    update_scores()

# Function to update scores and check for winner
def update_scores():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

    if user_score == 5:
        winner_label.config(text="Congratulations! You win the game!", fg="green")
        disable_buttons()
    elif computer_score == 5:
        winner_label.config(text="Computer wins the game!", fg="red")
        disable_buttons()

# Function to disable buttons after game completion
def disable_buttons():
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)

# Initialize tkinter
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(background="#B4D4FF")

user_score = 0
computer_score = 0

# Function to get user's choice
def get_user_choice(choice):
    determine_winner(choice)

# Create GUI elements using grid layout
rock_button = tk.Button(root, text="Rock", padx=20, pady=10,font=("Helvetica",11,"bold"), bg="#176B87",fg="white", command=lambda: get_user_choice('Rock'))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", padx=20, pady=10,font=("Helvetica",11,"bold"), bg="#176B87",fg="white", command=lambda: get_user_choice('Paper'))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors", padx=20, pady=10,font=("Helvetica",11,"bold"), bg="#176B87",fg="white", command=lambda: get_user_choice('Scissors'))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(root, text="", padx=20, pady=10,bg="#B4D4FF")
result_label.grid(row=1, column=0, columnspan=3)

user_score_label = tk.Label(root, text=f"Your Score: {user_score}",bg="#B4D4FF",font=("Helvetica",11,"bold"))
user_score_label.grid(row=2, column=0, columnspan=3)

computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}",bg="#B4D4FF",font=("Helvetica",11,"bold"))
computer_score_label.grid(row=3, column=0, columnspan=3)

winner_label = tk.Label(root, text="", padx=20, pady=10,bg="#B4D4FF")
winner_label.grid(row=4, column=0, columnspan=3)

root.mainloop()
