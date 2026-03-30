import tkinter as tk
def submit():
    value = entry.get()
    if value != "":
        new_label = tk.Label(screen, text=value)
        new_label.pack()
        print(f"user entered: {value}")
        submit_button.pack_forget()
    else:
        hello_label.config(text="you must enter a name to submit")

screen = tk.Tk()
screen.title("my tkinter app")
screen.geometry("600x600")

hello_label = tk.Label(screen, text="enter your full name below",padx=50,pady=50, bg="blue")
submit_button = tk.Button(screen, text="submit", command=submit, padx=20, pady=20)
entry = tk.Entry(screen)
# hello_label.grid(row=5, column=5, padx=50)
hello_label.pack(side="top")
entry.pack()
submit_button.pack(side="top")



screen.mainloop()