import pyperclip
import random

import emojilist

# Gather input.
while True:
    emoji_chance = input("Input a number from 0 to 1.0 for the emoji density (defaults to 0.5):\n") or 0.5
    try:
        if 0 <= float(emoji_chance) <= 1:
            break
    except: 
        pass
    print("That is not a valid input you fool!")

text = list(input("Input the message you wish to emojify:\n"))

# Process input.
for n, i in enumerate(text):
    if i == " " and random.random() <= float(emoji_chance):
        text[n] = random.choice(emojilist.EMOJI_LIST)

# Format and return result.
text = "".join(text)
pyperclip.copy(text)
print("The result has been copied to your clipboard")
