def main():
    slownik={}
    with open("instrukcje.txt", 'r') as f:
        for polecenie in f:
            if polecenie.find("DOPISZ") >= 0:
                tabela_polecenia = polecenie.split(" ")
                litera = tabela_polecenia [1][:-1]
                if litera in slownik:
                    slownik[litera] = slownik[litera] + 1
                else:
                    slownik [litera] = 1

    litery = list(slownik.keys()) #["a", "b", ...]
    litery.sort(key=lambda litera: slownik[litera] )
    print(litery)
    print(slownik)


if __name__ == '__main__':
    slowo = 'kajak'
    print(slowo[::-1] == slowo)
    main()
