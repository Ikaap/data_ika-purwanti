# (10) Docker

## Deskripsi
**Virtual Machine** merupakan sebuah representasi virtual dari sebuah komputer.  
**Container** merupakan sebuah unit yang membungkus kode beserta dependensi sehingga aplikasi dapat dijalankan dengan cepat dan andal di berbagai environment.

## Perbedaan Antara Virtual Machine dan Container
1. Virtual Machine : Abstraksi di hardware fisik  
   Container       : Abstraksi di layer aplikasi
2. Virtual Machine : Menggunakan kapasitas yang lebih banyak  
   Container       : Menggunakan kapasitas yang lebih kecil/sedikit
3. Virtual Machine : Booting lebih lambat  
   Container       : Booting lebih cepat
4. Virtual Machine : Digunakan untuk menjalankan komputer dalam bentuk virtual  
   Container       : Digunakan untuk membungkus sebuah aplikasi. Satu container untuk satu aplikasi

## Docker
Docker merupakan sebuah container manager yang dapat digunakan untuk mengelola aplikasi dalam bentuk container. Cara kerja docker yaitu :  
Client (mengirimkan perintah yang diinginkan) -> Docker Host (perintah diproses di docker daemon dapat berupa membuat image lalu membuat container dengan image yang sebelumnya sudah dibuat atau di ambil dari registry/docker hub) <- Registry/docker hub (tempat tersedia berbagai image, extensions, dan plugin )

## Dockerfile Cheat sheet
1. **FROM**
   Digunakan untuk mendapatkan image dari docker registry.  
2. **RUN**
   Digunakan untuk menjalankan command ketika membuat container.  
3. **ENV**
   Digunakan untuk menentukan environment variable di dalam container.  
4. **ADD**
   Digunakan untuk menyalin file dengan prosess yang lain.   
5. **COPY**
   Digunakan untuk meng copy file ke dalam container.  
6. **WORKDIR**
   Digunakan untuk menentukan working directory.  
7. **ENTRYPOINT**
   Digunakan untuk menjalankan command ketika container sudah dibuat.  
8. **CMD**
   Digunakan untuk menjalankan commanf tapi dapat diganti.  

## Docker Basic Commands
Beberapa basic command yang sering digunakan di docker, antara lain :
1. docker pull
2. docker push
3. docker run
4. docker exec
5. docker logs
6. docker inspect
7. docker volume create
8. docker volume ls
9. docker network create
10. docker network connect

## Docker Volume
Docker Volume merupakan sebuah mekanisme penyimpanan data yang dapat digunakan agar data tetap ada ketika container sudah dihapus.

### Keunggulan Docker Volume
- Backup dan migrasi lebih mudah
- Dapat dibagi lebih aman dengan container lain
- Menambahkan fungsionalitas lain

## Docker Network
Docker Network merupakan sebuah jaringan yang dapat digunakan antar container untuk berkomunikasi satu sama lain.

**Cara Kerja :** 
Docker network akan dijadikan sebagai jembatan yang menghubungkan 2 container atau lebih menggunakan jaringan yang sama yang sudah dibuat sebelumnya.

## Docker Compose
Docker Compose merupakan sebuah mekanisme untuk mengelola berbagai container. Contohnya Container Orchestration. Docker Compose dapat digunakan untuk menjalankan berbagai container dengan membuat file konfigurasi dalam format YAML.

### Macam-macam Tools Container Orchestration
1. Docker Compose
2. Docker Swarm
3. Kubernetes
4. Red Hat OpenShift