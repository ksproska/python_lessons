from tkinter import *
from google_translator_simplified import Translator
window = Tk()
window.title('Pierwszy program Agaty')
frame = Frame(window)
frame.grid()
text_pl = Text(frame)
text_en = Text(frame)
text_pl.grid(column=1, row=1)
text_pl.config(height=3, width=50)
text_en.grid(column=0, row=1)
text_en.config(height=3, width=50)

def get_polish():
    textEn = text_en.get('1.0', END)
    translation = Translator.get_translation('pl', textEn, 'en')
    text_pl.delete('1.0', END)
    text_pl.insert(INSERT, translation)

def get_english():
    textPl = text_pl.get ('1.0', END)
    translation = Translator.get_translation('en', textPl,'pl')
    text_en.delete('1.0', END)
    text_en.insert(INSERT, translation)

def get_translate(evn=None):
    textEn = text_en.get('1.0', END)
    textPl = text_pl.get('1.0', END)
    if textEn != '\n':
        get_polish()
    elif textPl != '\n':
        get_english()


Button(frame, text="Tłumacz", command=get_translate, bg='#660066', fg='#ffffff').grid(column=0, row=2, sticky='ew')

def save(evn=None):
    textEn=text_en.get('1.0', END)
    textPl=text_pl.get('1.0', END)

    if textPl != '\n' and textEn != '\n':
        text =textEn + ' - ' + textPl
        text=text.replace("\n",'')
        text=text + '\n'

        with open ('tłumaczenia.txt', 'a', encoding='utf8') as f:
            f.write(text)
        text_en.delete('1.0',END)
        text_pl.delete('1.0',END)


Button(frame, text="Zapisz", command=save, bg='#800080', fg='#ffffff').grid(column=1, row=2, sticky='ew')
window.bind('<Return>', get_translate)
window.bind('<Control-s>', save)

# def change_focus(evn=None):
#     widget=window.focus_get()
#     print(widget)
#     if widget == text_en:
#         text_pl.focus_set()
#     elif widget ==text_pl:
#         text_en.focus_set()
#     else:
#         text_en.focus_set()

# window.bind('<Tab>', change_focus)

Label(frame, text='Angielski', bg='#660066', fg='#ffffff').grid(column=0, row=0, sticky='ew')
Label(frame, text='Polski', bg='#800080', fg='#ffffff').grid(column=1, row=0, sticky='ew')

window.mainloop()
