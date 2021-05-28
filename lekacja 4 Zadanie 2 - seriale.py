lista = ["1. Luis Miguel\n", "2. Riverdale\n", "3. SexEducation"]
print("Lista seriali : \n1.Luis Miguel \n2.Riverdale \n3.SexEducation")
print("Hej, jak masz na imie?")
imie = input()
print(imie, "jaki serial z listy chciałbyś obejrzeć?")
serial = input()
słownik = {"Luis Miguel": 9, "Riverdale": 8.5, "Sex Education": 9}
print("Średnia ocena serialu to", słownik[serial])
print("Jaki nowy serial chcesz dodać do listy? I jaką ocenę mu dajesz?")
nowy_serial = input()
print("Wszystkie pozycje", słownik, "najnowszy na liście -", nowy_serial)


