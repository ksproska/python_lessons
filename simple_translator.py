from calendar import month_name
from tkinter import *
from tkinter import ttk
from google_translator_simplified import Translator
from ponstrans import translate
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

sel_ang = StringVar()
en_cb = ttk.Combobox(window, textvariable = sel_ang)
en_cb.grid(column=0, row=2, sticky='ew')

def get_polish():
    textEn = text_en.get('1.0', END)
    translations = Translator.get_translation('pl', textEn, 'en')
    text_pl.delete('1.0', END)
    text_pl.insert(INSERT, translations)
    translations = translate(word=textEn, source_language='en', target_language='pl')
    translations = [t["target"] for t in translations]
    en_cb ['values'] = translations
    en_cb.focus_set()


def podmiana_polskiego(env=None):
    text_pl.delete('1.0', END)
    text_pl.insert(INSERT, sel_ang.get())
en_cb.bind('<<ComboboxSelected>>',podmiana_polskiego )


sel_pl = StringVar()
pl_cb = ttk.Combobox(window, textvariable = sel_pl)
pl_cb.grid(column=0, row=2, sticky='ew')

def get_english():
    textPl = text_pl.get ('1.0', END)
    translations = Translator.get_translation('en', textPl,'pl')
    text_en.delete('1.0', END)
    text_en.insert(INSERT, translations)
    translations = translate(word=textPl, source_language='pl', target_language='en')
    translations = [t['target'] for t in translations]
    pl_cb ['values'] = translations
    pl_cb.focus_set()

def podmiana_angielski(ekjrghflkghnv=None):
    text_en.delete('1.0', END)
    text_en.insert(INSERT, sel_pl.get())
pl_cb.bind('<<ComboboxSelected>>', podmiana_angielski)


def get_translate(evn=None):
    textEn = text_en.get('1.0', END)
    textPl = text_pl.get('1.0', END)
    if textEn != '\n' and textPl != '\n':
        save()
    elif textEn != '\n':
        get_polish()
    elif textPl != '\n':
        get_english()




# en_cb['values'] = [1, 3, 4, 5]


Button(frame, text="Tłumacz", command=get_translate, bg='#660066', fg='#ffffff').grid(column=0, row=3, sticky='ew')

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


Button(frame, text="Zapisz", command=save, bg='#800080', fg='#ffffff').grid(column=1, row=3, sticky='ew')
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
