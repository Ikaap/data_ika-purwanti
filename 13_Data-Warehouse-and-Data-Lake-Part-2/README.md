# (13) Data Warehouse and Data Lake Part 2

## Replication
Replication merupakan sebuah mekanisme untuk melakukan duplikasi data dari database utama ke beberapa instance database lainnya.  Replication cocok digunakan untuk databasae yg sering untuk operasi read(membaca atau mengambil data dri database).  
Jika menggunakan replication dapat membuat sebuah reference table.

### Keuntungan dari Replication
1. Dapat meningkatkan availability.
2. Dapat melakukan pemisahan fungsi dari masing-masing database tanpa mengganngu database utamanya.

## Sharding
Sharding merupakan sebuah mekanisme untuk menyimpan sebuah data melalui beberapa database.
Satu server database hanya menyimpan sebagian data saja sehingga sekumpulan data lainnya akan disimpan pada server database yang lain. 
Sharding cocok digunakan untuk database yang sering digunakan untuk operasi write (manipulasi) seperti create, update, dan delete data.  
Jika menggunakan sharding dapat membuat sebuah distributed table.

## Keuntungan dari Sharding
1. Jika menerima data yang sangat banyak maka data dapat dibagi kebeberapa database sehingga performa dari database nya menjadi maksimal.

## Macam-macam Schema
## Star Schema  
Start schema merupakan schema paling sederhana yang memiliki satu tabel tengah yaitu tabel fakta dimana tabel tersebut terhubung dengan beberapa dimensi tabel lainnya.  

### Karakteristik Start Schema
- Setiap dimensi dalam schema Star hanya digambarkan dengan satu tabel dimensi.
- Tabel dimensi harus memiliki sebuah set atribut.
- Tabel dimensi melakukan join pada tabel fakta menggunakan FK.
- Tabel dimensi tidak terhubung satu sama lain.
- Tabel fakta mengandung key dan measure.

## Snowflake Schema
Snowflake Schema merupakan perpanjangan dari schema Star dengan menambahkan tabel dimensi lainnya dimana tabel dimensi lain tersebut merupakan hasil normalisasi tabel-tabel dimensi yang telah ada sebelumnya.  

### Karakteristik Snowflake Schema
- Kinerja query berkurang akibat dari banyaknya tabel yang ada.
- Membutuhkan upaya maintenance yang lebih besar karena pencarian tabel lebih banyak.
- Lebih mudah untuk menambahkan dimensi ke dalam schema.

## One Big Table (OBT)
One Big Table merupakan schema yang mengacu pada penggunaan satu tabel untuk menampung semua data dalam satu tabel besar. Schema ini memastikan data warehouse tidak perlu melakukan penggabungan apa pun dengan cepat. Karena kesederhanaannya, OBT cocok untuk proyek kecil yang berfokus pada pelacakan/tracking item tertentu. Item ini biasanya memiliki beberapa atribut yang terkait dengannya.

### Karakteristik One Big Table (OBT)
1. Memiliki banyak data yang redudan didalamnya
2. Memiliki performa yang baik.
3. Tidak menerapkan metode normalisasi

## BigQuery
BigQuery adalah platform analisis data berbasis cloud yang dikembangkan oleh Google untuk mengolah dataset besar dengan kecepatan dan efisiensi tinggi.  
Salah satu keunggulan utama BigQuery adalah kemampuan menjalankan query SQL di atas dataset yang disimpan langsung di infrastrukturnya. BigQuery dapat mengakses database tersebut secara langsung, mengurangi waktu dan tenaga yang diperlukan untuk mengumpulkan serta mengolah data sebelum dianalisis.  

### Keuntungan menggunakan BigQuery
1. Kecepatan dan efisiensi
2. Skalabilitas otomatis
3. Kemudahan pengelolaan data
4. Kemudahan integrasi
5. Aksesibilitas dan kolaborasi
