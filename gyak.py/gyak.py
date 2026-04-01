class Auto:
    def __init__(self,tipus,fogyasztas):
        self.tipus = tipus
        self.fogyasztas = fogyasztas
autok = []

for i in range(3):
    tipus = input("Add meg az autó típúsát:")
    fogyasztas = float(input("Add meg a fogyasztását (l/100km)"))
    autok.append(Auto(tipus,fogyasztas))
    print()

for auto in autok:
    print(f"A(z) {auto.tipus} fogyasztása: {auto.fogyasztasa}")
ossz_fogy = sum(auto.fogyasztas for auto in autok)
atlag = ossz_fogy / len(autok)
print(f"\n Az autók átlagfogyasztása:{atlag} l/100km")

legkisebb_auto = [0]
for auto in autok:
    if auto.fogyasztas < legkisebb_auto.fogyasztas:
        legkisebb_auto = auto

f = open("legtakarekosabb.txt", "w",encoding = "utf-8")
f.write (f"Legtakarékosabb autó:{legkisebb_auto}- fogyasztása:{legkisebb_auto.fogyasztas} l/100km")

