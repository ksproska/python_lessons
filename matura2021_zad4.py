import string

def main():
    cale_slowo = ''

    with open("instrukcje.txt", 'r') as f:
        for polecenie in f:
            if polecenie.find("DOPISZ") >= 0:
                tabela_polecenia = polecenie.split(" ")
                litera = tabela_polecenia [1]
                cale_slowo = cale_slowo + litera[:-1]
            if polecenie.find("ZMIEN") >= 0:
                tabela_polecenia = polecenie.split(" ")
                litera = tabela_polecenia[1]
                cale_slowo = cale_slowo[:-1] + litera.replace('\n', '')
            if polecenie.find('USUN') >= 0:
                cale_slowo = cale_slowo[:-1]
            if polecenie.find('PRZESUN') >= 0:
                tabela_polecenia = polecenie.split(" ")
                stara_litera = tabela_polecenia[1][:-1]
                alfabet = string.ascii_uppercase + "A"
                inx_stara = alfabet.find(stara_litera)
                inx_nowa = inx_stara + 1
                nowa_litera = alfabet[inx_nowa]
                index=cale_slowo.find(stara_litera)
                # s[:index] + "X" + s[index + 1:]
                cale_slowo = cale_slowo[:index] + nowa_litera + cale_slowo[index + 1 :]

            print(f'{polecenie[:-1].ljust(12)}\t{cale_slowo}')

    print()
    print(len(cale_slowo))


if __name__ == '__main__':
    main()
