from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def get_info(self):
        pass

class BelfoldiJarat(Jarat):
    def get_info(self):
        return f"Belföldi járat: {self.jaratszam} - {self.celallomas}, Ár: {self.jegyar} Ft"

class NemzetkoziJarat(Jarat):
    def get_info(self):
        return f"Nemzetközi járat: {self.jaratszam} - {self.celallomas}, Ár: {self.jegyar} Ft"
