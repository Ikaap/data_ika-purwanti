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
        self.jumlah_sesi = 0
    
    def tampilkan_info(self):
        return "Jenis Latihan\t\t: " + self.__jenis_latihan + "\n" + "Jadwal\t\t\t: " + self.__jadwal
    
    def pesan_kelas(self, jumlah_sesi):
        self.jumlah_sesi += jumlah_sesi
        print("Pemesanan kelas berhasil!")
    
    def batalkan_kelas(self, jumlah_sesi):
        if jumlah_sesi > 0:
            print("Pembatalan kelas berhasil!")
        
        


class Yoga(KelasLatihan):
    def __init__(self, nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal, tingkat_kesulitan, posisi_yoga):
        super().__init__(nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal)
        self.__tingkat_kesulitan = tingkat_kesulitan
        self.__posisi_yoga = posisi_yoga
        self.__harga_per_sesi = 75000
    
    def AturPosisiYoga(self, posisi):
        self.__posisi_yoga = posisi
        return "Posisi Yoga\t\t: " + self.__posisi_yoga
        
    
    def tampilkan_info(self):
        return "Tingkat kesulitan\t: " + self.__tingkat_kesulitan
    
    def pesan_kelas(self, jumlah_sesi, bayar, usia):
        if jumlah_sesi >= 1 and usia >= 4:
            super().pesan_kelas(jumlah_sesi)
            bayar = jumlah_sesi * self.__harga_per_sesi
        else:
            print("Maaf, pemenasan kelas yoga tersedia untuk pelanggan yang memesan lebih dari 1 kali sesi")
        return bayar
    
    def batalkan_kelas(self, jumlah_sesi):
        if  jumlah_sesi >= 1:
            super().batalkan_kelas(jumlah_sesi)
        else:
            print("Maaf, pembatalan kelas yoga tersedia untuk pelanggan yang telah memesan lebih dari 1 kali sesi")
        

class AngkatBeban(KelasLatihan):
    def __init__(self, nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal, berat_maksimum, berat_badan):
        super().__init__(nama, spesialis, tahun_pengalaman, jenis_latihan, jadwal)
        self.__berat_maksimum = berat_maksimum
        self.__berat_badan = berat_badan
        self.harga_per_sesi = 100000
    
    def AturBeratBadan(self, bb):
        self.__berat_badan = bb
        return "Berat badan\t\t: " + self.__berat_badan + "kg"
    
    def tampilkan_info(self):
        return "Berat maksimum\t\t: " + str(self.__berat_maksimum) +"kg"
    
    def pesan_kelas(self, jumlah_sesi, bayar):
        if jumlah_sesi >= 1 and self.__berat_maksimum >= 20:
            super().pesan_kelas(jumlah_sesi)
            bayar = jumlah_sesi * self.harga_per_sesi
        else:
            print("Maaf, pemesanan kelas angkat beban tersedia untuk pelanggan yang memiliki berat badan minimum 30kg")
        return bayar
    
    def batalkan_kelas(self, jumlah_sesi):
        if  jumlah_sesi >= 1:
            super().batalkan_kelas(jumlah_sesi)
        else:
            print("Maaf, pembatalan kelas angkat beban tersedia untuk pelanggan yang telah memesan setidaknya 1 sesi")


