class Termek:
        self.nev = nev
        self.ar = ar
        self.keszletmennyiseg = keszletmennyiseg
    def adatok(self):
        print(f"A termék neve:{self.nev}-----ára:{self.ar}-----készleten:{self.keszletmennyiseg}")

termekek = []
def uj_termek_felvetele(termek):
    uj = Termek(nev,ar,keszletmennyiseg)
    termekek.append(uj)
    termek(mentes)

def mentes(adatok):
    f = open("adatok.txt", "w", encoding="utf-8")
    f.write(str(adatok))
    f.close
print("Az adatok mentésre kerultek.")




        
    