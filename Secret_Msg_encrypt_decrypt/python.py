from tkinter import *
from tkinter import messagebox
# base64 is a module used for encoding and decoding a given data
import base64
import os

def decrypt():

    password = code.get()

    if password == "1234":

        # The function Toplevel is used for creating a new window on the screen
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg = '#00bd56')

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        # The function Label is used for displaying something on the screen
        Label(screen2, text= "Decrypt", font="arial", fg="white", bg="#00bd56").place(x = 10, y = 0)
        text2 = Text(screen2, font = "Rpbote 10", bg = "white",relief = GROOVE, wrap = WORD, bd = 0)
        text2.place( x =10, y = 40, width= 380, height=150)

        text2.insert(END, decrypt)

    elif password=="":
        messagebox.showerror("decryption", "Input Password")

    elif password != "1234":
        messagebox.showerror("decryption", "Invalid Password")


def encrypt():

    password = code.get()

    if password == "1234":

        # The function Toplevel is used for creating a new window on the screen
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg = '#ed3833')

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        # The function Label is used for displaying something on the screen
        Label(screen1, text= "Encrypt", font="arial", fg="white", bg="#ed3833").place(x = 10, y = 0)
        text2 = Text(screen1, font = "Robote 10", bg = "white", relief=GROOVE, wrap=WORD,bd = 0)
        text2.place(x =10, y = 40, width= 380, height=150)

        text2.insert(END, encrypt)

    elif password=="":
        messagebox.showerror("encryption", "Input Password")

    elif password != "1234":
        messagebox.showerror("encryption", "Invalid Password")



def main_screen():

    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")

    # setting icon
    # entering the correct path with reversing the slashes
    image_icon = PhotoImage(file="C:/Users/Admin/Downloads/qualitative-research.png")
    screen.iconphoto(False, image_icon)

    screen.title("PCT App")

    def reset():

        code.set("")
        # 1.0 specifies the first line and 0th position i.e from the beginning
        text1.delete(1.0, END)

    # Introduction message
    Label(text = "Enter text for encrytion and decryption", fg="black",font = ("calbri",13)).place(x = 10,y = 10)

    # Relief is used for the border and wrap controls the text when it excedes the space specified for it to be written in.
    text1 = Text(font = "Robote 20",bg="white", relief = GROOVE, wrap = WORD, bd = 0)
    text1.place(x = 10, y = 50, width = 355, height = 100)

    Label(text = "Enter the secret key for encryption and decryption", fg="black", font=("calibri",13)).place(x =10,y = 160)

    code = StringVar()
    Entry(textvariable = code, width= 19, bd = 0, font=('arial', 25),show="*").place(x = 10, y = 190)

    Button(text = "Entrypt", height = '2', width = '23', bg = "#ed3833", fg = "white", bd = 0, command=encrypt).place(x = 10, y = 250)
    Button(text = "Decrypt", height = '2', width = '23', bg = "#00bd56", fg = "white", bd = 0, command=decrypt).place(x = 200, y = 250)
    Button(text = 'Reset', height = "2", width = '50', bg = "#1089ff",fg = 'white',bd = 0, command= reset ).place(x = 10, y = 300)

    screen.mainloop()

main_screen()