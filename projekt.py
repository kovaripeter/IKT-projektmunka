def eladas():
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
            

        