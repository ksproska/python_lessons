# import zewnętrznych bibliotek
from tkinter import *
from tkinter import ttk

# tworzenie okna
window = Tk()
# tworzenie ramki do przechowywania zawartości
frame = ttk.Frame(window, padding=10)

# grid oznacza układ siatki, czyli w której kolumnie i rzędzie oraz szerokość i wyskokość (np 1-ego, kilu rzędów)
frame.grid()

# tekst nieedytowalny
ttk.Label(frame, text="Hello World!").grid(column=0, row=0)

# przycisk, naciśnięcie kończy program
ttk.Button(frame, text="Quit", command=window.destroy).grid(column=1, row=0)

# uruchamiamy przygotowane okno
window.mainloop()
