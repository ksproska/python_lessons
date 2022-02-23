# import zewnętrznych bibliotek
from tkinter import *
from tkinter import ttk


def main():
    # tworzenie okna
    window = Tk()
    # tworzenie ramki do przechowywania zawartości
    frame = ttk.Frame(window, padding=10)

    # grid oznacza układ siatki, czyli w której kolumnie i rzędzie oraz szerokość i wyskokość (np 1-ego, kilu rzędów)
    frame.grid()

    # tekst edytowalny
    text: Text = Text(frame)
    text.config(height=2, width=4)
    text.grid(column=0, row=0, rowspan=2)
    text.insert(INSERT, 0)

    # funkcja zmieniająca text na liczbę o 1 większą
    def add_1():
        old_value = int(text.get('1.0', END))
        text.delete('1.0', END)
        text.insert(INSERT, old_value + 1)

    def sub_1():
        old_value = int(text.get('1.0', END))
        text.delete('1.0', END)
        text.insert(INSERT, old_value - 1)

    # przyciski, naciśnięcie dodaje/odejmuje 1
    ttk.Button(frame, text="+1", command=add_1).grid(column=1, row=0)
    ttk.Button(frame, text="-1", command=sub_1).grid(column=1, row=1)

    # uruchamiamy przygotowane okno
    window.mainloop()


if __name__ == '__main__':
    main()
