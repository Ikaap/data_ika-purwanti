# Soal Prioritas 2

1. Sebuah perusahaan yang bergerak di bidang jasa penyewaan kendaraan bermotor ingin menerapkan penggunaan data warehouse dalam operasional bisnis. Data warehouse nantinya digunakan untuk menganalisis penggunaan kendaraan bermotor, kepuasan konsumen serta menganalisis keuntungan yang diperoleh setiap bulannya. Berdasarkan skenario tersebut buatlah rancangan skema database dalam bentuk diagram ERD. Rancangan dapat dibuat dengan menggunakan aplikasi draw.io atau aplikasi lainnya yang sejenis.    
   **Jawab :**  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_ERD.png)  

2. Berdasarkan diagram ERD yang sudah dibuat pada nomor 1, buatlah berbagai tabel dengan kriteria sebagai berikut:  
    1. Menggunakan Citus dalam pembuatan tabel.  
       **Jawab :**  
        a. Membuat network  
        ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_create_network.png)  
        b. Membuat dan menjalankan container citus koor, citus worker 1, citus worker 2, dan container postgres  
        ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_create_container.png)  
        c. Masuk ke Postgres dan cek apakah sudah ada nodes yang terhubung  
        ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_check_nodes.png)  
        d. Menambahkan nodes untuk dihubungkan ke citus koor dan cek kembali list node yang terhubung  
        ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_add_nodes.png)  
        e. Create table dan insert data  
          - brands  
          ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_create_insert_brands.png)  
          - motorcycles  
          ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_create_insert_motorcycles.png)  
          - customers  
          ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_create_insert_customers.png)  
          - feedbacks  
          ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_create_insert_feedbacks.png)  
          - transactions  
          ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_create_insert_transactions.png)  
          - profit  
          ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_create_insert_profit.png)  
    2. Menerapkan replication.  
       **Jawab :**  
        ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_replication.png)  
    3. Menerapkan sharding.  
       **Jawab :**  
        a. Cek dulu shard tables  
        ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_check_shards.png)  

        b. Membuat sharding  
          - brands  
          ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_shard_brands.png)  
          - motorcycles  
          ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_shard_motorcycles.png)  
          - customers  
          ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_shard_customers.png)  
          - feedbacks  
          ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_shard_feedbacks.png)  
          - transactions  
          ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_shard_transactions.png)  
          - profit  
          ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_shard_profit.png)  

        c. Lihat Table di masing-masing worker  
          - Motorcycles 
            - Citus Worker 1  
              ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_motorcycles_worker_1.png)  
            - Citus Worker 2  
              ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_motorcycles_worker_2.png)  
          - Customers  
            - Citus Worker 1  
              ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_customers_worker_1.png) 
            - Citus Worker 2  
              ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_customers_worker_2.png)  
          - Transactions   
            - Citus Worker 1  
              ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_transactions_worker_1.png) 
            - Citus Worker 2  
              ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/12_Data-Warehouse-and-Data-Lake-Part-1/screenshots/output_priority_two_transactions_worker_2.png)  