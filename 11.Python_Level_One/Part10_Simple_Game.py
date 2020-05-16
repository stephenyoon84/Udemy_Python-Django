###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
# print(digits[:3])

# Another hint:
# guess = input("What is your guess? ")
# print(guess)

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

def generate_three_digits():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

def get_guess():
    guess = input("What is your guess?")
    return convert_num_to_list(guess)

def convert_num_to_list(num):
    return [int(x) for x in str(num)]

# def check_target(tar, list):
#     if (tar[0] == list[0] and tar[1] == list[1] and tar[2] == list[2]):
#         return True
#     return False

# def game_start():
#     print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
#     target = generate_three_digits()
#     print("Code has been generated, please guess a 3 digit number.")
#     print(target)
#     guess = get_guess()
#     print(guess)
#     while (target[0] == guess[0] and target[1] == guess[1] and target[2] == guess[2]):
#         if (guess[0] in target or guess[1] in target or guess[2] in target):
#             print("Close")
#         else:
#             print("Nope")



# game_start()