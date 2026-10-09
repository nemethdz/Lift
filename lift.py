utas = [72,85,64,91,58,103,77,69,88,95,60,81]

lift_teher = int(input("A lift teherbírása (kg): "))

osszegzes = 0
for tomeg in utas:
    osszegzes = osszegzes + tomeg

if osszegzes <= lift_teher:
    print(f"Az összes tömeg {osszegzes} kg. Mindenki elfér.")
else:
    print(f"Az összes tömeg {osszegzes} kg. Nem fér el mindenki.")

talalt = -1 
i = 0
while i < len(utas) and talalt== -1:
    if utas[i] > 100:
        talalt = i
    i = i + 1
if talalt != -1:
    print(f"Az első 100 kg feletti utas: {talalt + 1}. ({utas[talalt]} kg)")
else:
    print("Nincs 100 kg feletti utas.")