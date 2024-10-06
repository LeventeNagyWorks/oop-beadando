class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadasa(self, jarat):
        self.jaratok.append(jarat)

    def jarat_keresese(self, jaratszam):
        return next((jarat for jarat in self.jaratok if jarat.jaratszam == jaratszam), None)
