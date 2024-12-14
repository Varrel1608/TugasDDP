from classanimal import *

class Bird(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh
        
    def info_bird(self):
        super().info_animal()
        print("Warna \t\t\t:", self.warna,
              "\nJenis Paruh \t\t:", self.paruh,
              "\n========================")
        
# objek 1
BurungHantu = Bird("Burung Hantu", "Tikus", "Udara", "Bertelur", "Coklat", "Pendek")
BurungHantu.info_bird()

# objek 2
Bangau = Bird("Burung Bangau", "Serangga", "Rawa", "Bertelur", "Putih", "Panjang")
Bangau.info_bird()

# objek 3 
Kakatua = Bird("Kakatua", "Buah - buahan", "Pohon", "Bertelur", "Putih", "Bengkok")
Kakatua.info_bird()
