# (08) Relational Database

## Deskripsi
Database merupakan sekumpulan data yang terorganisir.

## Database Relationship
1. One to One  
   Contoh implementasi, setiap user hanya memiliki satu foto profil.  
2. One to Many  
   Contoh implementasi, setiap user bisa memiliki banyak tweets.  
3. Many to Many  
   Contoh implementasi, setiap user bisa memiliki banyak followers user dan setiap user bisa di follow banyak user.

## DDL
DDL (Data Definition Language) merupakan sebuah perintah yang digunakan untuk mendefinisikan skema di database seperti membuat, memodifikasi, dan menghapus struktur database.

### Macam-macam DDL Statement
1. CREATE DATABASE database_name;
2. USE database_name;
3. CREATE TABLE table_name(
    column1 data type PRIMARY KEY, 
    column2 data type
    ......);
4. DROP TABLE ...;
5. RENAME TABLE ...;
6. ALTER TABLE table_name 
   ADD COLUMN column1 data type;

## DML
DML (Data Manipulation Language) merupakan sebuah perintah yang digunakan untuk memanipulasi data dalam table dari suatu database.

### Macam-macam DML Operation
1. INSERT, digunakan untuk input data ke table.
2. SELECT, digunakan untuk menampilkan data dari table.
3. UPDATE, digunakan untuk mengupdate data di table.
4. DELETE, digunakan untuk menghapus data dari table.

### Macam-macam DML Statement
1. LIKE/BETWEEN
2. AND/OR
3. ORDER BY
4. LIMIT

## JOIN
JOIN merupakan sebuah klausa untuk mengkombinasikan record dari dua atau lebih table.

### Macam-macam Jenis JOIN
1. INNER  
   Inner join akan mengembalikan baris-baris dari dua table atau lebih yang memenuhi syarat.
2. LEFT  
   Left join akan mengembalikan seluruh baris dari table disebelah kiri yang dikenai kondisi ON dan hanya baris dari table disebelah kanan yang memenuhi kondisi join.
3. RIGHT  
   Right join akan mengembalikan seluruh baris dari table disebelah kanan yang dikenai kondisi ON dan hanya baris dari table disebelah kiri yang memenuhi kondisi join.

## AGGREGATE
Fungsi Agregasi merupakan fungsi dimana nilai beberapa baris dikelompokkan bersama untuk membentuk nilai ringkasan tunggal.

### Macam-macam Fungsi Agregasi SQL
1. MIN
2. MAX
3. SUM
4. AVG
5. COUNT
6. HAVING  
   Having digunakan untuk menyeleksi data berdasarkan kriteria tertentu, dimana kriteria berupa fungsi aggregat. 

## SUBQUERY
Subquery digunakan untuk mengembalikan data yang akan digunakan dalam query utama sebagai syarat untuk lebih membatasi data yang akan diambil. Subquery dapat digunakan dengan SELECT, INSERT, UPDATE, DELETE statment bersama dengan operator seperti =, <, >, >=, <=, IN, BETWEEN, dan lainnya.

## FUNCTION
Function merupakan sebuah kumpulan statement yang akan mengembalikan sebuah nilai balik pada pemanggilnya.  

**Komponen dalam pembuatan Function**
1. DELIMETER
2. CREATE FUNCTION
3. RETURN
4. DETERMINISTIC / NOT DETERMINISTIC
5. BEGIN END
