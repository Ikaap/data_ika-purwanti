# (11) Fundamental DE Part 2

## Data Terstruktur & Data Tidak Terstruktur
1. **Data Terstruktur**
   Data Terstruktur merupakan data yang memiliki model, format, dan schema. Data ini disimpan ke dalam database relational atau yg dikenal dengan RDBMS dan didalamnya dapat melakukan proses CRUD data. Data terstruktur memiliki penyimpanan yg relatif sedikit.
2. **Data Tidak Terstruktur**
   Data Tidak Terstruktur merupakan data yang memiliki struktur internal tapi tidak terstruktur melalui model data ataupun schema. Data tidak terstruktur memili penyimpanan yang relatif lebih besar atau banyak. Data tidak terstruktur bisanya disimpan di data lake atau file storage.  
   Contoh Data Tidak Terstruktur :
    - Dokumen PDF
    - Gambar
    - Video
    - Data dari media sosial seperti instagram, twitter, dan facebook.
3. **Data Semi Terstruktur**
   Data Semi Terstruktur berada diantara data terstruktur dan data tidak terstruktur. Data semi terstruktur tidak memiliki schema yang kaku, namun memiliki karakteristik klasifikasi tertentu yang memungkikan untuk dianalisis dan memungkinkan memiliki data dalam bentuk kolom dan baris. Data semi terstruktur dapat disimpan di file store/data lake.  Salah satu contohnya yaitu metadata. Data ini dapat disimpan kedalam NoSql database seperti dokumen, graph, key-value dan wide-column.

## Relational & NoSQL Database
1. **Relational Database**
   Relational Database merupakan sistem penyimpanan data yang mengatur data dalam bentuk table, setiap table akan memiliki kolom dan baris. Konsep kunci dri relational database adalah hubungan antar table yang akan diidentify oleh PK dan FK.  
   Macam-macam RDBMS :
    - Oracle Database
    - Microsoft SQL Server
    - IBM DB2
    - MySQL Database
    - PostgreSQL Database  

### Normalization
Normalization merupakan prinsip desain database yang bertujuan untuk mengindari complexcity, menghilangkan duplikasi dan menjaga integritas data serta mengatur data dengan cara yang terorganisir dan konsisten.

2. **NoSQL Database**
   NoSQL Database pada umumnya akan mendukung data yang semi terstruktur dan memiliki schema yang fleksibel untuk membangun sebuah app yang modern. NoSQL identik dengan sistem terdistribusi, dimana beberapa mesin dapat bekerja bersama melalui cluster.  
   Jenis-Jenis NoSQL Database : 
    - Document  
      Tools : Amazon DocumentDB, MongoDB, Cosmos DB, ArangoDB, Couchbase Server, CouchDB
    - Graph  
      Tools : Neo4j
    - Key-value  
      Tools : Redis, Memcached, Riak
    - Wide-column  
      Tools : HBase, Google BigTable, AWS DynamoDB, Apache Cassandra, MariaDB

## CAP Theorem
CAP Theorem merupakan prinsip dasar yang memperbarui design  dan operasi dari NoSQL Database. Dalam CAP Theorem menyatakan bahwa hanya dalam lingkungan terdistribusi hanya ada 2 atau 3 karakteristik berikut yang dapat di capai bersamaan yaitu : konsistensi, ketersediaan, ketahanan terhadap praktiksi.

## OLTP & OLAP
1. **OLTP**
   OLTP (Online Transaction Processing) merupakan kategori pemrosessan yang berurusan dengan banyak transaksi yang dilakukan oleh banyak pengguna. Proses OLTP sangat berhubungan dengan inserting, updating, dan deleting.
2. **OLAP**
   Data Warehouse merupakan tempat yang sangat ideal untuk memelihara atau menggunakan case penggunaan OLAP (Online Analytical Processing). Yang bertujuan untuk menjawab atau menyelesaikan query analitic multidimensi.

## Data Pipeline System 
Data Sources -> Data Lake -> (Proses ETL) -> Data Warehouse -> Data Mart

## Data Lake, Data Warehouse, dan Data Mart
1. **Data Lake**
   Data Lake adalah repository yang terpusat yang dirancang untuk menyimpan, memproses, dan mengamankan jumlah data yang semi terstruktur dan data tidak terstruktur yang jumlahnya sangat besar.Data Lake memungkinkan penyimpanan data dalam format aslinya dan dapat memproses data dari berbagai jenis tanpa memperhatikan batasan ukuran.  
   Contohnya : citra, dokumen pdf.  
   Tools : Amazon S3, Google Cloud Storage.
2. **Data Warehouse**
   Data Warehouse merupakan sebuah data yang digunakan untuk analisis pelaporan data terstruktur dan data semi terstruktur dari berbagai sumber. Data warehouse ini akan memberikan pandangan dalam jangka panjang.  
   Tools : Amazon Redshift, Google BigQuery.
3. **Data Mart**
   Data Mart merupakan subset dari data warehouse yg berfokus pada area bisnis tertentu. Dengan adanya data mart memungkinkan akses cepat ke wawasan bisnis tanpa harus mencari keseluruhan data warehouse.  
   Sebagai contoh : 
   Bnyak perusahaan yang memiliki data mart yang dimana data mart itu sangat spesifik terhadap bagaimana dept itu mengolah bisnis, seperti finance, sales atau marketing. Data ini nantinya akan dipecah-pecah menjadi bagian-bagian yang lebih subjektif.