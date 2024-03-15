# Soal Eksplorasi 


1. Eksplorasi API RentABook :
   - Pelajari dokumentasi API dari RentABook: https://app.swaggerhub.com/apis-docs/sepulsa/RentABook-API/1.0.0  
   - Identifikasi endpoint yang tersedia dan fungsinya.
   **Jawab :**  
     - Authentication  
       - GET /token, digunakan untuk mendapatkan access token ketika client berhasil untuk proses authentication (login/register).
     - Client
       - GET /client/{id}, digunakan untuk mendapatkan data client berdasarkan id.
       - PUT /client/{id}, digunakan untuk mengupdate data client berdasarkan id.
       - DELETE /client/{id}, digunakan untuk menghapus data client berdasarkan id.
       - GET /client, digunakan untuk mendapat semua data client.
       - POST /client, digunakan untuk menambahkan (create) data client baru.
     - User
       - GET /user/{id}, digunakan untuk mendapatkan data user berdasarkan id.
       - PUT /user/{id}, digunakan untuk mengupdate data user berdasarkan id.
       - DELETE /user/{id}, digunakan untuk menghapus data user berdasarkan id.
       - GET /user, digunakan untuk mendapat semua data user.
       - POST /user, digunakan untuk menambahkan (create) data user baru.
     - Book
       - GET /book/{id}, digunakan untuk mendapatkan data buku berdasarkan id.
       - PUT /book/{id}, digunakan untuk mengupdate data buku berdasarkan id.
       - DELETE /book/{id}, digunakan untuk menghapus data buku berdasarkan id.
       - GET /book, digunakan untuk mendapat semua data buku.
       - POST /book, digunakan untuk menambahkan (create) data buku baru.
     - Rent
       - GET /rent/{id}, digunakan untuk mendapatkan data transaksi sewa buku berdasarkan id.
       - GET /rent, digunakan untuk mendapat semua transaksi sewa buku book.
       - POST /rent, digunakan untuk menambahkan (create) data transaksi sewa buku baru.

2. Implementasi 4 Method pada RentABook API :
   - Lakukan request dengan method GET, POST, PUT, dan DELETE pada endpoint yang tersedia di RentABook API.  
   **Jawab :**  
     - Client
       - GET all  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_client_get_all.png)  
       - GET by id  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_client_get_by_id.png)  
       - POST  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_client_post.png)  
       - PUT  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_client_put.png)  
       - DELETE  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_client_delete.png)  
     - User
       - GET all  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_user_get_all.png)  
       - GET by id  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_user_get_by_id.png)  
       - POST  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_user_post.png)  
       - PUT  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_user_put.png)  
       - DELETE  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_user_delete.png)  
     - Book
       - GET all  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_book_get_all.png)  
       - GET by id  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_book_get_by_id.png)  
       - POST  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_book_post.png)  
       - PUT  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_book_put.png)  
       - DELETE  
       ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/09_REST-API/screenshots/output_exploration_book_delete.png)  