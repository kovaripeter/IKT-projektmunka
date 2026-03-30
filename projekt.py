def betoltes(fajl):
    betolt = termekek
    if betolt == True:
        termekek = open("raktar.txt", "w", encoding="utf-8")
        for sor in f:
            adatok = sor.strip().split(",")
            if len(adatok) == 3:
                nev, ar, mennyiseg = adatok
                termekek.append(Termek(nev, int(ar), int(mennyiseg)))
    else:
        termekek = []


def eladas(termekek):
    print("--- ELADÁS ---")
    nev = input("Melyik terméket vásárolták meg? ")

    for t in termekek:
        if t.nev == nev.lower():
            try:
                db = int(input("Hány darabot? "))
            except ValueError:
                print("[HIBA] Hibás mennyiség!")
                return
            
            if db > t.mennyiseg:
                print("[HIBA] Nincs elég készlet!")
                return

            t.mennyiseg -= db
            osszeg = db * t.ar

            print(f"[SIKER] Eladva: {db} db {t.nev}. Fizetendő: {osszeg} Ft.")
            print(f"(Új készlet: {t.mennyiseg} db)")

def kereses(termekek):
    print("--- KERESÉS ---")
    kereso = input("Keresett kifejezés: ")

    talalat = False
    for t in termekek:
        if kereso in t.nev():
            print(f"[TALÁLAT] {t.nev} - Ár: {t.ar} Ft, Készlet: {t.mennyiseg} db")
            talalat = True




fut = True
while fut:
    print("--- RAKTÁRKEZELŐ RENDSZER v1.0 ---\n[INFO] Adatok betöltése a 'raktar.txt' fájlból... OK.\n1. Készlet listázása\n2. Eladás (Készlet csökkentése)\n3. Új termék felvétele\n4. Termék keresése\n5. Mentés és Kilépés\n")

    bemenet = int(input("Válasszon műveletet (1-5): "))

    if bemenet == 1:
        listazas(termekek)
    elif bemenet == 2:
        uj_termek(termekek)
    elif bemenet == 3:
        eladas(termekek)
    elif bemenet == 4:
        kereses(termekek)
    elif bemenet == 5:
        fut = False  
        print("[INFO] Adatok mentése a 'raktar.txt' fájlba... KÉSZ.Viszontlátásra!")
        break
    else:
        print("[HIBA] Hibás választás!")



        