class Animal:
    #konstruktor properti
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    #method informasi
    def info_animal(self):
        print("Nama Hewan \t: ", self.nama,
              "\nMakanan\t\t: ", self.makanan,
              "\nHidup\t\t: ", self.hidup,
              "\nBerkembang Biak\t: ", self.berkembang_biak)
# objek 1
kucing = Animal("Kucing", "Daging", "Darat", "Beranak\n")
kucing.info_animal()

# objek 2
Singa = Animal("Singa", "Daging", "Darat", "Beranak\n")
Singa.info_animal()

# objek 3
Gajah = Animal("Gajah", "Tumbuhan", "Darat", "Beranak\n")
Gajah.info_animal()


