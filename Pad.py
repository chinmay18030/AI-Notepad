
from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
from tkinter import messagebox
import datetime
import webbrowser
import wikipedia


wn = Tk()
wn.title("ATA Notepad")
edAr = Text(wn, borderwidth=3, width=170, height=100)
edAr.pack()
file_path = ""
path = ""
ext = ".txt"


def file_type(ex):
    global ext
    ext = ex


def save_file():
    global ext
    message = messagebox.askquestion(
        "Ace Tech", "Do you want to save this code?")
    if message == "yes":
        path = asksaveasfilename(filetypes=[("File specified", "*")])
        code = edAr.get("1.0", END)
        with open(path+ext, "w") as file:
            file.write(code)


def open_file():

    path = askopenfilename(filetypes=[("All Files","*")])

    with open(path, 'r') as file:
        code = file.read()
        edAr.delete('1.0', END)
        edAr.insert('1.0', code)
        set_file_path(path)


def set_file_path(path):
    global file_path
    file_path = path

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = edAr.get('1.0', END)
        file.write(code)
        set_file_path(path)
def clear_all():

    edAr.delete("1.0", END)


def date_add():
    x = datetime.datetime.now()
    text = edAr.get("1.0", END)
    edAr.delete("1.0",END)
    edAr.insert("1.0",text +  x.strftime("%D")+" " +
                x.strftime("%T")+" "+x.strftime("%p"))


def about():
    top = Toplevel()
    top.title("About")
    text = Text(top)
    text.insert("1.0", "Hello, whether you want to code, or write something, you can do it easily by ATC Notepad."
                "This note pad has been made to help all people. You can use the simple in-built features"
                "offered by the ATC Notepad app. For any queries contact atcComm@gmail.com")


def open_link():
    webbrowser.get(
        'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("www.bing.com")


def wiki():
    top = Toplevel()
    top.title("ATA Wikipedia Search")
    E = Entry(top)
    txt = Text(top)

    def pressed():
        src = wikipedia.summary(E.get())
        txt.insert("1.0", src)

    def insert():
        src = wikipedia.summary(E.get())
        edAr.insert("1.0", src)
    E.grid(row=0,column=0,columnspan=4)
    txt.grid(row=1,column=0)
    menu = Menu(top)
    option = Menu(menu)
    option.add_command(label="Search", command=pressed)
    option.add_command(label="Insert in Pad", command=insert)
    menu.add_cascade(label="Options", menu=option)

    top.config(menu=menu)


menu_bar = Menu(wn)

file = Menu(menu_bar, tearoff=0)
edit = Menu(menu_bar, tearoff=0)
about_bar = Menu(menu_bar, tearoff=0)
File_type = Menu(menu_bar, tearoff=0)
ai = Menu(menu_bar, tearoff=0)

file.add_command(label="Save as", command=save_as)
file.add_command(label="Open", command=open_file)
file.add_command(label="Save", command=save_as)


ai.add_command(label="Add Definition", command=wiki)

edit.add_command(label="Clear all", command=clear_all)
edit.add_command(label="Add Date and Time", command=date_add)
edit.add_separator()
edit.add_cascade(label="AI  ",menu=ai)


File_type.add_command(label=".txt",command=lambda: file_type(".txt"))
File_type.add_command(label=".pdf", command=lambda: file_type(".pdf"))
File_type.add_command(label=".py",command=lambda: file_type(".py"))
File_type.add_command(label=".js", command=lambda: file_type(".js"))
File_type.add_command(label=".c",command=lambda: file_type(".c"))
File_type.add_command(label=".cpp", command=lambda: file_type(".cpp"))
File_type.add_command(label=".html",command=lambda: file_type(".html"))
File_type.add_command(label=".css", command=lambda: file_type(".css"))
File_type.add_command(label=".php",command=lambda: file_type(".php"))
File_type.add_command(label=".docx",command=lambda: file_type(".docx"))
File_type.add_command(label=".csv", command=lambda: file_type(".csv"))
File_type.add_command(label=".json",command=lambda: file_type(".json"))
File_type.add_command(label=".java", command=lambda: file_type(".java"))
File_type.add_separator()

about_bar.add_command(label="ATA Notepad", command=about)
about_bar.add_command(label="Get More info", command=open_link)

menu_bar.add_cascade(label="File", menu=file)
menu_bar.add_cascade(label="Edit", menu=edit)
menu_bar.add_cascade(label="About", menu=about_bar)
menu_bar.add_cascade(label="File Type", menu=File_type)

wn.config(menu=menu_bar)

wn.mainloop()
