import random

logo = '''

 ██████╗ ██╗   ██╗███████╗███████╗███████╗████████╗██╗  ██╗███████╗███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝╚══██╔══╝██║  ██║██╔════╝████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗   ██║   ███████║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║   ██║   ██╔══██║██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████║   ██║   ██║  ██║███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝                                       
'''
# GLOBAL CONSTANTS
ATTEMPTS_EASY_LEVEL = 10
ATTEMPTS_HARD_LEVEL = 5


def compare_answer(your_guess, the_number, attempts):
	''' Compares the guess against the random generated number and return the number of attempts remaining.
 	'''
	if your_guess > the_number:
		print("Too high!")
		return attempts - 1 
	elif your_guess < the_number:
		print("Too low!")
		return attempts - 1
	else: 
		print(f"You guessed right. The answer is {the_number}.")
		
def set_difficulty():
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if difficulty == 'easy':
		return ATTEMPTS_EASY_LEVEL
	else:
		return ATTEMPTS_HARD_LEVEL

def game():
	print(logo)
	print("Welcome to Mirela's Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100..")
	the_number = random.randint(1, 100)
	print(f"Tip: the actual number is {the_number}.")
	
	attempts = set_difficulty()
	
	your_guess = 0
	while your_guess != the_number:
		print(f"You have {attempts} attempts remaining to guess the number.")	
		your_guess = int(input("Make a guess: "))
		attempts = compare_answer(your_guess, the_number, attempts)
		
		if attempts == 0:
			print("You've run out of guesses, you lose.")
			return
		elif your_guess != the_number:
			print("Guess again.")
		

		
game()