from datetime import datetime

class HariKemerdekaan:
    def __init__(self, nama_negara, tanggal_Kemerdekaan):
        self.nama_negara = nama_negara
        self.tanggal_Kemerdekaan = tanggal_Kemerdekaan

    def tentukan_hari(self):
        """ Mengembalikan hari dari tanggal merdeka """
        dafthari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
        tanggal = datetime.strptime(self.tanggal_Kemerdekaan, "%d-%m-%Y")
        nama_hari = dafthari[tanggal.weekday()]
        return nama_hari

try:
    bacafile = open("tugas.txt", "r")
    bacafile.readline() 
    for baris in bacafile:
        nama, tanggal = baris.strip().split(",")
        merdeka = HariKemerdekaan(nama, tanggal)
        
        print("Negara:", merdeka.nama_negara)
        print("Hari Kemerdekaan:", merdeka.tentukan_hari())
finally:
    bacafile.close()  
