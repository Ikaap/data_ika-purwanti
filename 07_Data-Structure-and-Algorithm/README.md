# (07) Data Stucture and Algorithm

## Deskripsi
Data Structure merupakan suatu cara untuk mengatur dan menyimpan data agar dapat diakses dan digunakan secara efisien.

## Data Structure di Python
1. List  
   List merupakan kumpulan dari banyak nilai yang dapat disebut sebagai item atau elemen. Elemen pada list dapat di akses dan dimanipulasi. Untuk mengakses elemen pada list dapat mengguanakan indeks.  
   Method-method pada list :
   - len
   - append
   - extend
   - insert
   - remove
   - pop
   - index
   - copy
   - sort
2. Tuple
   Tupple sama dengan list, namun yang membedakan yaitu tuple bersifat imutable (nilai data/elemen tidak dapat diubah). Tuple biasanya digunakan untuk menyimpan nilai-nilai yang sudah constant. Contohnya titik koordinat x atau y.
3. Set
   Set merupakan salah satu array atau kumpulan dari banyak nilai yang tidak berurutan dan tidak boleh terdapat elemen/item yang duplikat di dalamnya. Pada set, kita tidak dapat mengakses elemen didalamnya menggunakan indeks. Set memungkinkan kita untuk mengubah elemen secara keseluruhan, namun tidak dapat mengubah item/elemen secara spesifik.  
   Method-method pada set:
   - add
   - union
   - remove
   - intersection
   - issuperset
   - difference
4. Dictionary
   Dictionary marupakan struktur data yang digunakan untuk menyimpan data berorientasikan key and value. Cara mendeklarasikan dictionary menggunakan kurung kurawal {}, lalu diisikan key and value nya atau bisa menggunakan keyword dict. Value dari dictionary dapat diakses menggunakan nama dari key nya.  
   Method-method pada dictionary :
   - items
   - get
   - keys
   - values
   - clear
   - setdefault
   - copy

## Searching  
   Algoritma searching digunakan untuk mencari atau menemukan data pada sebuah list. 

### Macam-macam Searching
1. Linear Search
   Pada algoritma linear search akan menjelajahi setiap elemen pada list dan menemukan nilai sesuai dengan target. 

## Sorting
   Sorting merupakan proses menyusun data dalam urutan tertentu.

### Macam-macam Sorting
1. Selection Sort  
   Pada algoritma selection sort, akan menjelajahi tiap elemen pada list lalu membandingkannya satu per satu mencri nilai paling kecil diantara mereka.
2. Counting Sort  
   Pada algoritma ini, mula-mula menemukan nilai terbesar pada suatu list dengan cara menggunakan method max, lalu diberikan list didalamnya. selanjutnya membuat array kosong sebanyak atau panjangnya sebesar nilai terbesar sebelumnya, lalu menghitung frekuensi masing-masing elemen dalam list. lalu membuat data hasil yang sudah diurutkan.
3. Merge Sort  
   Pada algoritma ini akan membagi dua nilai dari list yang diberikan lalu akan ada 2 sisi yang saling membandingkan tiap elemennya. Kalo len list nya ganjil, nilai tengahnya ikut kesebelah kiri, dan angka yang lebih kecil diletakkan di sebelah kiri.