from random import  choice

user_choice = input("Pick a choice (rock, paper, scissor): ")

options = ["rock", "paper", "scissor"]
cpu_choice = choice(options)
print("CPU Choice: ", cpu_choice)


