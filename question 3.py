#Aguila, Daniel C CPE21S1
import tkinter as tk

def show_name():
    txt2.delete(0, tk.END)
    txt2.insert(0, txt1.get())

root = tk.Tk()
root.title("Midterm in OOP")


lbl = tk.Label(root, text="Enter your fullname:", fg="red")
lbl.grid(row=0, column=0, padx=10, pady=10) # i used grid instead of place(x,y)

txt1 = tk.Entry(root)
txt1.grid(row=0, column=1, padx=10, pady=10)

btn = tk.Button(root, text="Click to display your Fullname", fg="red", command=show_name)
btn.grid(row=1, column=0, padx=10, pady=10)

txt2 = tk.Entry(root)
txt2.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()