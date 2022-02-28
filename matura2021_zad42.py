def main():
    slownik = {"DOPISZ": 0, "ZMIEN": 0, 'USUN':0 , 'PRZESUN': 0}
    wszystke_typy = ["DOPISZ", "ZMIEN", 'USUN', 'PRZESUN']
    poprzednie_polecenie = ''
    licznik = 0
    with open("instrukcje.txt", 'r') as f:
        for polecenie in f:
            typ_polecenia = ""
            for typ in wszystke_typy:
                if polecenie.find(typ) >= 0:
                    typ_polecenia = typ

            if poprzednie_polecenie != typ_polecenia:
                if slownik[typ_polecenia] < licznik:
                    slownik[typ_polecenia] = licznik
                licznik = 1
            else:
                licznik += 1
            poprzednie_polecenie = typ_polecenia
    print(slownik)


if __name__ == '__main__':
    main()
