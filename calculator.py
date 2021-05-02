import math
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, StringVar, ttk
from tkinter.ttk import *
import expressionparse


class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.style = ttk.Style()
        # Setting style so it won't be ugly
        self.style.theme_use('xpnative')

        # the outcome of the mathematical actions
        self.total = 0
        # the input
        self.input = 0

        # the outcome label
        self.total_label_text = StringVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        # the input entry
        self.entry_text = StringVar()
        self.entry_text.set('0')
        self.entry = Entry(master, textvariable=self.entry_text)

        # button for each action
        # Given an input, outputs to the total_label_text the corrects output
        self.equal_button = Button(master, text="=", command=lambda: self.set_total_label("equal"))
        # Resets the total_label_text and the input entry
        self.reset_button = Button(master, text="Reset", command=lambda: self.set_total_label("reset"))
        # Adds the total_label_text to the input entry
        self.ans_button = Button(master, text="ANS", command=lambda: self.write_answer_to_entry())

        # Clicking this button will set total_label_text to log(total_label_text)
        self.ln_ans_button = Button(master, text="ln(ANS)", command=lambda: self.set_total_label("log"))
        # Clicking this button will set total_label_text to e^(total_label_text)
        self.e_power_ans_button = Button(master, text="e^(ANS)", command=lambda: self.set_total_label("e_power"))
        # Clicking this button will set total_label_text to sqrt(total_label_text)
        self.sqrt_ans_button = Button(master, text="ANS^0.5", command=lambda: self.set_total_label("sqrt"))
        # Clicking this button will set total_label_text to total_label_text^(2)
        self.squared_ans_button = Button(master, text="ANS^2", command=lambda: self.set_total_label("squared"))

        # All these buttons add the matching action to the input entry
        self.plus_button = Button(master, text="+", command=lambda: self.add_action_to_entry("+"))
        self.subtract_button = Button(master, text="-", command=lambda: self.add_action_to_entry("-"))
        self.mult_button = Button(master, text="*", command=lambda: self.add_action_to_entry("*"))
        self.div_button = Button(master, text="/", command=lambda: self.add_action_to_entry("/"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=1, sticky=E)
        self.ans_button.grid(row=0, column=2)
        self.reset_button.grid(row=0, column=3, sticky=W + E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W + E)
        self.equal_button.grid(row=1, column=3)

        self.sqrt_ans_button.grid(row=2, column=0)
        self.squared_ans_button.grid(row=2, column=1)
        self.ln_ans_button.grid(row=2, column=3)
        self.e_power_ans_button.grid(row=2, column=2)

        self.plus_button.grid(row=3, column=0)
        self.subtract_button.grid(row=3, column=1)
        self.mult_button.grid(row=3, column=2)
        self.div_button.grid(row=3, column=3)

    # Given a method (equal, reset or log) this function sets total_label_text to its correct value
    def set_total_label(self, method):
        if method == 'equal':
            expression = self.entry.get()
            if not expression:
                expression = '0'
            try:
                # Using the expressionparse library we parse the input and evaluate it
                # if we cannot evaluate it or parse it total_label_text will show an exception
                t = expressionparse.Tree()
                t.parse(expression)
                self.total = t.evaluate()
            except:
                self.total = "Incorrect math expression"
        elif method == 'log':
            if self.total_label_text.get() != "Incorrect math expression" and float(self.total_label_text.get()) > 0:
                self.total = math.log(float(self.total_label_text.get()))
            else:
                self.total = "Incorrect math expression"
        elif method == 'e_power':
            if self.total_label_text.get() != "Incorrect math expression":
                self.total = math.exp(float(self.total_label_text.get()))
        elif method == 'squared':
            if self.total_label_text.get() != "Incorrect math expression":
                self.total = math.pow(float(self.total_label_text.get()), 2)
        elif method == 'sqrt':
            if self.total_label_text.get() != "Incorrect math expression" and float(self.total_label_text.get()) >= 0:
                self.total = math.sqrt(float(self.total_label_text.get()))
            else:
                self.total = "Incorrect math expression"
        elif method == 'reset':
            self.total = '0'

        self.total_label_text.set(str(self.total))
        self.entry_text.set('0')
        self.entry.focus()
        self.entry.icursor(END)

    # This function adds the content in total_label_text to the input entry
    def write_answer_to_entry(self):
        if self.total_label_text.get() != "Incorrect math expression":
            self.entry_text.set(self.entry_text.get()+self.total_label_text.get())
            self.entry.focus()
            self.entry.icursor(END)

    # This function adds the matching action to the input entry
    def add_action_to_entry(self, action):
        self.entry_text.set(self.entry_text.get() + action)
        self.entry.focus()
        self.entry.icursor(END)


root = Tk()
my_gui = Calculator(root)
root.mainloop()
