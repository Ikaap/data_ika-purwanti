# Soal Prioritas 2

1. Anda diberi tugas untuk merancang sistem basis data untuk sebuah perusahaan e-commerce. Perusahaan ini memiliki data yang sangat beragam, mulai dari data transaksi pelanggan hingga log interaksi pengguna di website. Diskusikan pendekatan yang akan Anda gunakan untuk mengelola data ini, termasuk pemilihan antara basis data relasional dan NoSQL, serta strategi untuk mengintegrasikan data terstruktur dan tidak terstruktur.  
   **Jawab :**  
   Database yang digunakan yaitu data relational, terdapat beberapa pertimbangan diantarnya :
   - Perusahaan memiliki mayoritas data yang terstruktur seperti data transaksi, pelanggan, produk, dan data lainnya. Data-data tersebut sudah memiliki model, format, dan skema yang sudah ditentukan.
   - Sistem relasional lebih cocok digunakan untuk sistem basis data e-commerce yang datanya saling berhubungan, contohnya data kategori produk dengan data produk, data user dengan transaksi, data transaksi dengan data produk.
   - Sistem basis data e-commerce memerlukan integritas data yang tinggi, dengan mengimplementasikan konsep Foreign Key untuk memastikan keakuratan dan keterhubungan data.
   - Sistem basis data e-commerce termasuk sistem dengan transaksional data yang kompleks oleh karena itu model data relational cocok diterapkan dalam sistem ini.  

   **Strategi Intergrasi Data**
   1. Data Terstruktur  
      - Identifikasikan kebutuhan data  
        Dalam proses ini tentukan entitas yang diperlukan, model, format serta skema untuk value dari masing-masing entitas.  
      - Design skema database  
        Buat ERD untuk sistem basis data e-commerce sesuai dengan aturan bisnis yang akan diterapkan di perusahaan. Dan lakukan normalisasi untuk menghindari terjadinya data redudan dan anomali dalam database.  
      - Lakukan ETL   
        Ekstrak data dari sumber-sumber data yang berbeda, lakukan transformasi data jika diperlukan kemudian load data ke penyimpanan untuk menyatukan kembali data dari sumber yang berbeda.  
      - Implementasikan Data Pipeline
        Pipeline batch dapat digunakan untuk pembuatan laporan, analisis lebih lanjut, maupun evaluasi sistem e-commerce. Ataupun menerapkan kombinasi analisis batch dan stream untuk mendapatkan wawasan yang lebih lengkap tentang perilaku pelanggan, kinerja produk, dan tren pasar.  
   2. Data Tidak Terstruktur  
      - Pengumpulan data
        Dalam proses ini gunakan alat untuk mengumpulkan data tidak terstruktur dari berbagai sumber, dan kirimkan data tersebut ke sistem basis data NoSQL.
      - Transformasi data
        Lakukan transformasi data tidak terstruktur untuk melakukan perubahan format atau pembersihan data.
      - Simpan data
        Simpan data tidak terstruktur dalam penyimpanan yang sesuai seperti ke dalam data lake atau sistem file.  
      - Integrasi dengan basis data relational  
        Setelah proses transformasi selesai dilakukan simpanlah hasil data ke dalam basis data relational yang digunakan. Dapat menggunakan docker compose untuk proses insert data dari penyimpanan ke dalam database relational yang digunakan.  


### Referensi :
1. Materi
2. Artikel entrance - When To Use NoSQL Vs. Relational Databases