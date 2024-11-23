print()
print("## NOMOR 1 ##")
def celcius_ke_farenheit(celcius):
    konversi = (celcius*9/5)+32
    return konversi

print(celcius_ke_farenheit(0)) #32
print(celcius_ke_farenheit(100))

print()
print("## NOMOR 2 ##")
def ganjil_genap(bilangan):
    penentu=bilangan % 2 == 0
    return penentu

print(ganjil_genap(4)) #true
print(ganjil_genap(7)) #false

print()
print("## NOMOR 3 ##")
def nilai(keterangan):
    if keterangan >= 80:
        print("lulus")
    elif keterangan<= 60:
        print("tidak lulus")
    else :
        print("invalid")

nilai(80)
nilai(50)

print()
print("## NOMOR 4 ##")
def bilangan_ganjil(bilangan):
    return[ i for i in range (1,bilangan,2)]
print(bilangan_ganjil(20))