print("Sistem Pemesanan Pusat Kebugaran")
print("====================================")
while True: 
    print("Pusat Informasi Kelas Latihan: ")
    print("1. Yoga")
    print("2. Angkat Beban")
    menu = input("Silakan pilih informasi yang ingin anda akses : ")
    data_pelatih_satu = Pelatih("Ika","Yoga", 3)
    data_pelatih_dua = Pelatih("Bopu","Angkat Beban", 5)
    data_pelatih_tiga = Pelatih("Chelly","Senam", 2)
    list_data_pelatih = [data_pelatih_satu.tampilkan_info(), data_pelatih_dua.tampilkan_info(), data_pelatih_tiga.tampilkan_info()]
    print("------------------------------------")
    print("-- Informasi Data Pelatih --")    
    print("------------------------------------\n")
    size = len(list_data_pelatih)
    for i in range(size):
        print(f"Ke-{i+1} :")
        print(list_data_pelatih[i])
        print("-----------------")
    if menu == "1":
        data_pelanggan = Pelanggan("", 1, "")
        print("\n------------------------------------")
        print("-- Pemesanan Kelas Latihan Yoga --")    
        print("------------------------------------\n")  
        print("Informasi Data Pelanggan")
        nama = input("Inputkan nama\t: ")
        umur = int(input("Inputkan umur\t: "))
        id_pelanggan = input("Inputkan ID\t: ")
        data_pelanggan.set_nama(nama)
        data_pelanggan.set_usia(umur)
        data_pelanggan.set_id_pelanggan(id_pelanggan) 
        print("\nData berhasil diinput!")
        
        print("------------------------------------\n")  
        print("Informasi Data Pelatih")
        pilih_pelatih = input("Pilih pelatih (1/2/3)\t: ")
        print("\nData berhasil diinput!\n")
        
        print("Informasi Kelas Latihan Yoga")
        print("Harga Kelas Latihan Yoga = Rp. 75.000/sesi")
        print("------------------------------------")  
        jumlah_sesi = int(input("Inputkan jumlah sesi\t\t: "))
        jenis_latihan = input("Inputkan jenis latihan\t\t: ")
        jadwal = input("Inputkan jadwal\t\t\t: ")
        tingkat_kesulitan = input("Inputkan tingkat kesulitan\t: ")
        posisi = "-"
        print("--------------------------------")
        if pilih_pelatih == "1":
            data_kelas = KelasLatihan("Ika", "Yoga", 3, jenis_latihan, jadwal)
            data_kelas_yoga = Yoga("Ika", "Yoga", 3, jenis_latihan, jadwal, tingkat_kesulitan, posisi)
        elif pilih_pelatih == "2":
            data_kelas = KelasLatihan("Bopu", "Angkat Beban", 5, jenis_latihan, jadwal)
            data_kelas_yoga = Yoga("Bopu", "Angkat Beban", 5, jenis_latihan, jadwal, tingkat_kesulitan, posisi)
        elif pilih_pelatih =="3":
            data_kelas = KelasLatihan("Chelly", "Senam", 2, jenis_latihan, jadwal)
            data_kelas_yoga = Yoga("Chelly", "Senam", 2, jenis_latihan, jadwal, tingkat_kesulitan, posisi)
        else:
            print("Data pelatih tidak tersedia")
            
        atur_posisi = input("Apakah anda ingin mengatur posisi yoga ? (Y/N) ")
        if atur_posisi.lower() == "y":
            posisi = input("Silakan input posisi yoga : ")
            data_kelas_yoga.AturPosisiYoga(posisi)
            print("\nData berhasil diinput!")
            print("--------------------------------\n")
            
        if umur >= 4 :
            data_kelas_yoga.pesan_kelas(jumlah_sesi, jumlah_sesi*75000, umur)
            print("------------------------------------")
            print(f"Anda melakukan pesan kelas latihan untuk {jumlah_sesi} sesi")
            print("Total Tagihan : ", jumlah_sesi*75000)
            print("------------------------------------")
            print("Selamat anda berhasil melakukan pemesanan pada kelas latihan Yoga!")
            print("====================================================================")
            
            pilihan = input("Keluar Program atau Batalkan Kelas Latihan (1/2) ? ")
            if pilihan == "2":
                data_kelas_yoga.batalkan_kelas(jumlah_sesi)
                print("------------------------------------\n")
        else :
            print("------------------------------------")
            print("Maaf usia anda tidak cukup untuk pesan kelas latihan yoga!")
            print("====================================================================")
            
    elif menu == "2":
        data_pelanggan = Pelanggan("", 1, "")
        print("------------------------------------")
        print("-- Pemesanan Kelas Latihan Angkat Beban --")    
        print("------------------------------------\n")  
        print("Informasi Data Pelanggan")
        nama = input("Inputkan nama\t: ")
        umur = int(input("Inputkan umur\t: "))
        id_pelanggan = input("Inputkan ID\t: ")
        data_pelanggan.set_nama(nama)
        data_pelanggan.set_usia(umur)
        data_pelanggan.set_id_pelanggan(id_pelanggan) 
        print("\nData berhasil diinput!")
        print("------------------------------------\n")  
        print("Informasi Data Pelatih")
        pilih_pelatih = input("Pilih pelatih\t: ")
        print("\nData berhasil diinput!\n") 
        print("Informasi Kelas Latihan Angkat Beban")
        print("Harga Kelas Latihan Angkat Beban = Rp. 100.000/sesi")
        print("------------------------------------")  
        jumlah_sesi = int(input("Inputkan jumlah sesi\t: "))
        jenis_latihan = input("Inputkan jenis latihan\t: ")
        jadwal = input("Inputkan jadwal\t\t: ")
        berat_maksimum = int(input("Inputkan berat maksimum\t: "))
        bb = "-"
        print("--------------------------------")
        if pilih_pelatih == "1":
            data_kelas = KelasLatihan("Ika", "Yoga", 3, jenis_latihan, jadwal)
            data_kelas_angkat_beban = AngkatBeban("Ika", "Yoga", 3, jenis_latihan, jadwal, berat_maksimum, bb)
        elif pilih_pelatih == "2":
            data_kelas = KelasLatihan("Bopu", "Angkat Beban", 5, jenis_latihan, jadwal)
            data_kelas_angkat_beban = AngkatBeban("Bopu", "Angkat Beban", 5, jenis_latihan, jadwal, berat_maksimum, bb)
        elif pilih_pelatih == "3":
            data_kelas = KelasLatihan("Chelly", "Senam", 2, jenis_latihan, jadwal)
            data_kelas_angkat_beban = AngkatBeban("Chelly", "Senam", 2,  jenis_latihan, jadwal, berat_maksimum, bb)
        else:
            print("Data pelatih tidak tersedia")
        
        atur_bb = input("Apakah anda ingin mengatur berat badan ? (Y/N) ")
        if atur_bb.lower() == "y":
            bb = input("Silakan input berat badan : ")
            data_kelas_angkat_beban.AturBeratBadan(bb) 
            print("\nData berhasil diinput!")
            print("--------------------------------\n")
            
        if berat_maksimum >= 20:
            data_kelas_angkat_beban.pesan_kelas(jumlah_sesi, jumlah_sesi*100000)
            print("------------------------------------")
            print(f"Anda melakukan pesan kelas latihan untuk {jumlah_sesi} sesi")
            print("Total Tagihan : ", jumlah_sesi*100000)
            print("------------------------------------")
            print("Selamat anda berhasil melakukan pemesanan pada kelas latihan angkat beban!")
            print("====================================================================")
            
            pilihan = input("Keluar Program ini atau Batalkan Kelas Latihan (1/2) ? ")
            if pilihan == "2":
                data_kelas_angkat_beban.batalkan_kelas(jumlah_sesi)
                print("------------------------------------\n")
                
        else: 
            print("------------------------------------")
            print("Maaf data berat maksimum anda tidak memenuhi persyaaratan untuk pesan kelas latihan angkat beban!")
            print("====================================================================")
            
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
