from tkinter import *
import json
import random

typing = ""
character = 0
timer_id = ""
string = ""


# Test only begins on first character press. Can change test time with window.after in ms
# make sure to update WPM in results to reflect test time
def begin_typing(event):
    global character
    global typing
    global timer_id
    if character == 0:
        print("timer started")
        character += 1
        timer_id = window.after(10000, results)


# User input compared against test
def results():
    global string
    global typing
    typing = text_typing_label.get("1.0", 'end-1c')
    window.after_cancel(timer_id)
    string_list = string.split()
    typing_results = typing.split()
    words = 0
    for value in typing_results:
        if value in string_list:
            words += 1
            string_list.remove(value)
    print(f"You have typed {words} words")
    # Adjust the (X/60) to match the window.after value to mirror length of test
    print(f"You have typed {int(words / (10 / 60))} WPM")
    your_results = f"You have typed {words} words\nYou have typed {int(words / (10 / 60))} WPM"
    results_label.configure(text=your_results)


# Restart test
def restart():
    global character
    global timer_id
    window.after_cancel(timer_id)
    timer_id = ""
    text_typing_label.delete("1.0", "end")
    character = 0
    results_label.configure(text="Good luck!")


# Changes the test selection for typing
def change():
    global string
    previous_string = string
    with open("choices.txt", "r") as tests:
        data = json.load(tests)
    choice = str(random.randint(1, 5))
    string = data[choice]
    while previous_string == string:
        choice = str(random.randint(1, 5))
        string = data[choice]
    test_label.delete("1.0", "end")
    test_label.insert(END, string)


# Initialize TKinter
window = Tk()
window.title("Type speed checker!")
window.geometry("1000x500")

# Text box showing test
test_label = Text(window, height=10, width=100, wrap=WORD)
test_label.grid()

# Text box for user entry
text_typing_label = Text(window, height=10, width=100)
text_typing_label.bind('<Key>', begin_typing)
text_typing_label.grid(padx=(100, 100))

# Results of speed test in WPM
results_label = Label(window, text="Good luck!")
results_label.grid()

# Resets the test
reset_button = Button(text="Restart", command=restart)
reset_button.grid()

# Changes the test to a different choice in dictionary
change_test = Button(text="Change Test", command=change)
change_test.grid()

# Displays initial test chosen
change()

window.mainloop()
