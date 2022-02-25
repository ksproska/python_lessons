przykład_tekstu = """
    Litwo! Ojczyzno moja! ty jesteś jak zdrowie:
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.
"""
print("\nPodział po spacji:")
print(przykład_tekstu.split(" "))

print("\nPodział po kropce:")
print(przykład_tekstu.split("."))

print("\nPodział po enterze:")
print(przykład_tekstu.split("\n"))

print("\nPodmiana fragmentu:")
print(przykład_tekstu.replace("Litwo", "Polsko"))

print("\nSprawdź czy zawiera:")
print(przykład_tekstu.find("ty"))
print(przykład_tekstu.find("cokolwiek innego"))

print("\nWielkie litery:")
print(przykład_tekstu.upper())

print("\nMałe litery:")
print(przykład_tekstu.lower())

print("\nCo druga litera:")
print(przykład_tekstu[::2])

index = 7
print(f"\nPodmiana znaku o indeksie {index}:")
s = przykład_tekstu
s = s[:index] + "X" + s[index + 1:]
print(s)

print("\nTekst bez ostatnich 2 znaków:")
print(przykład_tekstu[:-3])
