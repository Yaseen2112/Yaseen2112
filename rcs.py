import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You Win!"
    else:
        return "You Lose!"

# Function to handle user choice
def play(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    # Update labels and scores
    user_choice_label.config(text=f"Your Choice: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice.capitalize()}")
    result_label.config(text=result)
    
    if result == "You Win!":
        global user_score
        user_score += 1
        user_score_label.config(text=f"Your Score: {user_score}")
    elif result == "You Lose!":
        global computer_score
        computer_score += 1
        computer_score_label.config(text=f"Computer's Score: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score, computer_score = 0, 0
    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer's Score: 0")
    user_choice_label.config(text="Your Choice: None")
    computer_choice_label.config(text="Computer's Choice: None")
    result_label.config(text="Welcome to Rock-Paper-Scissors!")

# Create main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Set window size and position
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Initialize scores
user_score = 0
computer_score = 0

# Create and place widgets
title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

user_choice_label = tk.Label(root, text="Your Choice: None", font=("Arial", 12))
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer's Choice: None", font=("Arial", 12))
computer_choice_label.pack()

result_label = tk.Label(root, text="Welcome to Rock-Paper-Scissors!", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Rock", command=lambda: play("rock")).grid(row=0, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Paper", command=lambda: play("paper")).grid(row=0, column=1, padx=10, pady=10)
tk.Button(button_frame, text="Scissors", command=lambda: play("scissors")).grid(row=0, column=2, padx=10, pady=10)

score_frame = tk.Frame(root)
score_frame.pack(pady=10)

user_score_label = tk.Label(score_frame, text="Your Score: 0", font=("Arial", 12))
user_score_label.grid(row=0, column=0, padx=10)

computer_score_label = tk.Label(score_frame, text="Computer's Score: 0", font=("Arial", 12))
computer_score_label.grid(row=0, column=1, padx=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Arial", 12))
reset_button.pack(pady=10)

# Start the application
root.mainloop()
