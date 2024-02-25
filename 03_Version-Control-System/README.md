# (03) Version Control System (Git dan Github)

## Deskripsi
Mengatur versi dari source code program disebut dengan **Versioning**  

**Tools**
- Version Control System (VCS)
- Source Code Manager (SCM)
- Revision Control System (RCS)

## Git dan Github
Git merupakan salah satu version control system populer yang digunakan para developer untuk mengembangkan software secara bersama-sama.  
**Github** merupakan Git hosting service yang membantu developer menyimpan dan mengelola kode yang dibuat, serta melacak dan mengontrol perubahan pada kode tersebut.

## Perintah-perintah yang biasa digunakan di Github
- **git init**, digunakan untuk inisialisasi repository di local.
- **git clone**, digunakan untuk mendownload repository dari server ke device user.
- **git config**, digunakan untuk proses configurasi ketika baru pertama kali menggunakan github.
- **git status**, digunakan untuk menampilkan informasi/status file di repository lokal.
- **git add**, digunakan untuk menambahkan file baru ke staging area sebelum dipush ke server.
- **git commit**, digunakan untuk menyimpan perubahan direpository local.
- **git diff**, digunakan untuk melihat perbedaan perubahan pada file.
- **git stash**, digunakan untuk menyimpan perubahan yang tidak ingin di commit. Untuk mengambil perubahan dari stash dapat menggunakan perintah **git stash apply** dan **git stash pop**.
- **git log**, digunakan untuk melihat list commit.
- **git checkout**, digunakan untuk berpindah dari satu branch ke branch lainnya.
- **git reset**, digunakan untuk mengatur ulang keadaan repository ke commit tertentu. Ada 2 jenis reset yaitu soft dan hard.
- **git push**, digunakan untuk mengirim file ke repository remote (server).
- **git pull**, digunakan untuk mendapatkan update dari repository server ke local.
- **git branch**, digunakan untuk membuat sebuah branch.
- **git merge**, digunakan untuk menggabungkan dua branch menjadi satu.
- **pull request**, digunakan untuk mengabungkan dua branch menjadi satu namun code harus direview terlebih dahulu sebelum digabungkan.

## Workflow
**Tips**
1. Buat branch development dari master/main
2. Hindari direct edit ke branch development
3. Merge branch feature hanya ke development 
4. Merge branch development ke branch master/main jika proses development sudah selesai
