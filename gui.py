from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from photo import separate_images
import tkinter.font as TkFont
from PIL import Image, ImageTk

# create the root window
root = Tk()
root.title('Photo Digitizer')
root.resizable(False, False)
root.geometry("640x480")
root.configure(background="#444444")
frmMain = Frame(root, background="#444444")

helvB = TkFont.Font(family="Helvetica",size=11,weight="bold")
helvN = TkFont.Font(family="Helvetica",size=11)

def select_files():
    rows = rowEntry.get()
    cols = colEntry.get()
    if rows.isnumeric() and cols.isnumeric():
        filetypes = (
            ('Image Files', '*.jpg'),
            ('Image Files', '*.png'),
        )

        filenames = fd.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=filetypes)
        
        for file in filenames:
            separate_images(file, int(rows), int(cols))
    
    else:
        root.bell()
        messagebox.showerror("Error", "Enter number of rows and columns!") 

# Label
rowLabel = Label(frmMain, text="Enter the number of rows", font = helvB, bg="#444444", fg='white')
colLabel = Label(frmMain, text="Enter the number of columns", font = helvB, bg="#444444", fg='white')

# Entry for user input
rowEntry = Entry(frmMain, font=helvN, width=20)
colEntry = Entry(frmMain, font=helvN, width=20)

# open button
open_button = Button(
    frmMain,
    text='Select Files',
    command=select_files,
    font=helvN,
    justify='right',
    bg='gray',
    fg='white'
)

# Place label, entry, and button in grid
rowLabel.grid(row=0, column=0, pady=10, padx=30)
rowEntry.grid(row=0, column=1) 
colLabel.grid(row=1, column=0)
colEntry.grid(row=1, column=1) 
open_button.grid(row=2, column=1, pady=30, sticky='E')  
frmMain.grid(row=0, column=0, sticky="")
frmMain.grid_rowconfigure(0, weight=1)
frmMain.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()