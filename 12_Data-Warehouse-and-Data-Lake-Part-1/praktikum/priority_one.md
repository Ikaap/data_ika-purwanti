# Soal Prioritas 1

1. Sebutkan dan jelaskan tantangan yang perlu dihadapi dalam penggunaan Data Warehouse!  
   **Jawab :**  
   - **Integrasi Data**, mengintegrasikan data dari berbagai sumber yang memiki format dan model data yang berbeda-beda, dapat menjadi proses yang kompleks serta menjaga konsisten dalam mengintegrasikan data menjadi tantangan dalam penggunaan data warehouse.  
   - **Kualitas Data**, Kualitas data yang buruk dapat menyebabkan analisis yang tidak akurat atau tidak lengkap, sehingga memerlukan pembersihan dan validasi data yang cermat.  
   - **Volume Data**, data warehouse dapat berisi data dalam jumlah besar, sehingga menyulitkan pengelolaan dan pemrosesan. Pengelolaan dan pemrosesan volume data besar memerlukan perencanaan, desain, dan pengoptimalan yang cermat.  
   - **Kinerja**, data warehouse harus menyediakan waktu respons query yang cepat untuk mendukung  business intelligence dan analytics. Untuk mencapai kinerja tinggi memerlukan model data yang kompleks dan strategi pengindeksan yang baik.  
   - **Keamanan**, data warehouse berisi data sensitif, dan memastikan keamanan data sangatlah penting. Menerapkan langkah-langkah keamanan yang kuat, seperti kontrol akses, enkripsi data, dan penyembunyian data, dapat menjadi tantangan, terutama ketika berhadapan dengan data dalam jumlah besar.  
   - **Persyaratan Bisnis**, merancang dan mengimplementasikan data warehouse yang memenuhi persyaratan bisnis yang kompleks memerlukan perencanaan, komunikasi, dan kolaborasi yang cermat antara tim IT dan tim bisnis.  
   - **Biaya**, penerapan data warehouse bisa memakan biaya yang mahal, dengan biaya yang signifikan terkait dengan perangkat keras, perangkat lunak, dan pemeliharaan berkelanjutan.  
   - **Manajemen Perubahan**, data warehouse dirancang untuk mendukung pengambilan keputusan bisnis, dan oleh karena itu, data warehouse harus dapat beradaptasi dengan perubahan dalam proses dan persyaratan bisnis, sehingga memerlukan proses manajemen perubahan yang efektif.  

2. Berdasarkan diagram ERD yang ada pada soal buatlah berbagai tabel dengan menggunakan Citus.  
   **Jawab :**  
   1. Membuat dan menjalankan container citus dan container postgres  
   **Jawab :**  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_one_2_1.png)  
   2. Masuk ke Postgres  
   **Jawab :**  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_one_2_2.png)  
   3. Membuat table  
      - users  
      **Jawab :**  
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_one_2_3.png)  
      - categories  
      **Jawab :**  
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_one_2_4.png)  
      - posts  
      **Jawab :**  
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_one_2_5.png)  
      - comments  
      **Jawab :**  
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_one_2_6.png)  
   4. Menampilkan table yang sudah dibuat  
   **Jawab :**  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_one_2_7.png)  
   5. Insert dan menampilkan data  
      - users  
      **Jawab :**  
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_one_2_8.png)  
      - categories  
      **Jawab :**  
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_one_2_9.png)  
      - posts  
      **Jawab :**  
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_one_2_10.png)  
      - comments  
      **Jawab :**  
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_one_2_11.png)  