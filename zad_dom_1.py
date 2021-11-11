# napisz funkcję która jako argument będzie brała text w postaci równania i zwracała jego wynik

# cz1
# pomyśl w jaki sposób z tekstu uzyskać tablicę w stylu: [2, '+', 20, '-', 3]
# gdzie znaki są typu str i liczby typu int
# podpowiedź: zobacz sobie w main.py jak dokonałaś podziału stringa: "Kamila-Sproska Szymon-Sproski Witek-Fracek"
# przykład utworzenia nowej tabeli i dodawania do niej elementów masz w: reading_file.py linijki 29 i 43, 47

# cz2
# zobacz sobie przykład "for i in range(5)" przedstawiony po niżej
# kolejne wartości i wynoszą od 0 do 4, możemy w ten sposób odwoływać się do kolejnych elementów tablicy
# mając już tablicę w stylu: [2, '+', 20, '-', 3] możemy utwożyć warunek:
# dotychczasowy_wynik = tablica[0]
# jeżeli tablica[i] jest równa '+' to wykonujemy: dotychczasowy_wynik += tablica[i+1]
# jeżeli tablica[i] jest równa '-' to wykonujemy: dotychczasowy_wynik -= tablica[i+1]
# i na samym końcu zwracamy dotychczasowy_wynik

def policz(text: str):
    return 0


if __name__ == '__main__':
    print("Działanie pętli for i in range(5)")
    for i in range(5):
        print(i)

    # przykładowe stringi:
    rownanie1 = "2+20"
    rownanie2 = "2+20-3"
    rownanie3 = "2+20-3+10-8"

    print("wyniki naszych równań jak na razie")
    print(policz(rownanie1))  # wynik ma być: 22
    print(policz(rownanie2))  # wynik ma być: 19
    print(policz(rownanie3))  # wynik ma być: 21
