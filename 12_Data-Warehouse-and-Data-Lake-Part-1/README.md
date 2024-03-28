# (12) Data Warehouse and Data Lake Part 1

## Data Warehouse
Data Warehouse merupakan sebuah sistem yang mengumpulkan data yang sudah di proses di pipeline ETL dari berbagai sumber dalam satu tempat yang terpusat, yang nantinya data tersebut dapat digunakan untuk analisis, data mining AI dan ML.  

### Teknologi yang sering digunakan untuk Data Warehouse
1. AWS Redshift
2. Google Big Query
3. Clickhouse
4. Snowflake
5. Databricks
6. Apache Dorris
7. Postgre dengan Citus Extension

## Data Lake
Data Lake merupakan sistem yang mengumpulkan berbagai macam data di satu tempat namun data yang dikumpulkan belum melewati proses tidak ada proses ETL. Struktur data yang ada di data lake bersifat raw.  
Data Lake memiliki aksesbilitas yang lebih unggul daripada data warehouse dan proses update data yang cepat.  

## Data Lakehouse
Data Lakehouse merupakan sebuah arsitektur yang menggabungkan fleksibilitas dan efesiensi cost dari data lake yang nantinya dapat digabungkan dengan manajement data yang lebih terstruktur dari data warehouse, nantinya arsitektur ini dapat digabungkan di satu platform.  


## Columnar Table
Columnar Table merupakan sebuah mekanisme dimana dapat menyimpan data yang berorientasi dengan structur column. Columnar table dapat digunakan menggunakan PostgreSQL dengan Citus Extension. 

## Keunggulan Columnar Table
1. Mengakses data lebih cepat.
2. Menerapkan mekanisme compression, yaitu ukuran dri database bisa diminimalisir, jadi ukuran dari columnar table lebih kecil jika dibandingkan dengan table biasa. 

## Kelemahan Columnar Table
1. Tidak cocok untuk operasi write, karena prosesnya akan lebih lama.  

## Citus
Citus merupakan sebuah extension yang bersifat open source yang dapat digunakan di postgresql. Dengan menggunakan citus dapat mengubah database SQL menjadi database yang terdistribusi, sehingga dapat mengimplementasikan distributed table, reference table, SQL query engine yang didevelop secara terdistribusi.  

## Keunggulan Citus 
1. Dapat menerapkan proses sharding menggunakan distributed table.
2. Dapat menerapkan refences table sebagai proses replikasi atau dapat digunakan untuk melakukan operasi join atau penggunaan FK dari berbagai table yg terdistribusi.
3. Dapat memanfaatkan query engine yg sudah tersedia di Citus.
4. Dapat memanfaatkan columnar storage, nantinya di citus dapat merancang sebuah table berbasis columnar untuk digunakan proses analisis atau OLAP.  

## Kasus-kasus Tidak Cocok Menggunakan Citus
1. Memiliki database postgreSQL, yang workloadnya belum terlalu besar.
2. Melakukan proses analitikal secara offline, dan tidak membutuhkan data dari database secara realtime.
3. Menggunakan aplikasi analitik yang tidak support jumlah user yang banyak.

## Partition
Patition merupakan mekanisme memecah satu table menjadi beberapa table lainnya secara terpisah. Tujuan dari partitioning adalah dapat melakukan semacam separation of concern antara table yang digunakan untuk proses umum dan dapat pecah table yang digunakan untuk analisis data secara spesifik. Sehingga sistem menjadi lebih stabil. 