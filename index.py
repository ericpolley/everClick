import tkinter as tk


def button_00():
    print("Button clicked!")
    button.destroy()
    button1.place(relx=0.35, rely=0.5, anchor=tk.CENTER, command=button_01)
    button2.place(relx=0.5, rely=0.5, anchor=tk.CENTER, command=button_01)
    button3.place(relx=0.65, rely=0.5, anchor=tk.CENTER, command=button_01)


def button_01():
    print('button1Clicked !')
    button1.destroy()
    button2.destroy()
    button3.destroy()
    ending = tk.Text(window, text="The end")
    ending.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


window = tk.Tk()
window.title("Green Window")
window.geometry("800x600")
window.configure(bg="green")

button = tk.Button(window, text="Press Here", command=button_00)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
button1 = tk.Button(window, text="Button 1")
button2 = tk.Button(window, text="Button 2")
button3 = tk.Button(window, text="Button 3")

window.mainloop()
