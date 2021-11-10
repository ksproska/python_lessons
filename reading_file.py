class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __str__(self):
        # return self.imie + ' ' + self.nazwisko + ' - ' + str(self.wiek)
        return f'{self.nazwisko} {self.imie} = {self.wiek}'

class Pracownik(Osoba):
    pass

class Student(Osoba):
    def __init__(self, imie, nazwisko, wiek, index):
        super(Student, self).__init__(imie, nazwisko, wiek)
        self.index = index

    def __str__(self):
        # return f'{self.imie} {self.nazwisko} - {self.wiek} * {self.index}'
        return super(Student, self).__str__() + f' * {self.index}'






if __name__ == '__main__':
    ludki = []

    with open("ludzie.txt", 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            # print(line)
            nasza_osoba = line.split('\t')
            wiek=nasza_osoba[3]
            wiek=int(wiek)
            nasza_osoba[3]=wiek
            # print(nasza_osoba)
            if nasza_osoba[0]=='p':
                pracownik=Pracownik(nasza_osoba[1], nasza_osoba[2], nasza_osoba[3])
                # print(pracownik)
                ludki.append(pracownik)
            if nasza_osoba[0]=='s':
                student=Student(nasza_osoba[1], nasza_osoba[2], nasza_osoba[3], nasza_osoba[4])
                # print(student)
                ludki.append(student)

    # print(ludki)
    for ludek in ludki:
        if ludek.wiek > 25 and len(ludek.imie) > 6 :
            print(ludek)

