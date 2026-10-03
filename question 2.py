#Aguila, Daniel C CPE21S1
import tkinter as tk

def change_color():
    btn.config(bg="yellow")

root = tk.Tk()
root.title("Special Midterm Exam in OOP")
root.geometry("300x200")

btn = tk.Button(
    root,
    text="Click to Change Color",
    command=change_color
)
btn.pack(expand=True)

root.mainloop()