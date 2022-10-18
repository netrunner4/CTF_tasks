#  Made for a friend after CTF (28.09.2021), just for fun

import string
import random

# Take words from list
words = ["Bass", "Battle", "Beast", "Bees", "Berries", "Birds", "Bite", "Black", "Boundary", "Brown", "Walk", "Watching", "Water", "Weather", "Weight", "Wilderness", "Winter", "Wolves", "Males", "Mammal", "Mate", "Maul", "May", "Meadow", "Migrate", "Milk", "Mountain", "Movement"]
word_chosen = random.choice(words)

# Generation of x, y for words
x = random.randrange(0, 13)
y = random.randrange(0, 13)
while True:
    if 15 - x < len(word_chosen):
        x = random.randrange(0, 13)
        continue
    elif 15 - y < len(word_chosen):
        y = random.randrange(0, 13)
        continue
    else:
        break

# Creation of filled matrix
s = string.ascii_letters.upper()
a = []
for i in range(16):
    a += [[]]
    for j in range(16):
        a[i] += random.choice(s)

# Choise of direction for word and its addition to matrix
play = random.randrange(1, 4)
correct = []
if play == 1:
    for i in range(len(word_chosen)):
        a[y+i][x] = word_chosen.upper()[i]
        correct += [(x, y+i)]
elif play == 2:
    for i in range(len(word_chosen)):
        a[y][x+i] = word_chosen.upper()[i]
        correct += [(x + i, y)]
elif play == 3:
    for i in range(len(word_chosen)):
        a[y+i][x+i] = word_chosen.upper()[i]
        correct += [(x + i, y + i)]

# Matrix output
for i in range(16):
    print("")
    if i >= 10:
        print(i, "| ", end=" ")
    elif i <= 10:
        print(i, " | ", end=" ")
    for j in range(16):
        print(a[i][j], end=" ")
print("\n\nWord to find:", word_chosen.upper())
print("Answer example: [(9, 3), (10, 4), (11, 5), (12, 6), (13, 7)]")

# Answer check
answer = input()
if str(correct) == answer:
    print("Correct")
elif str(correct) != answer:
    print("Wrong, correct answer: "+str(correct))
