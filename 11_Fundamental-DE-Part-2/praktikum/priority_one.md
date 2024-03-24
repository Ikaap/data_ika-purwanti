# Soal Priority One

1. Jelaskan perbedaan antara data terstruktur dan data tidak terstruktur. Berikan contoh untuk masing-masing dan bahas bagaimana mereka biasanya disimpan dan diproses.  
   **Jawab :**  
   - Perbedaan dan contoh  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/11_Fundamental-DE-Part-2/screenshots/perbedaan_data.png)  
   **Pemrosesan Data :**  
   1. Data Terstruktur  
      - Ekstraksi data/informasi  
        Data dapat diekstraksi langsung dari basis data menggunakan bahasa kueri seperti SQL untuk basis data relational. Lakukan transformasi data jika diperlukan.  
      - Simpan dan atur data  
        Pilih tempat penyimpanan yang sesuai untuk fleksibilitas penyimpanan yang lebih besar.  
      - Analisis dan visualisasikan data  
        Gunakan alat analisis data seperti SQL, R, atau Python untuk menganalisis data terstruktur dan visualisasikan hasil analisis menggunakan grafik, diagram, atau laporan untuk memudahkan pemahaman.  
      - Hal yang perlu dipertimbangkan  
        Pertimbangkan penggunaan teknologi dan alat otomatisasi untuk meningkatkan efisiensi pemrosesan data terstruktur, seperti alat ETL atau sistem manajemen basis data.  
   2. Data Tidak Terstruktur  
      - Ekstraksi data/informasi  
        Gunakan teknik seperti analisis teks, pengenalan karakter optik, pemrosesan bahasa alami, atau visi komputer untuk mengekstrak informasi penting dari data tidak terstruktur. Atau konversikan data tidak terstruktur menjadi format yang lebih terstruktur atau semi-terstruktur, seperti tabel, grafik, atau key-value.  
      - Simpan dan atur data  
        Pilih penyimpanan yang sesuai untuk data tidak terstruktur, seperti database relasional, database NoSQL, data lake, atau platform cloud.  
      - Analisis dan visualisasikan data  
        Gunakan alat dan metode analisis yang sesuai seperti analisis statistik, pembelajaran mesin, atau analisis teks. Kemudian visualisasikan hasil analisis menggunakan teknik visualisasi seperti charts, maps, atau dashboard.  

2. Apa itu basis data relasional dan bagaimana cara kerjanya? Berikan contoh penggunaannya dalam dunia nyata.  
   **Jawab :**   
   Relational Database merupakan sistem penyimpanan data yang mengatur data dalam bentuk table, setiap table akan memiliki kolom dan baris. Konsep kunci dri relational database adalah hubungan antar table yang akan diidentify oleh PK dan FK.  
   Basis data relasional bekerja sesuai dengan model data yang sudah dibuat dan menggunakan SQL untuk berkomunikasi dengan database untuk melakukan transaksi yang diinginkan.  
   Contoh : Sistem E-Commerce, Sistem Manajement Penjualan, Sistem Perbankan dan Keuangan, Sistem Pemesanan/reservasi dan masih banyak sistem lainnya yang menggunakan basis data relational.  
   
3. Jelaskan konsep normalisasi basis data dan mengapa hal ini penting dalam konteks basis data relasional.  
   **Jawab :**  
   Pengertian dari normalisasi yaitu sebuah prinsip desain database yang bertujuan untuk mengindari complexcity, menghilangkan duplikasi dan menjaga integritas data serta mengatur data dengan cara yang terorganisir dan konsisten.  
   Namun pada kenyataannya, data pada table di database itu berupa data yang redudan (duplikat), berangkat dari permasalahan yang ada normalisasi dilakukan sebagai sebuah proses pengubahan data ke dalam bentuk standar atau normal agar memudahkan pengolahan dan analisis data. Untuk menjadikan table berada dalam bentuk yang normal terdapat beberapa tahapan normalisasi yang digunakan, diantaranya ada bentuk 1NF, 2NF, 3NF, NF, dan lainnya. Tahapan ini dapat disesuaikan dengan data yang digunakan, jika data pada table di database sudah berada pada bentuk yang standar maka tidak wajib melakukan tahapan yang selanjutnya/lainnya.  
   Normalisasi penting dilakukan agar database yang dirancang memiliki kuatlitas yang baik, meminimalisir terjadinya redudansi data, dan mencegah anomali data. Jika terdapat kesalahan dalam pembuatan rancangan database maka dapat menyebabkan berbagai masalah yang dapat memengaruhi kinerja sistem, integritas data, dan kemampuan sistem untuk memenuhi kebutuhan bisnis.  


### Referensi :
1. Artikel Linkedln - How do you manage unstructured data?
2. Artikel Binus - Normalisasi
3. Artikel Jojonomic - Normalisasi Database
4. Artikel AWS - Apa itu Basis Data Relasional?
