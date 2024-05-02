# Soal Prioritas 2

- Perintah pada prompt :  
  **Jawab :**  
  menurut schema database di atas, buatkan query membuat view yang menghasilkan data submission dan quis dari user pada masing-masing course yang sudah diikuti  

- Output :  
  **Jawab :**  
  Anda dapat membuat view yang menggabungkan data dari tabel Submissions dan Quizzes untuk setiap user pada setiap course yang telah diikuti. Berikut adalah contoh query untuk membuat view tersebut:  

  CREATE VIEW UserSubmissions AS  
  SELECT  
      u.username AS username,  
      c.course_name AS course_name,  
      q.quiz_name AS quiz_name,  
      s.submission_date AS submission_date,  
      s.score AS score  
  FROM  
      Users u  
  JOIN  
      Enrollments e ON u.user_id = e.user_id  
  JOIN  
      Courses c ON e.course_id = c.course_id  
  JOIN  
      Lessons l ON c.course_id = l.course_id  
  JOIN  
      Quizzes q ON l.lesson_id = q.lesson_id  
  LEFT JOIN  
      Submissions s ON u.user_id = s.user_id AND q.quiz_id = s.quiz_id  
  ORDER BY  
      u.username, c.course_name, q.quiz_name;  

  Penjelasan:  
  - Query ini menggabungkan tabel Users, Enrollments, Courses, Lessons, Quizzes, dan Submissions menggunakan operasi JOIN.
  - Mencocokkan user dengan kursus yang diikuti dan kemudian menghubungkannya dengan kuis melalui pelajaran.
  - Menggunakan LEFT JOIN dengan Submissions untuk memastikan bahwa bahkan jika pengguna belum mengirimkan jawaban, data mereka tetap ditampilkan dalam view.
  - Mengurutkan data berdasarkan username, nama kursus, dan nama kuis.  

  Setelah menjalankan query di atas, Anda akan membuat view baru yang disebut "UserSubmissions" yang berisi data submission dan quiz dari setiap pengguna pada setiap kursus yang telah diikuti.


- Hasil :  
  **Jawab :**  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_priority_two_1.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_priority_two_2.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_priority_two_3.png)  

- Penjelasan :  
  **Jawab :**  
  ChatGPT memberikan output yang sesuai dengan input yang saya berikan yaitu membuatkan query untuk create view dengan menampilkan data yang saya minta. Dengan membuat view dapat memudahkan kita untuk melihat data berdasarkan kriteria yang diinginkan, jadi tinggal memanggil view nya saja.  
  - keterbatasan/kekeurangn :  
    Hanya memberikan output sesuai dengan input prompt yang diberikan. ChatGPT tidak memberikan contoh pemanggilan view nya, walaupun masih berhubungan dengan prompt yang saya inputkan.  
