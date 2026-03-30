class Termek:
    def __init__(self, nev, ar, mennyiseg):
        self.nev = nev
        self.ar = ar
        self.mennyiseg = mennyiseg


def fajl_beolvasas():
    termekek = []
    f = open("keszlet.txt", "r")

    for sor in f:
        adatok = sor.strip().split(";")
        nev = adatok[0]
        ar = int(adatok[1])
        mennyiseg = int(adatok[2])

        t = Termek(nev, ar, mennyiseg)
        termekek.append(t)

    return termekek


def keszlet_kilistazasa(termekek):
    print("Nev\nAr\nMennyiseg")

    for t in termekek:
        print(t.nev, t.ar, t.mennyiseg)


def uj_termek(termekek):
    nev = input("Add meg a termek nevet: ")
    ar = int(input("Add meg az arat: "))
    mennyiseg = int(input("Add meg a mennyiseget: "))

    uj = Termek(nev, ar, mennyiseg)
    termekek.append(uj)


def mentes(termekek):
    f = open("keszlet.txt", "w")

    for t in termekek:
        f.write(t.nev + ";" + str(t.ar) + ";" + str(t.mennyiseg) + "\n")

    f.close()


def menu():
    print("1 - Keszlet kilistazasa")
    print("2 - Uj termek")
    print("3 - Kilepes")


def main():
    termekek = fajl_beolvasas()

    valasztas = ""

    while valasztas != "3":
        menu()
        valasztas = input("Valassz: ")

        if valasztas == "1":
            keszlet_kilistazasa(termekek)

        if valasztas == "2":
            uj_termek(termekek)
            mentes(termekek)

    mentes(termekek)
        
    def betoltes(fajl):
        betolt = termekek
        if betolt == True:
            f = open("raktar.txt", "w", encoding="utf-8")
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

    def mentes(fajl, termekek):
        pass

    def listazas(termekek):
        pass
    
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



        