from tkinter import *
from tkinter import messagebox, ttk
import googletrans 
from textblob import TextBlob

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

# The below function to constantly update the the text we are entering into the combo boxes.(After every 500 milliseconds i.e. every half second)
def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text = c1)
    label2.configure(text = c2)
    root.after(500,label_change)

def translate_now():
    global language

    try:
        text_ = text1.get(1.0,END)
        c2 = combo1.get()
        c3 = combo2.get()

        if (text_):
            words = TextBlob(text_)
            lan = words.detect_language()

            for i,j in language.items():
                if (j == c3):
                    lan_ = i
            words = words.translate(from_lang = lan, to = str(lan_))
            text2.delete(1.0,END)
            text2.insert(END, words)
    except Exception as e:
        messagebox.showerror("googletrans", "please try again")




# icon
image_icon = PhotoImage(file="C:/Users/Admin/OneDrive/Desktop/Important docunments/Google_Translate_Icon.png")
root.iconphoto(False, image_icon)

#arrow
arrow_image = PhotoImage(file = "C:/Users/Admin/OneDrive/Desktop/F1221G2H/Translator/1969111.png")
image_label = Label(root, image = arrow_image, width = 150)
image_label.place(x = 460, y = 70)

# this imports different languages into a DICTIONARY
language = googletrans.LANGUAGES
# this converst all the names of the language from the dictionary into a list
languageV = list(language.values())
# this converts all the language codes from the dictionary into a seperate list
lang1 = list(language.keys())

combo1 = ttk.Combobox(root , values= languageV, font = "Robot 14", state = 'r')
combo1.place(x = 110, y = 20)
combo1.set("English")

label1 = Label(root, text='English',font = 'segoe 30 bold', bg = 'white', width = 18, bd = 5, relief=GROOVE)
label1.place(x= 10, y = 50)

frame1 = Frame(root, bg = "Black", bd = 5)
frame1.place(x = 10, y = 110, width = 440, height= 210)

text1 = Text(frame1, font="Roboto 20", bg = 'white', relief=GROOVE, wrap = WORD)
text1.place(x=0, y=0, width =430, height = 200)

Scrollbar1 = Scrollbar(frame1)
# y is used in the last to spacify that it should fill up the vertical space
Scrollbar1.pack(side="right", fill = 'y')

Scrollbar1.configure(command=text1.yview)
text1.config(yscrollcommand= Scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14",state = 'r')
combo2.place(x = 730 , y = 20)
combo2.set('Selet Language')

label2 = Label(root, text='English', font='segoe 30 bold', bg = 'white', width = 18,bd = 5, relief = GROOVE)
label2.place(x = 620, y = 50)
 
frame2 = Frame(root, bg = "Black", bd = 5)
frame2.place(x =620 , y = 110, width= 440, height=210)

text2 = Text(frame2, font = "Robot 20", bg = "white", relief = GROOVE, wrap = WORD)
text2.place(x=0, y=0, width=430, height=200)

Scrollbar2 = Scrollbar(frame2)
Scrollbar2.pack(side = "right", fill = "y")

Scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=Scrollbar2.set)

# translate button
translate = Button(root,text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd = 5, bg = "red", fg = "white",command=translate_now)
translate.place(x =480, y=250)



label_change()

root.configure(bg = "white")
root.mainloop()