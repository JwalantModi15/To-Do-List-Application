from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle
root = Tk()
root.title("To do List")
root.geometry("500x500")

# Creat frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Create listbox
my_list = Listbox(my_frame,
	font=("Arial",23,"bold"),
	width=25,
	height=8,
	bg="SystemButtonFace",
	bd=0,
	fg="#464646",
	highlightthickness=0,
	selectbackground="#a6a6a6",
	activestyle="none")

my_list.pack(side=LEFT, fill=BOTH)

# Create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)
s = StringVar()
# create entry box to add items to the list
my_entry = Entry(root, font=("Arial", 21),textvariable = s, width = 25)
my_entry.pack(pady=21)

# Create a button frame
button_frame = Frame(root)
button_frame.pack(pady=21)

# FUNCTIONS
def save_list():
    file_name = filedialog.asksaveasfilename(
        title = "Save File",
        filetypes = (("Dat File","*.dat"),("All Files","*.*"))
    )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f"{file_name}.dat"
        delete_cross()
        items = my_list.get(0,END)
        output_file = open(file_name,"wb")
        pickle.dump(items,output_file)

def open_list():
    file_name = filedialog.askopenfilename(
        title = "Open File",
        filetypes = (("Dat File","*.dat"),("All Files","*.*"))
    )
    if file_name:
        my_list.delete(0,END)
        input_file = open(file_name, "rb")
        items = pickle.load(input_file)
        for item in items:
            my_list.insert(END,item)
def delete_cross():
    count=0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count+=1     

def delete_item():
    try:
        my_list.delete(my_list.curselection())
    except Exception: 
        pass
      
def add_item():
    if s.get() != "":
        my_list.insert(END, s.get())
        s.set("")

def cross_off_item():
        try:
            my_list.itemconfig(my_list.curselection(),fg = "#dedede")
            my_list.selection_clear(0,END)
        except Exception:
            pass   
          
def uncross_item():
        try:
            my_list.itemconfig(my_list.curselection(),fg = "#464646")
            my_list.selection_clear(0,END)
        except Exception:
            pass 

def Clear():
    my_list.delete(0,END)

# Add some buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item, font = ("", 10))
add_button = Button(button_frame, text="Add Item", command=add_item, font = ("", 10))
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item, font = ("", 10))
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item, font = ("", 10))
delete_cross_button = Button(button_frame, text="Delete Cross", command=delete_cross, font = ("", 10))

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_cross_button.grid(row=0,column = 4)

my_menu = Menu(root)
save_menu = Menubutton(my_menu)
my_menu.add_cascade(label = "Save", menu = save_menu, command = save_list)
open_menu = Menubutton(my_menu)
my_menu.add_cascade(label = "Open", menu = open_menu, command = open_list)
clear_menu = Menubutton(my_menu)
my_menu.add_cascade(label = "Clear All", menu = clear_menu, command = Clear)
root.config(menu = my_menu)


root.mainloop()
