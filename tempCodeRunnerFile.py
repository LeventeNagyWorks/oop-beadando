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
                
                while True:
                    try:
                        datum_obj = datetime.strptime(datum, "%Y-%m-%d")
                        if datum_obj < datetime.now():
                            print("A foglalás dátuma nem lehet korábbi, mint a mai nap!")
                            datum = input("Kérem, adjon meg egy új dátumot (ÉÉÉÉ-HH-NN): ")
                        else:
                            break
                    except ValueError:
                        print("Érvénytelen dátum formátum! Használja: ÉÉÉÉ-HH-NN")
                        datum = input("Kérem, adjon meg egy új dátumot (ÉÉÉÉ-HH-NN): ")
                
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
                print("\nÉrvénytelen választás!")