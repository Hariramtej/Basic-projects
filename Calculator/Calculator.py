
from tkinter import Tk, Entry, Button, StringVar

class Calculator:

    def __init__(self,master):
        
        master.title("Calculator")

        #First two values are used for the length and width of the window and the next to for the position of the window on the screen
        master.geometry("357x420+0+0")

        # Entering the background color
        master.config(bg = 'Gray')
        master.resizable(False,False)

        # self.equation is used to display the typed values and results inside the calculator
        self.equation = StringVar()
        # temporarily we are storing nothing in this space
        self.entry_value =''

        # Styling the text which gets displayed
        Entry(width=17,bg='#ccddff',font=('Arial Bold',28),textvariable = self.equation).place(x=0,y=0)

        # Designing all the buttons involved in the calculator
        Button(width=11, height=4, text='(', relief='flat',bg='white',command=lambda:self.show("(")).place(x=0 ,y=50 )
        Button(width=11, height=4, text=')', relief='flat',bg='white',command=lambda:self.show(')')).place(x=90 ,y=50 )
        Button(width=11, height=4, text='%', relief='flat',bg='white',command=lambda:self.show('%')).place(x=180 ,y=50 )
        Button(width=11, height=4, text='1', relief='flat',bg='white',command=lambda:self.show(1)).place(x=0 ,y=125 )
        Button(width=11, height=4, text='2', relief='flat',bg='white',command=lambda:self.show(2)).place(x=90 ,y=125 )
        Button(width=11, height=4, text='3', relief='flat',bg='white',command=lambda:self.show(3)).place(x=180 ,y=125 )
        Button(width=11, height=4, text='4', relief='flat',bg='white',command=lambda:self.show(4)).place(x=0 ,y=200 )
        Button(width=11, height=4, text='5', relief='flat',bg='white',command=lambda:self.show(5)).place(x=90 ,y=200 )
        Button(width=11, height=4, text='6', relief='flat',bg='white',command=lambda:self.show(6)).place(x=180 ,y=200 )
        Button(width=11, height=4, text='7', relief='flat',bg='white',command=lambda:self.show(7)).place(x= 0,y=275 )
        Button(width=11, height=4, text='8', relief='flat',bg='white',command=lambda:self.show(8)).place(x=90 ,y=275 )
        Button(width=11, height=4, text='9', relief='flat',bg='white',command=lambda:self.show(9)).place(x=180 ,y=275 )
        Button(width=11, height=4, text='0', relief='flat',bg='white',command=lambda:self.show(0)).place(x=90 ,y=350 )
        Button(width=11, height=4, text='+', relief='flat',bg='white',command=lambda:self.show('+')).place(x=270 ,y=275 )
        Button(width=11, height=4, text='-', relief='flat',bg='white',command=lambda:self.show('-')).place(x=270 ,y=200 )
        Button(width=11, height=4, text='*', relief='flat',bg='white',command=lambda:self.show('*')).place(x=270 ,y=50 )
        Button(width=11, height=4, text='/', relief='flat',bg='white',command=lambda:self.show('/')).place(x=270 ,y=125 )
        Button(width=24, height=4, text='=', relief='flat',bg='lightblue',command=self.solve).place(x=180 ,y=350 )
        Button(width=11, height=4, text='c', relief='flat',command=self.clear).place(x=0 ,y=350 )
        

        
    def show(self, value):

        # Incrementing i.e increasing each character we enter into the text box!!!
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    
    def clear(self):

        # Clearing the text box
        self.entry_value = ''
        self.equation.set(self.entry_value)


    def solve(self):

        # eval is a inbuilt function used to calculate basic math calculations
        result = eval(self.entry_value)
        self.equation.set(result)


root = Tk()
Calculator = Calculator(root)
root.mainloop()

