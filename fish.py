from classanimal import *

class Fish(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernafas, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernafas = bernafas
        self.habitat = habitat
        
    def info_fish(self):
        super().info_animal()
        print("Bernafas Menggunakan \t:", self.bernafas,
              "\nJenis Air \t\t:", self.habitat,
              "\n========================")
        
# objek 1
ikan = Fish("Lumba-lumba", "Plankton", "Air", "Melahirkan", "Paru - Paru", "Asin")
ikan.info_fish()

# objek 2
paus = Fish("Paus", "Plankton", "Air", "Melahirkan", "Paru - Paru", "Asin")
paus.info_fish()

# objek 3
hiu = Fish("Hiu", "Karnivora", "Air", "Melahirkan", "Insang", "Asin")
hiu.info_fish()