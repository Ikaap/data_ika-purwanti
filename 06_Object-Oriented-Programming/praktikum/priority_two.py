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
        return "Jenis Latihan\t\t: " + self.__jenis_latihan + "\n" + "Jadwal\t\t\t: " + self.__jadwal


class Yoga(KelasLatihan):
    def __init__(self, nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal, tingkat_kesulitan, posisi_yoga):
        super().__init__(nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal)
        self.__tingkat_kesulitan = tingkat_kesulitan
        self.__posisi_yoga = posisi_yoga
    
    def AturPosisiYoga(self, posisi):
        self.__posisi_yoga = posisi
        return "Posisi Yoga\t\t: " + self.__posisi_yoga
        
    
    def tampilkan_info(self):
        return "Tingkat kesulitan\t: " + self.__tingkat_kesulitan


class AngkatBeban(KelasLatihan):
    def __init__(self, nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal, berat_maksimum, berat_badan):
        super().__init__(nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal)
        self.__berat_maksimum = berat_maksimum
        self.__berat_badan = berat_badan
    
    def AturBeratBadan(self, bb):
        self.__berat_badan = bb
        return "Berat badan\t\t: " + self.__berat_badan + "kg"
    
    def tampilkan_info(self):
        return "Berat maksimum\t\t: " + str(self.__berat_maksimum) +"kg"

def pilih_kelas(jk):
    if jk == "1":
        print("\n-- Kelas Latihan Yoga --")
        print("--------------------------------")
        tingkat_kesulitan = input("Inputkan tingkat kesulitan\t: ")
        posisi = "-"
        data_kelas_yoga = Yoga(nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal, tingkat_kesulitan, posisi)
        print("--------------------------------")
        atur_posisi = input("Apakah anda ingin mengatur posisi yoga ? (Y/N) ")
        if atur_posisi.lower() == "y":
            posisi = input("Silakan input posisi yoga : ")
            data_kelas_yoga.AturPosisiYoga(posisi)
                        
        print("\nData berhasil diinput!")
        print("\n--------------------------------")
        print("Informasi Kelas Latihan Yoga")
        print("--------------------------------")
        print("Informasi Pelatih")
        print(data_pelatih.tampilkan_info())
        print("\nInformasi Detail Kelas Latihan Yoga")
        print(data_kelas.tampilkan_info())
        print(data_kelas_yoga.tampilkan_info())
        print(data_kelas_yoga.AturPosisiYoga(posisi))
                        
    elif jk == "2":
        print("\n-- Kelas Latihan Angkat Beban --")
        print("--------------------------------")
        berat_maksimum = int(input("Inputkan berat maksimum\t: "))
        bb = "-"
        data_kelas_angkat_beban = AngkatBeban(nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal, berat_maksimum, bb)
        print("--------------------------------")
        atur_bb = input("Apakah anda ingin mengatur berat badan ? (Y/N) ")
        if atur_bb.lower() == "y":
            bb = input("Silakan input berat badan : ")
            data_kelas_angkat_beban.AturBeratBadan(bb)
                            
        print("\nData berhasil diinput!")
        print("\n--------------------------------")
        print("Informasi Kelas Latihan Angkat Beban")
        print("--------------------------------")
        print("Informasi Pelatih")
        print(data_pelatih.tampilkan_info())
        print("\nInformasi Detail Kelas Latihan Yoga")
        print(data_kelas.tampilkan_info())
        print(data_kelas_angkat_beban.tampilkan_info())
        print(data_kelas_angkat_beban.AturBeratBadan(bb))
    
    else:
        print("Data yang anda inputkan tidak tersedia")  
    


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
            input_data_kelas = input("\nTambah data kelas latihan (Y/N) ? ")
            if input_data_kelas.lower() == 'y':
                while True:
                    print("------------------------------------")
                    print("Menu Input Data Kelas Latihan")
                    jenis_latihan = input("Inputkan jenis latihan\t: ")
                    jadwal = input("Inputkan jadwal\t\t: ")
                    data_kelas = KelasLatihan(nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal)
                    
                    print("\nInformasi Jenis Kelas")
                    print("1. Yoga")
                    print("2. Angkat Beban")
                    jenis_kelas = input("Inputkan jenis kelas latihan\t: ")
                    pilih_kelas(jenis_kelas)
                    
                    input_tambah_kelas = input("\nInput data kelas lagi (Y/N) ? ")
                    print("====================================")
                    if input_tambah_kelas == "y":
                        continue
                    else:
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
