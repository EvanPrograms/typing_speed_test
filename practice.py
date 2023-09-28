import time
import pyautogui
import threading
import json
import random

# Opening text file with multiple different typing tests
with open("choices.txt", "r") as tests:
    data = json.load(tests)

# Selecting a random test and turning it into a list
choice = str(random.randint(1, 5))
string = data[choice]
string_list = string.split()


# Create timer. Change time.sleep(x) to desired typing test time length
def break_input():
    time.sleep(10)


def begin_typing():
    threading.Thread(target=break_input).start()
    prompt = f"Begin typing \n"
    code = input(prompt)
    return code


print(string)
typed_out = begin_typing()
typed_out_list = typed_out.split()
words = 0
for value in typed_out_list:
    if value in string_list:
        words += 1
        string_list.remove(value)
print(f"You have typed {words} words")
# Adjust the (X/60) to match the time.sleep(x) value to mirror length of test
print(f"You have typed {int(words / (10/60))} WPM")