class Termek:
    def __init__(self,nev,ar,keszletmennyiseg):
        self.nev = nev
        self.ar= ar
        self.keszletmennyiseg = keszletmennyiseg
    def adatok(self):
        print(f"A termék neve:{self.nev}, ára: {self.ar}, készleten:{self.keszletmennyiseg} db.")

termek1 = Termek("Tej", 300, 30)
termek2 = Termek("Kenyér", 600,21)
termek3 = Termek("Alma",60,80)
keszlet = [termek1,termek2,termek3]
def adatokmentese(self):
        f = open("keszlet.txt", "w", encoding="utf-8")
        for termek in self.termekek:
            f.write(f"{termek['nev']},{termek['ar']},{termek['db']}\n")
            f.close()
def uj_termekfelvetel(self):
    print("\n--- Új termék felvétele ---")
    
    nev = input("Termék neve: ")
    
    try:
        ar = int(input("Ár (Ft): "))
        mennyiseg = int(input("Mennyiség (db): "))
        uj_elem = {
            "Termék": nev,
            "Ár": ar,
            "Mennyiség": mennyiseg
        }
        self.termekek.append(uj_elem)
        print(f"Sikeresen hozzáadva: {nev}")
        
        self.adatokmentese()

    except ValueError:
        print("Hiba: Az ár és a mennyiség csak szám lehet!")
bemenet = int(input("Válasszon műveletet (1-5): "))

while bemenet != 5:
    if bemenet == 1:
        pass
    elif bemenet == 2:
        pass
    elif bemenet == 3:
        pass
    elif bemenet == 4:
        pass
    bemenet = int(input("Válasszon műveletet (1-5): "))
    
