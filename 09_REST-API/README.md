# (09) REST API

## Deskripsi
API (Application Programming Interface) merupakan sebuah metode komunikasi antara satu aplikasi dengan satu atau banyak aplikasi lainnya.  

**API Workflow Sederhana**  
Client -> Request -> Server/System -> Response  

### Contoh Implementasi API
1. Sebuah aplikasi multi platform client app. Aplikasi E-commerce yang memiliki aplikasi dalam platform web, android, dan iOS
2. Aplikasi e-commerce yang terhubung dengan sistem pembayaran dan ekspedisi
3. Register dan Login menggunakan akun Google, Facebook, dan lainnya.

## REST API
REST (Representational State Transfer) merupakan sebuah guideline dan rekomendasi untuk membentuk API dengan pemodelan 'real world object'. REST berbasis protokol HTTP.

**REST API Komponen**
- Endpoint
- Metode (GET, POST, PUT, DELETE)
- Header
- Body (data)

### Macam-macam HTTP Methods
1. **POST**  
   Digunakan untuk membuat/menambahkan data baru ke server.
2. **GET**  
   Digunakan untuk mendapatkan data dari server.
3. **PUT**  
   Digunakan untuk mengupdate/replace data secara keseluruhan di server.
4. **PATCH**  
   Digunakan untuk mengupdate/modify data sebagian di server.
5. **DELETE**  
   Digunakan untuk menghapus data yang ada diserver.

### Macam-macam HTTP Response Code yang sering dijumpai
1. **200 OK**, response berhasil.
2. **201 Created**, data berhasil dibuat.
3. **400 Bad Request**, server gagal memahami permintaan dari user.
4. **404 Not Found**, server web tidak dapat menemukan halaman yang diminta oleh user.
5. **401 Unauthorized**, server tidak memiliki kredensial autentikasi yang valid.
6. **405 Method Not Allowed**, server sudah menerima request HTTP, tetapi ia menolaknya.
7. **500 Internal Server Error**, terdapat error di server.

## JSON
JSON (JavaScript Object Notation) merupakan sebuah format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna.  

**Format JSON**  
{  
    "key": "value"  
}