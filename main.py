# python jest bardzo matematyczny:
def f(x):
    return 2 * x


# albo:
def g(x, y):
    return x ^ 2 + y + 10


# wartości w pythonie mogą być różnych typów:
a = 1  # int - liczba całkowita
b = 2.2  # float/dubble - zmiennoprzecinkowa
c = "tekst"  # string - ciąg znaków
d = True # boolean - wartości True lub False

# typów jest o wiele więcej, ale na początek starczy :)

# dla typów liczbowych mamy różne operacje matematyczne:
nazwa = 1 # przypisanie wartości
nazwa == 2 # porównanie wartości
nazwa = nazwa*2 + 15

# dla typów boolean najczęstrze operacje:
True and False # matematyczne i - obie wartości muszą być true
True or False  # matematyczne lub - jedna z wartości musi być true

# dla stringów jest wiele, wiele różnych operacji, przykładowe mogą być np:
text = "text"
text[0] # pierwsza litera tekstu
text.replace('t', 'u') # zamana wszyltkich t w tekście na
'jakies zdanie ze spacjami'.split(' ') # rozbija string na tablicę ['jakies', 'zdanie', 'ze', 'spacjami']

# jeśli chcemy wyświetlić element używamy funkcji print:
print(text)

# pętla for działa w ten sposób, że przechodzimy po odpowiednich elementach do końca:
for litera in text:
    print(litera)

for text2 in 'jakies zdanie ze spacjami'.split(' '):
    print(text2)

# zad 1: wypisz w konsoli tylko imona ludzi z poniższego stringa
tekst_ludzie = "Kamila-Sproska Szymon-Sproski Witek-Fracek"
