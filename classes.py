import datetime


class Zwierze:
    # klasa jest to wzór przy pomocy którego możemy tworzyć obiekty
    # obiekt jest instancją danej klasy, to znaczy "fizycznie istniejączym obiektem"
    # klasą może być np zwierze, pies, kot
    # obiekt to np miś uszatek, kot filemon, pies reksio - "fizycznie istniejące"

    def __init__(self, imie: str, data_urodzenia: datetime.datetime):
        # to jest konstruktor - służy on do tworzenia nowych obiektów
        self.imie = imie
        # używając self inforujesz, że dana zmienna jest elementem klasy

        wartosc_tymczasowa = 10
        w2 = wartosc_tymczasowa + 20
        # brak znaku self oznacza, że dana zmienna jest tymczasowa, to znaczy, że nie możesz
        # się do niej odwoływać używając później obiektu
        self.data_urodzenia = data_urodzenia

    def odzew(self) -> str:
        # w ten spozób zadeklarowana metoda pozwala na nadpisanie jej w klasach dziedziczących
        # pass oznacza, że metoda sama w sobie nic nie robi
        pass

    def wiek(self):
        diff = datetime.datetime.now() - self.data_urodzenia
        return int(diff.days / 365.25)

    def __str__(self):
        # toString jest to metoda pozwalająca na stworzenie etykiety reprezentatywnej dla obiektu
        # przy braku tej metody przy wywołaniu print wyświetlony zostanie numer obiektu i jego klasa
        return f'{self.__class__.__name__}: {self.imie}'


class Kanarek(Zwierze):
    # nawiasy po kanarku oznaczają klasę po której dziedziczy kanarek
    # dziedziczenie obejmuje atrybuty i metody
    # oznacza to, że dzięki dziedziczeniu możemy rozszerzyć funkcjonalność klasy
    # np poprzez dodawanie kolejnych metod czy atrybutów

    def odzew(self) -> str:
        # to jest metoda zwracająca element, do tego używa się słowa return
        return 'świr świr'

    def __str__(self):
        # to jest przykład nadpisania metody
        # element super().nadpisywana_metoda() zwraca pierwotną wartość i dzięki temu możemy
        # rozszerzyć działanie poprzedniej metody
        return super().__str__() + f'; odzew: {self.odzew()}'


class Pies(Zwierze):
    def __init__(self, imie: str, data_urodzenia: datetime.datetime):
        # kolejny przykład nadpisywania metody, w tym przypadku przekazujemy atrybuty
        super().__init__(imie, data_urodzenia)
        self.szczepienia: list[str] = []

    def odzew(self) -> str:
        return 'hau hau'

    def dodaj_szczepienie(self, nazwa_choroby: str) -> None:
        # to jest metoda biorąca pewne argumenty
        self.szczepienia.append(nazwa_choroby)

    def wyswietl_szczepienia(self):
        # to jest metoda która nic nie zwraca, ale wyświetla szczepienia
        print(f'szczepienia dla {self.imie}: {self.szczepienia}')


if __name__ == '__main__':
    z = Pies('Burek', datetime.datetime(2002, 12, 1))
    print(z)
    print(z.wiek())
    print(z.odzew())
    z.dodaj_szczepienie('wścieklizna')
    z.dodaj_szczepienie('inna choroba - nie jestem ;)')
    z.wyswietl_szczepienia()

    k = Kanarek('Pierzak', datetime.datetime(2021, 1, 1))
    print(k)
    print(k.wiek())
    print(k.odzew())

