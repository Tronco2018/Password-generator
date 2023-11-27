import random
import string
import tkinter as tk
import pyperclip

# Creazione della finestra
win = tk.Tk()
win.geometry("300x300")
win.title("Password generator")

#fonts
title_font = ("Arial", 20, "bold")
password_font = ("Arial", 15)

# Funzione per generare la password
def generator():
    a = random.randint(0, 10)
    b = random.choice(string.ascii_lowercase)
    c = random.choice(string.ascii_uppercase)
    d = random.randint(0, 20)
    e = random.randint(7, 99)
    f = random.choice(string.punctuation)
    g = random.choice(string.punctuation)
    h = random.choice(string.digits)
    i = random.choice(string.punctuation)

    # Creazione della password
    password = str(a) + b + c + str(d) + str(e) + f + g + h + i
    password_label.config(text=password)
    pyperclip.copy(password)

# Creazione dell'etichetta del titolo
title = tk.Label(win, text="Password generator", font=title_font)
title.pack()

# Creazione del pulsante per generare la password
generate_button = tk.Button(win, text="Generate Password", command=generator)
generate_button.place(x="70", y="50")

#password label
password_label = tk.Label(win, text="", font=password_font)
password_label.place(x="80", y="80")

# Avvio del loop principale della finestra
win.mainloop()
