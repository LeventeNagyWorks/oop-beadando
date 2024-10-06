from datetime import datetime, timedelta
from legi_tarsasag import LegiTarsasag
from jarat import BelfoldiJarat, NemzetkoziJarat
from jegy_foglalas import JegyFoglalas

class FoglalasiRendszer:

    vonal = "--------------------------------------------------------------------------------------------------------"

    def __init__(self):
        self.legi_tarsasag = None
        self.foglalasok = []

    def inicializalas(self):
        self.legi_tarsasag = LegiTarsasag("Magyar Légitársaság")
        self.legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("BUD001", "Debrecen", 15000))
        self.legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("BUD002", "Szeged", 12000))
        self.legi_tarsasag.jarat_hozzaadasa(NemzetkoziJarat("BUD003", "London", 50000))

        ma = datetime.now()
        self.jegy_foglalas("BUD001", (ma + timedelta(days=1)).strftime("%Y-%m-%d"), "Kiss János")
        self.jegy_foglalas("BUD002", (ma + timedelta(days=2)).strftime("%Y-%m-%d"), "Nagy Éva")
        self.jegy_foglalas("BUD003", (ma + timedelta(days=3)).strftime("%Y-%m-%d"), "Szabó Péter")
        self.jegy_foglalas("BUD001", (ma + timedelta(days=4)).strftime("%Y-%m-%d"), "Kovács Anna")
        self.jegy_foglalas("BUD002", (ma + timedelta(days=5)).strftime("%Y-%m-%d"), "Tóth Gábor")
        self.jegy_foglalas("BUD003", (ma + timedelta(days=6)).strftime("%Y-%m-%d"), "Horváth Katalin")

    def jegy_foglalas(self, jaratszam, datum_str, utas_nev):
        jarat = self.legi_tarsasag.jarat_keresese(jaratszam)
        if not jarat:
            print("Érvénytelen járatszám!")
            return

        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
        except ValueError:
            print("Érvénytelen dátum formátum! Használja: ÉÉÉÉ-HH-NN")
            return

        if datum < datetime.now():
            print("A foglalás dátuma nem lehet korábbi, mint a mai nap!")
            return

        foglalas = JegyFoglalas(jarat, datum, utas_nev)
        self.foglalasok.append(foglalas)
        print(f"Foglalás sikeres! Ár: {jarat.jegyar} Ft")

    def foglalas_lemondasa(self, index):
        if 0 <= index < len(self.foglalasok):
            del self.foglalasok[index]
            print("Foglalás sikeresen lemondva!")
        else:
            print("Érvénytelen foglalási index!")

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincsenek foglalások.")
        else:
            for i, foglalas in enumerate(self.foglalasok):
                print(f"{i + 1}. {foglalas.get_info()}")

    def futtatas(self):
        while True:
            print(f"\n{self.vonal}")
            print("\n1. Jegy foglalása")
            print("2. Foglalás lemondása")
            print("3. Foglalások listázása")
            print("4. Kilépés")
            
            valasztas = input("\nVálasszon egy műveletet (1-4): ")
            
            if valasztas == "1":
                jaratszam = input("Adja meg a járatszámot: ")
                datum = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN): ")
                utas_nev = input("Adja meg az utas nevét: ")
                self.jegy_foglalas(jaratszam, datum, utas_nev)
            elif valasztas == "2":
                self.foglalasok_listazasa()
                index = int(input("Adja meg a lemondani kívánt foglalás sorszámát: ")) - 1
                self.foglalas_lemondasa(index)
            elif valasztas == "3":
                self.foglalasok_listazasa()
            elif valasztas == "4":
                print("Viszontlátásra!")
                break
            else:
                print("Érvénytelen választás!")
