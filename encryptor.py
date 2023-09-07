import os
import random

t = []
text = ""
crypt = ""

cap_lets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def make_block(letters, brick_size, brick_var, codes):
    while True:
        let = letters
        random.shuffle(let)
        code = let[:round(brick_size+(brick_var*random.random()))]
        if not code in codes: 
            c = ""
            for co in code:
                c+=co
            return c

while True:
    txt = input("Enter the text to be encypted (type 'done' when you have finished): ").lower() + "\n"
    if txt == "done\n":
        break
    t.append(txt)   

for i, z in enumerate(t):
    text += z

text = text[:-1]

inp = input("Chose the encryptor:\n1) Letter Pusher\n2) Letter Bricks\n")

if inp == "1":
    letter_shift = int(input("How much should letters be pushed? "))

    for i in text:
        try: crypt += letters[(letters.index(i)+letter_shift)%26]
        except Exception: crypt+=i

if inp == "2": 
    brick_size = int(input("How big should the brick be? "))
    brick_var = int(input("How big should the brick variation be (at most)? "))
    letter_assigned = []
    for _ in range(len(letters)):
        letter_assigned.append(make_block(letters, brick_size, brick_var, letter_assigned))
    for let in text:
        try: crypt += letter_assigned[letters.index(let)] + " "
        except Exception: crypt+=let
os.system("cls")
input(crypt)
text_file = open("crypt.txt", "w", encoding="utf-8")
n = text_file.write(crypt)
text_file.close()

