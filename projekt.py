class Termek:
    def __init__(self,nev,ar,keszletmennyiseg):
        self.nev = nev
        self.ar= ar
        self.keszletmennyiseg = keszletmennyiseg
    def adatok(self):
        print(f"A termék neve:{self.nev}, ára: {self.ar}, készleten:{self.keszletmennyiseg} db.")

print("--- RAKTÁRKEZELŐ RENDSZER v1.0 ---\n[INFO] Adatok betöltése a 'raktar.txt' fájlból... OK.\n1. Készlet listázása\n2. Eladás (Készlet csökkentése)\n3. Új termék felvétele\n4. Termék keresése\n5. Mentés és Kilépés\n")
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
    
