class Termek:
    def __init__(self,nev,ar,keszletmennyiseg):
        self.nev = nev
        self.ar= ar
        self.keszletmennyiseg = keszletmennyiseg
    def adatok(self):
        print(f"A termék neve:{self.nev}, ára: {self.ar}, készleten:{self.keszletmennyiseg} db.")

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
    
