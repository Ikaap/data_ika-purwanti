# Soal Eksplorasi

- Input & output pada prompt :  
  **Jawab :**  
  1. proses 1
     - **input :**  
       saya memiliki struktur table  untuk aplikasi e-commerce X, buatkan dataset nya dalam format excel, berdasarkan schema berikut :  
        1. table user (10 data)  
            id int,  
            name varchar,  
            email varchar,  
            nohp varchar,  
            gender char,  
            address text   
        2.  table product (7 data)  
            id int,  
            name varchar,  
            stok int,  
            price int  
        3. table transaction (20 data)  
            transaction_id int,  
            user_id int,  
            transaction_date date,  
            produk_id int,  
            qty int,  
            payment_method int,  
            notes text  
        pastikan datanya saling berhubungan dan lengkap sesuai jumlah data yang sudah ditentukan  

     - **output :**  
       Berikut adalah dataset dalam format Excel berdasarkan skema yang Anda berikan:  
        1. Tabel User  
            id	name	email	nohp	gender	address
            1	John Doe	john.doe@example.com	08123456789	M	123 Main St, City A, Country 1  
            2	Jane Smith	jane.smith@example.com	08234567890	F	456 Elm St, City B, Country 2  
            3	David Lee	david.lee@example.com	08345678901	M	789 Oak St, City C, Country 3  
            4	Emily Chen	emily.chen@example.com	08456789012	F	321 Pine St, City D, Country 4  
            5	Michael Kim	michael.kim@example.com	08567890123	M	654 Cedar St, City E, Country 5  
            6	Sarah Wong	sarah.wong@example.com	08678901234	F	987 Maple St, City F, Country 6  
            7	Alex Wang	alex.wang@example.com	08789012345	M	159 Walnut St, City G, Country 7  
            8	Lisa Zhang	lisa.zhang@example.com	08890123456	F	753 Birch St, City H, Country 8  
            9	Kevin Liu	kevin.liu@example.com	08901234567	M	852 Ash St, City I, Country 9  
            10	Mary Park	mary.park@example.com	09012345678	F	246 Spruce St, City J, Country 10  
        2. Tabel Product  
            id	name	stok	price  
            1	T-shirt	    100	    15000  
            2	Jeans	    80	    25000  
            3	Sneakers	120	    50000  
            4	Backpack	50	    75000  
            5	Watch	    200	    100000  
            6	Smartphone	70	    300000  
            7	Laptop	    30	    700000  
        3. Tabel Transaction  
            transaction_id	user_id	transaction_date	product_id	qty	payment_method	notes  
            1	1	2024-04-01	1	2	1	Nice purchase!  
            2	2	2024-04-02	3	1	2  
            3	3	2024-04-03	5	3	1  
            4	4	2024-04-04	2	1	1  
            5	5	2024-04-05	6	2	2  
            6	6	2024-04-06	4	1	1  
            7	7	2024-04-07	1	3	2  
            8	8	2024-04-08	3	2	1  
            9	9	2024-04-09	7	1	2  
            10	10	2024-04-10	5	2	1  
            11	1	2024-04-11	2	1	2  
            12	2	2024-04-12	6	2	1  
            13	3	2024-04-13	3	1	2  
            14	4	2024-04-14	5	3	1  
            15	5	2024-04-15	4	1	2  
            16	6	2024-04-16	1	2	1  
            17	7	2024-04-17	7	1	2  
            18	8	2024-04-18	2	1	1  
            19	9	2024-04-19	3	2	2  
            20	10	2024-04-20	6	1	1  
        Dataset ini mencakup 10 data pengguna, 7 data produk, dan 20 data transaksi yang saling berhubungan sesuai dengan skema yang telah Anda tentukan. Jika Anda memerlukan format atau informasi tambahan, jangan ragu untuk memberi tahu saya!  
    
  2. proses 2
     - **input :**  
       dari dataset diatas, gunakan teknik machine learning dan analisis data untuk memberikan solusi mengenai sistem rekomendasi produk yang lebih relevan untuk setiap pelanggan.  

     - **output :**  
       Untuk memberikan solusi sistem rekomendasi produk yang lebih relevan untuk setiap pelanggan berdasarkan dataset yang diberikan, Anda dapat menggunakan teknik Collaborative Filtering atau Content-Based Filtering. Saya akan memberikan contoh implementasi keduanya:

        1. Collaborative Filtering:  
        Collaborative Filtering menggunakan informasi dari perilaku pengguna (dalam hal ini, transaksi) untuk menemukan pola atau kemiripan antara pengguna dan produk. Berikut adalah langkah-langkahnya:  
        - Matriks Pengguna-Produk: Buat matriks yang menunjukkan hubungan antara pengguna dan produk berdasarkan transaksi.
        - Similarity Measures: Hitung kesamaan antara pengguna atau produk. Anda dapat menggunakan metrik seperti Cosine Similarity atau Pearson Correlation.
        - Rekomendasi Produk: Gunakan similarity scores untuk merekomendasikan produk kepada pengguna berdasarkan riwayat transaksi mereka dan transaksi pengguna lain yang serupa.

        2. Content-Based Filtering:  
        Content-Based Filtering menggunakan fitur produk untuk merekomendasikan produk yang serupa dengan yang telah disukai oleh pengguna. Berikut adalah langkah-langkahnya:  
        - Ekstraksi Fitur: Ekstrak fitur-fitur penting dari setiap produk. Dalam kasus ini, Anda dapat menggunakan atribut seperti nama produk, harga, dan stok.
        - Pembuatan Profil Pengguna: Buat profil pengguna berdasarkan transaksi sebelumnya.
        - Perhitungan Kesamaan: Hitung kesamaan antara produk yang tersedia dan produk yang disukai oleh pengguna berdasarkan profil pengguna dan fitur produk.
        - Rekomendasi Produk: Rekomendasikan produk yang memiliki kesamaan tertinggi dengan produk yang disukai oleh pengguna.

        Langkah-langkah di atas bisa diimplementasikan dengan menggunakan algoritma Machine Learning seperti Nearest Neighbors, Support Vector Machines, atau Decision Trees.  

        Saya bisa membantu Anda dalam mengimplementasikan salah satu teknik tersebut secara lebih rinci, atau jika Anda memiliki preferensi tertentu dalam metode yang ingin digunakan. Apakah Anda ingin melanjutkan dengan salah satu teknik tersebut?  
    
  3. proses 3
     - **input :**  
       coba implementasikan integrasi salah satu teknik yang direkomendasikan di atas  

     - **output :**  
       Mari kita implementasikan metode Content-Based Filtering untuk sistem rekomendasi produk. Kita akan menggunakan fitur-fitur produk (nama produk, harga, stok) dan profil pengguna (riwayat transaksi) untuk merekomendasikan produk yang sesuai dengan preferensi setiap pengguna.  

        Berikut adalah langkah-langkah implementasinya:  
        1. Ekstraksi Fitur: Kita akan menggunakan nama produk, harga, dan stok sebagai fitur-fitur produk.
        2. Pembuatan Profil Pengguna: Kita akan membuat profil pengguna berdasarkan riwayat transaksi mereka.
        3. Perhitungan Kesamaan: Kita akan menghitung kesamaan antara produk yang tersedia dan produk yang disukai oleh pengguna berdasarkan profil pengguna dan fitur produk.
        4. Rekomendasi Produk: Kita akan merekomendasikan produk yang memiliki kesamaan tertinggi dengan produk yang disukai oleh pengguna.  

        Mari kita mulai dengan langkah pertama, yaitu ekstraksi fitur dari produk dan pembuatan profil pengguna. Saya akan menggunakan Python dan library pandas untuk melakukan ini. Apakah Anda ingin melanjutkan?  
    
  4. proses 4
     - **input :**  
       lanjutkan tahap implementasinya dari tahap 1 - 4  

     - **output :**  
        Baik, mari kita lanjutkan dengan implementasi tahap 1 - 4:  

        Tahap 1: Ekstraksi Fitur  
        Pertama, kita akan mengimpor dataset dan melakukan pengolahan awal untuk mengekstrak fitur-fitur produk.  
        **Code :**  
            import pandas as pd  
            **# Import dataset**  
            users_df = pd.read_excel("dataset.xlsx", sheet_name="User")  
            products_df = pd.read_excel("dataset.xlsx", sheet_name="Product")  
            transactions_df = pd.read_excel("dataset.xlsx", sheet_name="Transaction")    
            **# Menggabungkan transaksi dengan informasi produk dan pengguna**  
            transactions_df = transactions_df.merge(users_df, how='left', left_on='user_id', right_on='id')  
            transactions_df = transactions_df.merge(products_df, how='left', left_on='product_id', right_on='id')    
            **# Mengambil hanya kolom yang relevan untuk analisis**  
            transactions_df = transactions_df[['user_id', 'id_x', 'name_x', 'price', 'stok']]    
            **# Mengganti nama kolom agar sesuai**  
            transactions_df.columns = ['user_id', 'product_id', 'product_name', 'price', 'stok']    
            **# Melihat data**  
            print(transactions_df.head())  
        
        Tahap 2: Pembuatan Profil Pengguna  
        Sekarang, kita akan membuat profil pengguna berdasarkan riwayat transaksi mereka.  
        **Code :**  
            **# Membuat tabel pivot untuk mencatat pembelian setiap produk oleh setiap pengguna**  
            user_product_matrix = pd.pivot_table(transactions_df, values='price', index='user_id', columns='product_name', aggfunc='count', fill_value=0)    
            **# Melihat profil pengguna**  
            print(user_product_matrix.head())  

        Tahap 3: Perhitungan Kesamaan  
        Selanjutnya, kita akan menghitung kesamaan antara produk yang tersedia dan produk yang disukai oleh pengguna berdasarkan profil pengguna dan fitur produk.  
        **Code :**  
            from sklearn.metrics.pairwise import cosine_similarity  
            **# Menghitung kesamaan antara produk**
            product_features = products_df[['price', 'stok']].values  
            product_similarity = cosine_similarity(product_features)    
            **# Melihat matriks kesamaan produk**  
            print(product_similarity)  
        
        Tahap 4: Rekomendasi Produk  
        Terakhir, kita akan merekomendasikan produk yang memiliki kesamaan tertinggi dengan produk yang disukai oleh pengguna.  
        **Code :**  
            def recommend_products(user_id, top_n=5):  
                **# Mengambil profil pengguna**  
                user_profile = user_product_matrix.loc[user_id]    
                **# Menghitung skor kesamaan antara produk yang disukai oleh pengguna dan produk lainnya**  
                product_scores = product_similarity.dot(user_profile)    
                **# Mengurutkan produk berdasarkan skor kesamaan**  
                recommended_indices = product_scores.argsort()[::-1]    
                **# Mengambil top N produk yang direkomendasikan**  
                top_recommended_indices = recommended_indices[:top_n]    
                **# Mengambil nama produk dari indeks yang direkomendasikan**  
                top_recommended_products = products_df.iloc[top_recommended_indices]['name'].values  
                return top_recommended_products    
            **# Contoh rekomendasi untuk pengguna dengan id 1**  
            user_id = 1  
            recommended_products = recommend_products(user_id)  
            print("Rekomendasi Produk untuk Pengguna dengan ID", user_id, ":")  
            for idx, product in enumerate(recommended_products, start=1):  
                print(idx, ".", product)  

  5. proses 5
     - **input :**  
       buatkan dokumentasi lengkap untuk dataset, sistem rekomendasi sampai implementasi proses di atas  

     - **output :**  
       Dokumentasi Sistem Rekomendasi Produk
        1. Dataset  
        Dataset yang digunakan untuk sistem rekomendasi produk terdiri dari tiga tabel utama:  
        a. Tabel User  
            id: ID unik untuk setiap pengguna.  
            name: Nama pengguna.  
            email: Alamat email pengguna.  
            nohp: Nomor telepon pengguna.  
            gender: Jenis kelamin pengguna.  
            address: Alamat lengkap pengguna.  
        b. Tabel Product  
            id: ID unik untuk setiap produk.  
            name: Nama produk.  
            stok: Jumlah stok produk yang tersedia.  
            price: Harga produk.  
        c. Tabel Transaction  
            transaction_id: ID transaksi unik.  
            user_id: ID pengguna yang melakukan transaksi.  
            transaction_date: Tanggal transaksi dilakukan.  
            product_id: ID produk yang dibeli.  
            qty: Jumlah produk yang dibeli dalam transaksi.  
            payment_method: Metode pembayaran yang digunakan.  
            notes: Catatan tambahan (opsional) untuk transaksi.  
        
        2. Sistem Rekomendasi Produk  
        Sistem rekomendasi produk yang diimplementasikan menggunakan metode Content-Based Filtering. Langkah-langkahnya sebagai berikut:  
        - Tahap 1: Ekstraksi Fitur  
          Pada tahap ini, fitur-fitur produk diekstraksi dari dataset, termasuk nama produk, harga, dan stok.  
        - Tahap 2: Pembuatan Profil Pengguna  
          Profil pengguna dibuat berdasarkan riwayat transaksi mereka. Matriks pengguna-produk digunakan untuk mencatat pembelian setiap produk oleh setiap pengguna.  
        - Tahap 3: Perhitungan Kesamaan  
          Kesamaan antara produk yang tersedia dihitung berdasarkan fitur-fitur produk menggunakan metrik cosine similarity.  
        - Tahap 4: Rekomendasi Produk  
          Pada tahap terakhir, produk direkomendasikan kepada pengguna berdasarkan kesamaan produk yang disukai oleh pengguna dan produk yang tersedia.  

        3. Implementasi Proses  
        Implementasi proses di atas dilakukan menggunakan bahasa pemrograman Python dan beberapa library, antara lain:  
            - pandas: Untuk manipulasi dan analisis data.  
            - scikit-learn: Untuk menghitung kesamaan antara produk menggunakan cosine similarity.  
            - numpy: Untuk operasi numerik.  

        Langkah-langkah implementasinya adalah sebagai berikut:  
            - Ekstraksi Fitur: Fitur-fitur produk diekstraksi dari dataset menggunakan library pandas.  
            - Pembuatan Profil Pengguna: Profil pengguna dibuat berdasarkan riwayat transaksi menggunakan operasi pivot tabel.  
            - Perhitungan Kesamaan: Kesamaan antara produk dihitung menggunakan cosine similarity dari fitur-fitur produk.  
            - Rekomendasi Produk: Produk direkomendasikan kepada pengguna berdasarkan kesamaan produk yang disukai oleh pengguna.  

        Implementasi ini memberikan solusi rekomendasi produk yang lebih relevan untuk setiap pengguna berdasarkan preferensi dan pembelian sebelumnya. Anda dapat menyesuaikan dan mengoptimalkan algoritma ini sesuai dengan kebutuhan bisnis dan data yang tersedia.  

- Hasil :  
  **Jawab :**  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_1.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_2.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_3.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_4.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_5.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_6.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_7.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_8.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_9.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_10.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_11.png)  
  ![preview](21_Introduction-AI-on-Data-Engineer\screenshots\output_exploration_12.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_13.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_14.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_15.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_16.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_17.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_18.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_19.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_20.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_exploration_21.png)  

- Penjelasan :  
  **Jawab :**  
  ChatGPT memberikan output yang sesuai dengan input yang saya berikan terkait membuat dataset, identifikasi pola pembelian pelanggan, rekomendasi dan implementasi sistem rekomendasi serta dokumentasi. 