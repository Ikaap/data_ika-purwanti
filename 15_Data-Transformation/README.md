# (15) Data Transformation

## Deskripsi
Data Transformation adalah proses mengkonversi data dari satu format / struktut kedalam bentuk format lainnya. Proses ini merupakan fundamental dalam proses integrasi data.

### Alasan Pentingnya Data Transformation
1. Memungkinkan data dari berbagai sumber untuk digabungkan, sehingga memudahkan analisis dan pengambilan keputusan.
2. Memastikan kualitas dan konsistensi data.
3. Memfasilitasi analisis data dan BI.

### Jenis-Jenis Transformasi Data
1. Normalization  
   Memastikan bahwa setiap fitur akan berkontribusi secara setara terhadap perhitungan, biasa digunakan dalam komputasi dalam algoritma Machine Learning.  
   **Beberapa method :**
   - Min Max Scaling
   - Z-score normalization
2. Encoding  
   Pendekatan ini akan melibatkan contoh dari Machine Learning, Machine Learning membutuhkan sebuah numerical input, jadi data yang katergorikal akan di konvert kedalam bentuk data numerikal.  
   **Beberapa method :**
   - One-hot encoding, akan memberikan nilai binary ke dalam setiap kolom untuk setiap kategori (akan membuat kolom baru sesuai jumlah nilai).
   - Label encoding, akan memberikan nilai ke dalam sebuah int unik untuk setiap kategori.
3. Aggrrgation
   Membantu DE untuk mendapatkan tampilan data yang diringkas, seringkali akan mengubah data dalam bentuk granularitas.  
   **Beberapa method :**
   - Sum
   - Average
   - Count
   - Max
   - Min

### Tantangan dalam Data Transformasi
1. Mengelola data yang hilang  
   Metode :
   - Deletion, menghapus baris dengan nilai yang hilang.
   - Imputation, mengisi nilai yang hilang berdasarkan data point yang lain. Seperti avg, min atau modulus, dan lainnya.
   - Foward/Backward Fill, menggunakan nilai sesudah atau sebelumnya untuk mengisi nilai yang hilang.
2. Menangani outlier  
   Metode :
   - Z-score, digunakan untuk mengidentifikasi nilai yang berjarak berdasarkan standar deviasi.
   - IQR (Interquartile Range), akan menemukan nilai yang jauh dri rentang normal.
3. Memastikan integrasi data selama proses transformasi  
   Metode :
   - Regular Backups, membuat cadangan data.
   - Validation Checks, digunakan untuk memastikan data dimasukan kedalam sistem.
   - Checksums, untuk memverifikasi integritas data selama transfer.