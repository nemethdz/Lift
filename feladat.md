# Gyakorlófeladat 2 – Liftteher

*Nehézség: ★★☆☆☆ – Digitális kultúra, középszintű érettségi programozási feladat szintje, Python nyelven.*

Egy irodaház liftjébe egyszerre 12 utas szeretne beszállni. Az utasok tömege kilogrammban az `utasok.txt` fájlban található:

```
72,85,64,91,58,103,77,69,88,95,60,81
```

Írjon programot, amely az alábbi feladatokat oldja meg!

1. Tárolja el a 12 utas tömegét egy megfelelő adatszerkezetben a program forráskódjában!
2. Kérje be a billentyűzetről a lift teherbírását kilogrammban (egész szám)! A bekérés előtt jelenjen meg a minta szerinti felirat!
3. Számítsa ki az utasok összes tömegét, majd döntse el, hogy mindenki elfér-e egyszerre a liftben! Az összes tömeg és a teherbírás egyenlősége esetén még elfér mindenki. Írja ki az összes tömeget, és hogy „Mindenki elfér.” vagy „Nem fér el mindenki.”!
4. Keresse meg az első olyan utast, aki 100 kg-nál nehezebb! Írja ki a sorszámát (1-től számozva) és a tömegét! Ha nincs ilyen utas, a „Nincs 100 kg feletti utas.” üzenetet írja ki!
5. **Leadás.** A megoldását **GitHubon keresztül** kell leadnia: töltse fel a `lift.py` fájlt egy GitHub repositoryba, majd a **repository URL-jét** (pl. `https://github.com/felhasznalonev/repository-neve`) töltse fel a **Google Classroom** megfelelő feladatához! Más módon (e-mail, pendrive, csatolt fájl) leadott megoldást nem fogadunk el.

**Minta a szöveges kimenet kialakításához** (a bemenet: `900`):

```
2. feladat: A lift teherbírása (kg): 900
3. feladat: Az összes tömeg 943 kg. Nem fér el mindenki.
4. feladat: Az első 100 kg feletti utas: 6. (103 kg)
```

Ha a teherbírás `1000`, a 3. feladat kimenete: `3. feladat: Az összes tömeg 943 kg. Mindenki elfér.`

## Általános tudnivalók

- A program forráskódját **`lift.py`** néven mentse!
- Az adatokat a program forráskódjában, **listában** tárolja. A(z) `utasok.txt` fájl tartalmát a kódba másolhatja, a programnak fájlt **nem** kell (és nem szabad) beolvasnia.
- A felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie.
- A programnak akkor is helyesen kell működnie, ha az adatokat a kódban kicseréljük (más elemszám, más értékek), ezért ne írjon a programba előre kiszámolt eredményt vagy az elemszámot rögzítő számot!
- A képernyőre írást igénylő feladatoknál az ékezet nélküli kiírás is elfogadott.
- A minta szerint írja ki a feladat sorszámát (pl. `2. feladat:`), majd a kiírt tartalomra utaló szöveget!
- A megjegyzésben (kommentben) elhelyezett kód vagy szöveg nem értékelhető.
- Ajánlott megoldási idő: **25 perc**. Összesen **15 pont** szerezhető.

