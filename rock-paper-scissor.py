import random
import time

def print_with_delay(text, delay=0.03):
    """Print text with a slight delay between characters for a better CLI experience"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_header():
    """Display the game header"""
    header = """
    ╔═══════════════════════════════════════╗
    ║         ROCK PAPER SCISSORS           ║
    ╚═══════════════════════════════════════╝
    """
    print(header)

def display_rules():
    """Display the game rules"""
    rules = """
    RULES:
    - Rock crushes Scissors
    - Scissors cuts Paper
    - Paper covers Rock
    
    HOW TO PLAY:
    Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors
    Enter 'q' to quit the game
    """
    print(rules)

def get_user_choice():
    """Get and validate the user's choice"""
    valid_choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'q': 'Quit'}
    
    while True:
        print("\nEnter your choice (r/p/s or q to quit): ", end='')
        user_input = input().lower()
        
        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid choice! Please enter 'r', 'p', 's', or 'q'.")

def get_computer_choice():
    """Generate a random choice for the computer"""
    choices = ['r', 'p', 's']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the round"""
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    
    print(f"\nYou chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")
    
    # If choices are the same, it's a tie
    if user_choice == computer_choice:
        return "tie"
    
    # All winning conditions for the user
    if (user_choice == 'r' and computer_choice == 's') or \
       (user_choice == 's' and computer_choice == 'p') or \
       (user_choice == 'p' and computer_choice == 'r'):
        return "user"
    
    # Otherwise, computer wins
    return "computer"

def display_result(result):
    """Display the result of the round"""
    if result == "tie":
        print_with_delay("\n🤝 It's a tie! 🤝")
    elif result == "user":
        print_with_delay("\n🎉 You win this round! 🎉")
    else:
        print_with_delay("\n💻 Computer wins this round! 💻")

def display_score(user_score, computer_score, ties):
    """Display the current score"""
    score_board = f"""
    ┌───────────────────────────┐
    │         SCOREBOARD        │
    ├───────────┬───────────────┤
    │ You       │ {user_score:<13} │
    │ Computer  │ {computer_score:<13} │
    │ Ties      │ {ties:<13} │
    └───────────┴───────────────┘
    """
    print(score_board)

def play_again():
    """Ask if the user wants to play again"""
    while True:
        print("\nDo you want to play again? (y/n): ", end='')
        choice = input().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Please enter 'y' or 'n'.")

def main():
    """Main game function"""
    display_header()
    display_rules()
    
    user_score = 0
    computer_score = 0
    ties = 0
    round_number = 1
    
    while True:
        print(f"\n===== Round {round_number} =====")
        
        user_choice = get_user_choice()
        if user_choice == 'q':
            break
        
        # Add a little suspense
        print("\nRock...")
        time.sleep(0.5)
        print("Paper...")
        time.sleep(0.5)
        print("Scissors...")
        time.sleep(0.5)
        print("Shoot!")
        time.sleep(0.3)
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_result(result)
        
        # Update scores
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            ties += 1
        
        display_score(user_score, computer_score, ties)
        
        round_number += 1
        
        # Check if user wants to continue after every 3 rounds
        if round_number % 4 == 0:
            if not play_again():
                break
    
    # Game over
    print_with_delay("\n🎮 Game Over! 🎮")
    print("\nFinal Score:")
    display_score(user_score, computer_score, ties)
    
    # Determine overall winner
    if user_score > computer_score:
        print_with_delay("\n🏆 Congratulations! You are the overall winner! 🏆")
    elif computer_score > user_score:
        print_with_delay("\n💻 The computer is the overall winner! Better luck next time! 💻")
    else:
        print_with_delay("\n🤝 The game ended in a tie! 🤝")
    
    print_with_delay("\nThanks for playing Rock Paper Scissors!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Game terminated.")