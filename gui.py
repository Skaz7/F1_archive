import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# windows size in pixels
window_width = 600
window_height = 440

screen_width = root.winfo_screenwidth()  # gets actual screen x resolution
screen_height = root.winfo_screenheight()  # gest actual screen y resolution

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
# root.resizable(False, False)
root.attributes('-alpha', 0.95)  # sets transparency
root.title("F1 Database")
# root.iconbitmap("F1icon.ico")

rec1 = tk.Frame(root, bg="#3d6466")
rec1.grid(row=0, column=0)  # creates additional Frame widget
rec1.pack()  # makes rec1 frame visible

photo = tk.PhotoImage(file="D:\\Users\\sebas\\OneDrive\\Repositories\\F1_archive\\assets\\f1photo.png")
label = tk.Label(root,
                 text="Classic Label",
                 compound="top",
                 font=("Helvetica", 12),
                 image=photo,
                 bg="#3d6466",  # background color
                 fg="#ff0")  # font color
label.pack(ipadx=10, ipady=10)  # displays label


def button_clicked():
    print("Button clicked")
    btn3.state(["!disabled"])  # makes button3 enabled


btn1 = ttk.Button(root, text="Activate", command=button_clicked)
btn1.pack()


def return_pressed(event):
    print("Return key pressed.")


def log(event):
    print(event)


btn2 = ttk.Button(root, text="Save")
btn2.bind("<Return>", return_pressed)
btn2.bind("<Return>", log, add="+")

btn2.focus()
btn2.pack(expand=True)


def callback():
    print(text)


download_icon = tk.PhotoImage(file="D:\\Users\\sebas\\OneDrive\\Repositories\\F1_archive\\assets\\download.png")
btn3 = ttk.Button(root, image=download_icon, text="Download", compound=tk.LEFT, command=callback)
btn3.state(["disabled"])
btn3.pack()

text = tk.StringVar()
textbox = ttk.Entry(root, textvariable=text)
textbox.pack()


root.mainloop()
