from tkinter import *
from tkinter import messagebox

calculator = Tk()
calculator.title("CALCULATOR")
calculator.resizable(0, 1)

class Application(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.createWidgets()
        self.grid()

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def appendToDisplay(self, text):
        self.entryText = self.display.get()
        self.textLength = len(self.entryText)

        if self.entryText == "0":
            self.replaceText(text)
        else:
            self.display.insert(self.textLength, text)

    def calculateExpression(self):
        self.expression = self.display.get()
        self.expression = self.expression.replace("%", "/ 100")

        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)
        except:
            messagebox.showinfo("ERROR", "Invalid input", icon="warning", parent=calculator)

    def clearText(self):
        self.replaceText("0")

    def createWidgets(self):
        button_bg = "#333333"
        button_fg = "#FFFFFF"
        button_active_bg = "#555555"
        button_borderwidth = 2
        display_bg = "#000000"
        display_fg = "#FFFFFF"

        self.display = Entry(self, font=("Helvetica", 20), borderwidth=0, relief=RAISED, justify=RIGHT, bg=display_bg, fg=display_fg)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('/', 2, 3), ('%', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('=', 3, 4),
            ('000', 4, 0), ('00', 4, 1), ('0', 4, 2), ('.', 4, 3), ('+', 4, 4)
        ]

        for button in buttons:
            text, row, column = button[0], button[1], button[2]
            command = lambda t=text: self.appendToDisplay(t) if t not in ["=", "C"] else (self.calculateExpression if t == "=" else self.clearText)
            Button(self, font=("Helvetica", 18), text=text, borderwidth=button_borderwidth, bg=button_bg, fg=button_fg, activebackground=button_active_bg, command=command, highlightthickness=button_borderwidth).grid(row=row, column=column, sticky="NWNESWSE")

app = Application(calculator)
calculator.configure(bg='#000000')
calculator.mainloop()
