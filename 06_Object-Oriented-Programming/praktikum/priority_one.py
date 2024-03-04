# Program Sistem untuk mengelola aktivitas di sebuah pusat kebugaran

class Pelanggan:
    def __init__(self, nama, usia, id_pelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__id_pelanggan = id_pelanggan
    
    def get_nama_pelanggan(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama
        return self.__nama
    
    def get_usia_pelanggan(self):
        return self.__usia
    
    def set_usia(self, usia):
        self.__usia = usia
        return self.__usia
    
    def get_id_pelanggan(self):
        return self.__id_pelanggan
    
    def set_id_pelanggan(self, id_pelanggan):
        self.__id_pelanggan = id_pelanggan
        return self.__id_pelanggan
    
    def tampilkan_info(self):
        return "Nama\t\t: " + self.__nama + "\n" + "Usia\t\t: " + str(self.__usia) + " tahun\n" + "ID Pelanggan\t: " + self.__id_pelanggan


class Pelatih:
    def __init__(self, nama, spesialis, tahun_pengalaman):
        self.__nama = nama
        self.__spesialis = spesialis
        self.__tahun_pengalaman = tahun_pengalaman
        
    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama
        return self.__nama
    
    def get_spesialis(self):
        return self.__spesialis
    
    def set_spesialis(self, spesialis):
        self.__spesialis = spesialis
        return self.__spesialis
    
    def get_tahun_pengalaman(self):
        return self.__tahun_pengalaman
    
    def set_tahun_pengalaman(self, tahun_pengalaman):
        self.__tahun_pengalaman = tahun_pengalaman
        return self.__tahun_pengalaman
    
    def tampilkan_info(self):
        return "Nama\t\t\t: " + self.__nama + "\n" + "Spesialis\t\t: " + self.__spesialis + "\n" + "Tahun Pengalaman\t: " + str(self.__tahun_pengalaman) + " tahun"


class KelasLatihan(Pelatih):
    def __init__(self, nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal):
        super().__init__(nama, spesialis, tahun_pengalaman)
        self.__jenis_latihan = jenis_latihan
        self.__jadwal = jadwal
    
    def tampilkan_info(self):
        nama = self.get_nama()
        return "Jenis Latihan\t: " + self.__jenis_latihan + "\n" + "Jadwal\t\t: " + self.__jadwal


print("Sistem Pengelolaan Pusat Kebugaran")
print("====================================")
while True: 
    print("Pusat Informasi : ")
    print("1. Pelanggan")
    print("2. Pelatih dan Kelas Latihan")
    menu = input("Silakan input informasi yang ingin anda akses : ")
    if menu == "1":
        print("------------------------------------\n")
        print("-- Sistem Pengelolaan Data Pelanggan --")        
        data_pelanggan = Pelanggan("", 1, "")
        list_data_pelanggan = []
        while True:
            print("------------------------------------")
            print("Menu Input Data Pelanggan")
            nama = input("Inputkan nama pelanggan\t: ")
            umur = int(input("Inputkan umur pelanggan\t: "))
            id_pelanggan = input("Inputkan ID pelanggan\t: ")
            data_pelanggan.set_nama(nama)
            data_pelanggan.set_usia(umur)
            data_pelanggan.set_id_pelanggan(id_pelanggan)
            
            list_data_pelanggan.append(data_pelanggan.tampilkan_info())
            print("\nData berhasil diinput!")
            input_data_pelanggan = input("Tampilkan data pelanggan atau input data pelanggan lagi (1/2) ? ")
            print("====================================")
            if input_data_pelanggan == "1":
                print("Informasi Pelanggan")
                size = len(list_data_pelanggan)
                for i in range(size):
                    print(f"Data Pelanggan ke-{i+1} :")
                    print(list_data_pelanggan[i])
                    print()
            else:
                continue
                
            break
    elif menu == "2":
        print("------------------------------------\n")
        print("-- Sistem Pengelolaan Data Pelatih --")
        data_pelatih = Pelatih("","", 1)
        list_data_pelatih = []
        while True:
            print("------------------------------------")
            print("Menu Input Data Pelatih")
            nama = input("Inputkan nama pelatih\t\t: ")
            spesialis = input("Inputkan spesialis pelatih\t: ")
            tahun_pengalaman = int(input("Inputkan tahun pengalaman\t: "))
            data_pelatih.set_nama(nama)
            data_pelatih.set_spesialis(spesialis)
            data_pelatih.set_tahun_pengalaman(tahun_pengalaman)
            print("\nData berhasil diinput!")
            list_data_pelatih.append(data_pelatih.tampilkan_info())
                
            data_kelas = KelasLatihan("","",0,"","")
            list_data_kelas = []
            input_data_kelas = input("\nTambah data kelas latihan (Y/N) ? ")
            if input_data_kelas.lower() == 'y':
                while True:
                    print("------------------------------------")
                    print("Menu Input Data Kelas Latihan")
                    jenis_latihan = input("Inputkan jenis latihan\t: ")
                    jadwal = input("Inputkan jadwal\t\t: ")
                    data_kelas = KelasLatihan(nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal)
                    
                    print("\nData berhasil diinput!")
                    list_data_kelas.append(data_kelas.tampilkan_info())
                    input_tambah_kelas = input("\nTampilkan data kelas latihan atau input data kelas lagi (1/2) ? ")
                    print("====================================")
                    if input_tambah_kelas == "1":
                        print("Informasi Kelas Latihan")
                        print("------------------------------------")
                        print("Data Pelatih")
                        print(data_pelatih.tampilkan_info())
                        print("\nData Kelas Latihan : ")
                        size = len(list_data_kelas)
                        for i in range(size):
                            print(f"Ke-{i+1} :")
                            print(list_data_kelas[i])
                            print()
                    else:
                        continue
                    break
            else:
                tambah_data_pelatih = input("Tambah data pelatih ? (Y/N)")
                if tambah_data_pelatih.lower() == 'y':
                    continue
                tampil_data_pelatih = input("Tampilkan semua data pelatih ? (Y/N)")
                if tampil_data_pelatih.lower() == 'y':
                    print("\nInformasi Data Pelatih")
                    size = len(list_data_pelatih)
                    print(f"jumlah pelatih : ", size)
                    for i in range(size):
                        print(f"Ke-{i+1} :")
                        print(list_data_pelatih[i])
                        print()
            break
                
    else:
        print("Data yang anda inputkan tidak valid!")
        ulang = input("Ingin input ulang (Y/N) ? ")
        print("\n====================================")
        if ulang.lower() != 'y':
            print(f"\t-- Terima Kasih --".upper())
            break
        else:
            continue
    
    ulang = input("Keluar dari program (Y/N) ? ")
    print("\n====================================")
    if ulang.lower() == 'y':
        print(f"\t-- Terima Kasih --".upper())
        break
    else:
        continue

