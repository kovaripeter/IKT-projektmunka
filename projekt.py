import os

class Termek:
    def __init__(self,nev,ar,keszletmennyiseg):
        self.nev = nev
        self.ar= ar
        self.keszletmennyiseg = keszletmennyiseg

    def adatok(self):
        print(f"A termék neve:{self.nev}, ára: {self.ar}, készleten:{self.keszletmennyiseg} db.")

    def betoltes(fajlnev):
        termekek = []
        if not os.path.exists(fajlnev):
            return termekek

        with open(fajlnev, "r", encoding="utf-8") as f:
            for sor in f:
                adatok = sor.strip().split(",")
                if len(adatok) == 3:
                    nev, ar, mennyiseg = adatok
                    termekek.append(Termek(nev, int(ar), int(mennyiseg)))
        return termekek


    def adatokmentese(fajlnev, termekek):
        with open(fajlnev, "w", encoding="utf-8") as f:
            for t in termekek:
                f.write(str(t) + "\n")

    def listazas(termekek):
        print("\n--- AKTUÁLIS KÉSZLET ---")
        print(f"{'Név':15} {'Ár (Ft)':10} {'Mennyiség'}")
        print("-" * 40)

    def kereses(termekek):
        print("\n--- KERESÉS ---")
        kifejezes = input("Keresett kifejezés: ").lower()

        talalat = False
        for t in termekek:
            if kifejezes in t.nev.lower():
                print(f"[TALÁLAT] {t.nev} - Ár: {t.ar} Ft, Készlet: {t.mennyiseg} db")
                talalat = True

        if not talalat:
            print("[INFO] Nincs találat.")
        print()

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

    print("--- RAKTÁRKEZELŐ RENDSZER v1.0 ---\n[INFO] Adatok betöltése a 'raktar.txt' fájlból... OK.\n1. Készlet listázása\n2. Eladás (Készlet csökkentése)\n3. Új termék felvétele\n4. Termék keresése\n5. Mentés és Kilépés\n")

    def eladas(termekek):
        print("\n--- ELADÁS ---")
        nev = input("Melyik terméket vásárolták meg? ")
        for t in termekek():
            if t.nev.lower() == nev.lower():
                try:
                    db = int(input("Hány darabot? "))
                    if db <= 0:
                        raise ValueError
                except:
                    print("[HIBA] Hibás mennyiség!")
                    return

            if db > t.mennyiseg:
                print("[HIBA] Nincs elég készlet!\n")
                return

            t.mennyiseg -= db
            osszeg = db * t.ar

            print(f"[SIKER] Eladva: {db} db {t.nev}. Fizetendő: {osszeg} Ft.")
            print(f"(Új készlet: {t.mennyiseg} db)\n")
            return

    print("[HIBA] Nincs ilyen termék!\n")

    while True:
        print("1. Készlet listázása")
        print("2. Új termék felvétele")
        print("3. Eladás")
        print("4. Keresés")
        print("5. Mentés és Kilépés")

        valasztas = input("Válasszon (1-5): ")

        if valasztas == "1":
            listazas(termekek)
        elif valasztas == "2":
            uj_termekfelvetel(termekek)
        elif valasztas == "3":
            eladas(termekek)
        elif valasztas == "4":
            kereses(termekek)
        elif valasztas == "5":
            print("\n[INFO] Mentés...")
            adatokmentese(fajlnev, termekek)
            print("Viszontlátásra!")
            break
        else:
            print("[HIBA] Hibás választás!\n")