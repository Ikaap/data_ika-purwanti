# (06) Object Oriented Programming

## Deskripsi
Object Oriented Programming merupakan suatu paradigma yang memungkinkan ktia untuk mengorganisir program sehingga properti dan perilaku dikemas kedalam object individu.

Terdapat istilah yang sering digunakan dalam konsep OOP, diantaranya :
1. **Properties**, properties ditentukan oleh nilai dari suatu atribut.
2. **Behavior**, behavior ditentukan oleh bagaimana object tersebut bertindak atau bereaksi terhadap permintaan.

## Fundamental OOP
1. Encapsulation  
   Encapsulation melibatkan pengelompokan atribut dan metode dalam satu unit yang dikenal sebagai class. Encapsulation sangat membantu untuk melindungi atribut dan metode dari gangguan eksternal.  
   - Basic-basic Encapsulation :
     - Class  
       Class merupakan template atau blueprint yang digunakan untuk membuat object. Dalam pembuatan sebuah nama class dapat menggunakan notation **CamelCase**.
     - Atribut
       Atribut merupakan instance yang berisi karakteristik. Terdapat 3 tipe dalam atribut, diantaranya :
       - **Public**, dapat diakses diclassnya sendiri maupun diluar class.
       - **Protected**, hanya dapat diakses di classnya sendiri dan class turunannya.
       - **Private**, hanya dapat diakses di classnya sendiri.
     - Method / Function  
       Hal-hal penting dalam membuat sebuah method :
       - Method / Function Name
       - Parameters
       - Returns
2. Data Abstraction  
   Data Abstraction merupakan konsep dimana hanya menampilkan fitur-fitur penting dalam suatu object. Data Abstraction juga dapat menyembunyikan detail-detail yang complex seperti dengan menggunakan metode/teknik getter dan setter.
3. Inheritance  
   Inheritance merupakan salah satu pilar utama dalam OOP. Inherintance memungkinkan kita untuk mewarisi code dari kelas lain, sehingga tidak perlu menulis ulang code yang sama.  
   Terdapat dua keyword yang sering digunakan dalam inheritance :
   - Super
     Digunakan untuk memanggil metode dari kelas induk. Super memungkinkan kita untuk menggunakan metode yang sudah ada dan menambahkan logika tambahan yang diperlukan.
   - Overriding  
     Digunakan ketika menggunakan metode dari class induk tapi modifikasi logic sesuai kebutuhan.
4. Polymorphism  
   Polymorphism mengacu pada kemampuan object dari tipe yang berbeda untuk merespon fungsi dengan nama yang sama. Polymorphism memungkinkan kita untuk mendefinisikan satu antar muka yang digunakan oleh berbagai jenis object.
