from classanimal import *

class Reptile(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_sisik, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_sisik = jenis_sisik
        self.habitat = habitat

    def info_reptil(self):
        super().info_animal()
        print("Jenis Sisik \t\t:", self.jenis_sisik,
              "\nHabitat \t\t:", self.habitat,
              "\n========================")

        
# objek 1
UlarPiton = Reptile("Ular Piton", "Tikus", "Darat", "Bertelur", "Halus", "Hutan Tropis")
UlarPiton.info_reptil()

# objek 2
Komodo = Reptile("Komodo", "Karnivora", "Darat", "Bertelur", "Kasar", "Savana/Hutan Tropis")
Komodo.info_reptil()

# objek 3 
Buaya = Reptile("Buaya", "Karnivora", "Air dan Darat", "Bertelur", "Keras dan Tebal", "Rawa/Sungai")
Buaya.info_reptil()
