class JegyFoglalas:
    def __init__(self, jarat, datum, utas_nev):
        self.jarat = jarat
        self.datum = datum
        self.utas_nev = utas_nev

    def get_info(self):
        return f"{self.utas_nev} - {self.jarat.get_info()} - Dátum: {self.datum.strftime('%Y-%m-%d')}"
