# Soal Prioritas 1

1. Sebutkan dan jelaskan berbagai tools yang dapat digunakan untuk meningkatkan kualitas dari sebuah data!  
   **Jawab :**  
   - Deequ  
     Deequ adalah perpustakaan open source untuk kualitas data di atas platform Spark. Deequ cocok untuk menguji data dalam jumlah besar karena kekuatan pemrosesan dan fleksibilitas Spark. Deequ mengerjakan konsep saran dan verifikasi kendala.
   - dbt Core   
     dbt Core adalah platform development data pipeline dengan fitur SQL dinamis, templating, dan pemodelan. Salah satu fitur yang sering diabaikan adalah pengujian otomatis, yang dapat menjalankan pengujian skala penuh, pemeriksaan kualitas data, dan validasi. Fitur utama dbt Core termasuk kemampuan pengujian dbt dimulai dari pengujian validasi skema yang siap pakai, selain itu dbt juga terkenal dengan semua database populer, data warehouse, dan platform data.  
   - MobyDQ    
     MobyDQ adalah framework data quality yang awalnya dikembangkan oleh Ubisoft Entertainment. Fitur yang dimiliki MobyDQ meliputi framework data quality yang memperhatikan empat indikator utama: kelengkapan, kesegaran, latensi, dan validitas. MobyDQ juga memungkinkan user menjalankan pengujian menggunakan GraphQL API-nya.  Selain itu dapat menjalankan MobyDQ menggunakan demo yang disertakan dengan data pengujian dan sumber data seperti Hive, PostgreSQL, dan MySQL.
   - Great Expectations  
     Great Expectations (GX) adalah salah satu tools data quality paling populer. Fitur utama GX meliputi, daftar Ekspektasi yang lengkap untuk menetapkan "keadaan data yang diharapkan", dukungan kontrak data dengan otomatisasi pemeriksaan kualitas data, pencatatan hasil dari waktu ke waktu, dan penyediaan ringkasan pengujian, koneksi langsung dengan agregator metadata sumber dan katalog data, serta mesin orkestrasi seperti Airflow, Meltano, dan Dagster, dan fleksibilitas dengan backend penyimpanan.  
   - Soda Core  
     Soda Core adalah library open source Python yang dibuat untuk memungkinkan keandalan data di platform data. Fitur dari Sode Core meliputi, dapat menemukan data yang tidak mencukupi dengan masuk langsung ke sumber data Anda dan menjalankan pemeriksaan kualitas data di tempatnya, dapat menjalankan pemeriksaan kualitas data dengan menggunakan pemindaian terprogram, dan dapat terhubung ke orchestration tools dan workflow engines seperti Airflow, Dagster, dan dbt Core.  


2. Terdapat berbagai cara dalam meningkatkan kualitas dari sebuah data (data quality) seperti data governance, data profiling dan data matching. Dari berbagai cara tersebut, sebutkan berbagai tantangan yang perlu diperhatikan!  
   **Jawab :**  
   1. Mendefinisikan peran dan tanggung jawab yang jelas  
      Salah satu tantangan utama data governance adalah memastikan bahwa setiap orang memiliki peran yang jelas dan izin yang sesuai. Ini bisa menjadi proses yang memakan waktu, terutama di organisasi yang lebih besar. 
   2. Menetapkan kebijakan dan prosedur  
      Membuat dan menerapkan kebijakan dan prosedur data governance sangat penting untuk memastikan bahwa data dikelola dan digunakan dengan tepat. 
   3. Menyeimbangkan aksesibilitas dan keamanan  
      Memastikan bahwa pengguna memiliki akses terhadap data yang mereka perlukan sambil menjaga keamanan dan privasi data dapat menjadi tindakan penyeimbang yang rumit.
   4. Manajemen perubahan  
      Saat inisiatif data governance diterapkan, organisasi mungkin perlu beradaptasi dengan proses, teknologi, dan cara kerja baru.
   5. Pemantauan dan perbaikan berkelanjutan  
      Membangun mekanisme untuk melacak kemajuan, mengukur keberhasilan, dan mengidentifikasi area yang perlu ditingkatkan adalah hal yang penting.  
   6. Anggaran dan sumber daya  
      Menerapkan dan memelihara framework data governance memerlukan investasi yang signifikan dalam hal waktu, sumber daya, dan anggaran.    
   7. Skalabilitas  
      Seiring pertumbuhan organisasi, framework data harus mampu berkembang dan beradaptasi untuk mengakomodasi pengguna baru, sumber data, dan kasus penggunaan.  
   8. Kualitas dan konsistensi data  
      Memastikan keakuratan, kelengkapan, dan konsistensi data merupakan aspek penting dalam data governance. Hal ini memerlukan penetapan proses dan mekanisme untuk mengidentifikasi, memantau, dan menyelesaikan masalah kualitas data.  
   9. Kompleksitas dan keragaman data  
      Tantangan dalam data profiling adalah menangani kompleksitas dan keragaman sumber data, terutama di era big data dan cloud computing. Hal ini dapat mempersulit integrasi, perbandingan, dan analisis data secara efektif.  
  10. Kinerja sistem
      Proses pembuatan profil data memerlukan komputasi yang intensif karena melibatkan sejumlah besar perbandingan kolom – di dalam, di antara, dan juga di seluruh tabel. Hal ini memerlukan sejumlah besar sumber daya komputasi seperti memori dan ruang disk, serta lebih banyak waktu untuk menyelesaikan dan membangun hasil keluaran.  
  11. Membatasi cakupan hasil
      Karena laporan profil data dihasilkan dengan meringkas dan menggabungkan nilai data, harus ada ambang batas yang menentukan tingkat ringkasan yang akan diterapkan. Ini membantu mendapatkan hasil yang lebih bermakna dan fokus.  
  12. Self-service data profiling tools  
      Mengingat betapa kompleksnya pembuatan profil data secara komputasi, maka tidak tersedianya perangkat lunak pembuatan profil data layanan mandiri merupakan tantangan umum yang dihadapi.  
  13. Proses pencocokan data yang berpotensi rumit  
      Jika proses pengumpulan data dan standardisasi entri belum ada, prosedur standarisasi (kualitas data) pra-set data kurang kuat, pendekatan pencocokan mungkin memerlukan logika yang lebih kompleks untuk mengekstrak semua data yang berpotensi cocok.  
  14. Membutuhkan standarisasi data  
      Data besar, khususnya, dapat menimbulkan masalah melalui format data yang tidak sesuai dengan jumlah data yang banyak. Dengan demikian, proses harus memperhitungkan bagaimana bagian data ini harus ditangani.  
  15. Kesalahan dalam pencocokan data  
      Pencocokan data rentan terhadap kesalahan. Akurasi pencocokan data jarang diuji di banyak sistem integrasi data meskipun ada masalah ini. Hal ini menjadi perhatian besar karena pengukuran diperlukan untuk memahami dan meningkatkan akurasi pencocokan data.   


## Referensi :
1. Artikel dari atlan.com - 6 Popular Open Source Data Quality Tools To Know in 2024: Overview, Features & Resources
2. Artikel dari atlan.com - 10 Data Governance Challenges & How to Overcome Them!
3. Artikel dari linkedin.com - What are the common challenges and pitfalls of data profiling and how do you overcome them?
4. Artikel dari dataladder.com - What is data profiling: Scope, techniques, and challenges
5. Artikel dari spotfire.com - What is data matching? 