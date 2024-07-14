from tkinter import *
from project import *
from PIL import ImageTk, Image # type: ignore

root = Tk()
root.geometry("600x400")
root.title("Phần mềm đẹp zai :))")
root.iconbitmap('youtube.ico')

# # Creating a Label Widget
# myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
# myLabel2 = Label(root, text="Xin chào cuộc đời :))").grid(row=1, column=10)
# # Shoving it onto the screen

# #myLabel1.grid(row=0, column=0)
# #myLabel2.grid(row=1, column=5)

row = 11
# column = 3
# # Configure grid to make the center cell expandable
# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)
# root.grid_rowconfigure(2, weight=1)
# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
# root.grid_columnconfigure(2, weight=1)
for i in range(row):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Create and place the input box (Entry) in the center of the grid
input_box = Entry(root, width=50, text="URL", font=('Arial', 12))
input_box.grid(row=3, column=5, padx=10, pady=10)

myLabel1 = Label(root, text="Hello World!", font=('Arial', 12)).grid(row=0, column=3, padx=10, pady=10)
root.mainloop()