# import random
#
# dice=random.randint(1, 10)
# quit=False
# while quit !=True:
#     print(dice)
#     dice
#     guess = input("Enter your guess")
#     if guess==dice:
#         quit=True
#         print("good job")
##################################################RANDOM NUM GUESSING GAME
#import random
#
# def guess(randomNum):
#     gameOver = False
#     while not gameOver:
#         userInput = int(input("Guess a number: "))
#         if randomNum == userInput:
#             gameOver = True
#             print("You win!")
#
# randomNum = random.randint(1, 50)
# print(randomNum)
# guess(randomNum)
##################################################################################SIMPLE TO-DO LIST
#
# tasks = []
#
# def add(task):
#     tasks.append(task)
#     for x in tasks:
#         print(x)
#
# def remove(task):
#     if task in tasks:
#         tasks.remove(task)
#     else:
#         print("The word " + task + " does not exist in the to-do list.")
#     for x in tasks:
#         print(x)
#
# def edit(task, newTask):
#     if task in tasks:
#         if newTask not in tasks:
#             index = tasks.index(task)
#             tasks[index] = newTask
#             print("Edited the task.")
#         else:
#             print("New task already exists.")
#     else:
#         print("Task not found.")
#
#     for x in tasks:
#         print(x)
#
# for x in tasks:
#     print(x)
#
# exit = False
#
# while not exit:
#     choice = input("What would you like to do? Enter 'a' to add, 'r' to remove, 'e' to edit, or 'q' to quit: ")
#
#     if choice == 'a':
#         task = input("Enter a task to add: ")
#         add(task)
#
#     elif choice == 'r':
#         task = input("Enter a task to remove: ")
#         remove(task)
#
#     elif choice == 'e':
#         task = input("Enter the task name that you want to change: ")
#         if task in tasks:
#             newTask = input("Enter the new task name you would like to change it to: ")
#             edit(task, newTask)
#         else:
#             print("That task does not exist")
#     elif choice == 'q':
#         exit = True
#
#     else:
#         print("Incorrect choice")

######################################################################################ADD TO ARRAY AND SWITCH LETTERS

# letters=[]
# word=input("Enter a word ")
# for x in word:
#     letters.append(x)
#
# for x in letters:
#     print (x)
#
# charr=input("Enter a char you would like to move")
# newIndex=int(input("Enter a new position"))
#
# if charr in letters:
#     letters.remove(charr)
#     letters.insert(newIndex,charr)
#
# print (letters)
##########################################################################PULL STRING FROM WORD
# import random
# word=[]
# userWord=input("Enter a word")
# for char in userWord:
#     word.append(char)
#
# print(word)
# string=input("Enter a string to pull from the word")
# for x in string:
#     if x in word:
#         word.remove(x)
#
#
# print(word)
############################################################################SIMPLE HANGMAN GAME
# import random
#
# word="smart"
# blank="_____"
# lives=7
# letters=[]
# correct=[]
# gameOver=False
#
# while lives>0 and gameOver is not True:
#     print(blank)
#     guess=input("Enter a character to guess ")
#     trimmedGuess=guess.strip()
#     if len(trimmedGuess)==1:
#         if guess in word:
#             if guess not in letters:
#                 print("you got " + guess + " right")
#                 letters.append(guess)
#                 correct.append(guess)
#
#             else:
#                 print("You already guessed: " +guess)
#         elif guess in letters:
#             print("You already guessed: " +guess)
#
#         else:
#             lives -=1
#             print("you got " +guess+ " wrong")
#             letters.append(guess)
#
#         if len(correct)==5:
#             print("You got the word " +word)
#             break
#     else:
#         print("You must enter 1 character only")
# else:
#     print("Game Over, the word was: " +word)
################################################################################INDEX FROM STRING
# word = "hello"
# censoredWord = "_____"
# gameOver=False
# lives=8
#
# while not gameOver:
#     print(censoredWord)
#     while lives >0:
#         guess = input("Guess a character: ").strip()
#         newCensoredWord = ""
#         correctGuess=False
#
#         for i in range(len(word)):
#             if word[i] == guess.strip():
#                 newCensoredWord += guess.strip()
#                 correctGuess=True
#             else:
#                 newCensoredWord += censoredWord[i]
#
#         if newCensoredWord==word:
#             gameOver=True
#             break
#
#
#         censoredWord = newCensoredWord
#         print(censoredWord)
#
#
#
#         if not correctGuess:
#             lives = lives-1
#             print("You got " +guess+ " wrong")
#
#     else:
#         print("You ran out of lives")
#         break
#
# else:
#     print("you win")

# import pygame
# import random
#
#
# pygame.init()
# surface = pygame.display.set_mode((800, 700))
# pygame.display.set_caption("Hangman")
#
# x = 400
# y = 300
#
# color = (255, 0, 0)
# rect = pygame.Rect(x, y, 50, 50)
# running = True
# moveLeft = False
# moveRight = False
# foodEaten = False
#
# clock = pygame.time.Clock()
#
#
# pygame.init()
# surface = pygame.display.set_mode((800, 700))
# pygame.display.set_caption("Hangman")
#
# x = 400
# y = 300
#
# color = (255, 0, 0)
# rect = pygame.Rect(x, y, 50, 50)
# running = True
# moveLeft = False
# moveRight = False
# moveUp = False
# moveDown = False
# inBound = True
#
#
#
# clock = pygame.time.Clock()
#
# while running:
#     surface.fill((0, 0, 0))
#     pygame.draw.rect(surface, color, rect)
#     pygame.display.update()
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 x -= 10
#             if event.key == pygame.K_RIGHT:
#                 x += 10
#             if event.key == pygame.K_UP:
#                 y -= 10
#             if event.key == pygame.K_DOWN:
#                 y += 10
#
#             rect.x = x
#             rect.y = y
#             pygame.display.update()
#
#
#
# pygame.quit()
#########################ROCK PAPER SCISSOR###########################
import random

def computerGuess():
    choices = ['Rock', 'Paper', 'Scissors']
    compChoice = random.choice(choices)
    return compChoice


def compareChoices(userGuess):
    compGuess = computerGuess()
    userTotal = 0
    compTotal = 0
    if compGuess == userGuess:
        print("Computer picked " + compGuess + ". Go again.")
    elif compGuess == "Rock" and userGuess == "Paper":
        print("User guessed Paper - User wins")
        userTotal += 1
    elif compGuess == "Scissors" and userGuess == "Rock":
        print("User guessed Rock - User wins")
        userTotal += 1
    elif compGuess == "Paper" and userGuess == "Scissors":
        print("User guessed Scissors - User wins")
        userTotal += 1
    elif compGuess == "Paper" and userGuess == "Rock":
        print("Computer guessed Paper - Comp wins")
        compTotal += 1
    elif compGuess == "Rock" and userGuess == "Scissors":
        print("Computer guessed Rock - Comp wins")
        compTotal += 1
    elif compGuess == "Scissors" and userGuess == "Paper":
        print("Computer guessed Scissors - Comp wins")
        compTotal += 1

    print("User total: " + str(userTotal) + " Comp total: " + str(compTotal))


gameRunning = True
while gameRunning:
    guess = input("Enter your guess (Rock, Paper, or Scissors): ")
    if guess == "exit":
        gameRunning = False
    elif guess not in ["Rock", "Paper", "Scissors"]:
        print("Enter Rock, Paper, or Scissors.")
    else:
        compareChoices(guess)




