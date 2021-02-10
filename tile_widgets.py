import sys
import tkinter as tk
from tkinter import ttk 

class TileLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        super(TileLabel, self).__init__(*args, **kwargs)            
        self.configure(background="#4444AA", foreground="white", bd=-2)


class TileEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        super(TileEntry, self).__init__(*args, **kwargs)            
        self.configure(background="#9999FF", foreground="black", bd=-2,
        borderwidth=0, highlightthickness=0, relief=tk.FLAT)


class TileKnob(tk.Frame):
    def __init__(self, parent, name,  **kwargs):
        super(TileKnob, self).__init__(parent)
        self.configure(background="#4444AA", bd=-2)
        label = TileLabel(self, text=name)
        self.entry = TileEntry(self)
        # when we pack these into a frame with side='right'
        # it is the equivalent of "right justify" so the entries and labels line up 
        self.entry.pack(side='right')
        label.pack(side='right')


class TileButton(ttk.Button):
    def __init__(self, *args, **kwargs):
        style = ttk.Style()
        style.configure('W.TButton', foreground='#9999FF', background='#4444AA',
            fieldbackground='#4444AA', borderwidth=0, highlightthickness=0, relief=tk.FLAT)
        super(TileButton, self).__init__(*args, **kwargs, style='W.TButton',
            command=sys.exit)


if  __name__ == "__main__":
    root = tk.Tk()
    root.winfo_toplevel().title("Nifty")
    heading = TileLabel(root, text="Program Name")
    heading.configure(font=("Arial", 22))
    heading.pack(expand=True, fill='x')
    knob1 = TileKnob(root, "Foofers")
    knob1.pack(expand=True, fill='x')
    knob2 = TileKnob(root, "Banana")
    knob2.pack(expand=True, fill='x')
    button = TileButton(root, text="Exit")
    button.pack(expand=True, fill='x')
    button.bind(quit)
    root.mainloop()
