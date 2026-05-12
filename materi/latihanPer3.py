class Person:
    def __init__(self, nama, jenisKelamin, umur):
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.umur = umur


class Karyawan(Person):
    def __init__(self, nama, jenisKelamin, umur, gaji):
        super().__init__(nama, jenisKelamin, umur) 
        self.__gaji = gaji   


    def get_gaji(self):
        print("Mengambil gaji...")
        return self.__gaji

    
    def set_gaji(self, gajiBaru):
        print("Mengubah gaji...")
        self.__gaji = gajiBaru


class Rekening:
    def __init__(self, noRekening, pin):
        self.noRekening = noRekening
        self.__pin = pin 

    def cek_pin(self):
        return self.__pin



m1 = Person("Adit", "Laki-laki", 12)
k1 = Karyawan("Budi", "Laki-laki", 25, 2000)
r1 = Rekening("12345678", 1234)


print("Nama karyawan:", k1.nama)
print("Gaji:", k1.get_gaji())

k1.set_gaji(3000)
print("Gaji baru:", k1.get_gaji())

print("No rekening:", r1.noRekening)



    


