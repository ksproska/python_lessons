# import names as
#
# get_name()

lista_duza = [[2, 4], [6], [3, 3, 3]]
dic = {}

lista_duza = sorted(lista_duza)
# print(lista_duza)

lista2 = [elemu * 2 for elemu in lista_duza]

lista_duza = lista_duza.sort(key=lambda element_listy_duzej: element_listy_duzej[0])

slownik = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(list(slownik.keys()))
keys = list(slownik.keys())
keys.sort(key=lambda klucz: slownik[klucz])

print(keys)
