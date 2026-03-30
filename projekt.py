import os

class Termek:
    def __init__(self, nev, ar, mennyiseg):
        self.nev = nev
        self.ar = ar
        self.mennyiseg = mennyiseg

    def __str__(self):
        return f"{self.nev},{self.ar},{self.mennyiseg}"


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


def mentes(fajlnev, termekek):
    with open(fajlnev, "w", encoding="utf-8") as f:
        for t in termekek:
            f.write(str(t) + "\n")


def listazas(termekek):
    print("\n--- AKTUÁLIS KÉSZLET ---")
    print(f"{'Név':15} {'Ár (Ft)':10} {'Mennyiség'}")
    print("-" * 40)

    for t in termekek:
        print(f"{t.nev:15} {t.ar:<10} {t.mennyiseg}")

    print("-" * 40)
    print(f"Összesen: {len(termekek)} féle termék.\n")


def uj_termek(termekek):
    print("\n--- ÚJ TERMÉK FELVÉTELE ---")
    nev = input("Termék neve: ")

    try:
        ar = int(input("Egységár: "))
        if ar < 0:
            raise ValueError
    except:
        print("[HIBA] Az ár csak pozitív szám lehet!")
        return

    try:
        mennyiseg = int(input("Kezdőkészlet: "))
        if mennyiseg < 0:
            raise ValueError
    except:
        print("[HIBA] A mennyiség csak pozitív szám lehet!")
        return

    termekek.append(Termek(nev, ar, mennyiseg))
    print(f"[SIKER] '{nev}' hozzáadva.\n")


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


def eladas(termekek):
    print("\n--- ELADÁS ---")
    nev = input("Melyik terméket vásárolták meg? ")

    for t in termekek:
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


def main():
    fajlnev = "raktar.txt"

    print("--- RAKTÁRKEZELŐ RENDSZER v1.0 ---")
    print("[INFO] Betöltés...")

    termekek = betoltes(fajlnev)
    print("[OK]\n")

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
            uj_termek(termekek)
        elif valasztas == "3":
            eladas(termekek)
        elif valasztas == "4":
            kereses(termekek)
        elif valasztas == "5":
            print("\n[INFO] Mentés...")
            mentes(fajlnev, termekek)
            print("Viszontlátásra!")
            break
        else:
            print("[HIBA] Hibás választás!\n")


if __name__ == "__main__":
    main()