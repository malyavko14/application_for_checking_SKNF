from tkinter import *
from tkinter import messagebox
from check_SKNF_properties import check_SKNF


class GUICheckTheSKNFFormula:
    def __init__(self):
        self.window = Tk()
        self.window.title("Application for checking whether the formula is SKNF")
        self.window.wm_attributes('-alpha', 1)
        self.window.geometry('450x150')
        self.window.resizable(height=False, width=False)

        self.frame = Frame(self.window, bg='#bac7cf')
        self.frame.place(relwidth=1, relheight=1)
        self.title = Label(self.frame, text='Enter formula', bg='#bac7cf', font="Arial 16")
        self.title.pack()
        self.enterFormula = Entry(self.frame, width=45)
        self.enterFormula.pack()
        self.checkButton = Button(self.frame, text='Check', font="Arial 16", command=self.check, bg='#ead7d2')
        self.checkButton.pack()

        self.photo = PhotoImage(file="question_symbol.png")
        memoButton = Button(self.frame, image=self.photo, highlightthickness=0, bd=0, command=self.manual)
        memoButton.place(x=415, y=5)
        self.window.mainloop()

    def check(self):
        result = 'This formula is SKNF' if check_SKNF(self.enterFormula.get()) else 'This formula is not a SKNF'
        messagebox.showinfo("Result", f"{result}")

    def manual(self):
        def close():
            instructionWindow.destroy()

        instructionWindow = Toplevel()
        instructionWindow['bg'] = '#bac7cf'
        instructionWindow.geometry('250x100')
        instructionWindow.title("Manual")
        instructionWindow.resizable(False, False)
        Label(instructionWindow,
              text="\/ - disjunction \n /\ - conjunction \n ! - negation  \n [A...Z] - latin alphabet",
              font="Arial 12", bg='#bac7cf').pack()
        closeButton = Button(instructionWindow, text='OK', font="Arial 12", bg='#ead7d2', command=close)
        closeButton.pack()
