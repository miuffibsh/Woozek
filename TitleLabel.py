import tkinter as tki


class TitleLabel:

    def __init__(self, master):
        self.label = tki.Label(master, text="woozek", font=("Rosewood Std Regular", 45, "bold"),
                               bg='#e3d5ca')
        self.label.pack()
        self.label = tki.Label(master, text="wanted", font=("Rosewood Std Regular", 22), bg='#e3d5ca')
        self.label.pack()
