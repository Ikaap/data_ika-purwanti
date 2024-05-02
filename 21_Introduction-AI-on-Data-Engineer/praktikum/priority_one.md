# Soal Prioritas 1

- Perintah pada prompt :  
  **Jawab :**  
  Buatkan skema database beserta relasi antar table dan query DDL untuk aplikasi e-learning  

- Output :  
  **Jawab :**  
  Tentu, berikut adalah skema database sederhana untuk aplikasi e-learning bersama dengan relasi antar tabel dan beberapa contoh query DDL (Data Definition Language):  

  Skema Database:  
  1. Tabel: Users
     - user_id (Primary Key)
     - username
     - password
     - email
     - role (misalnya: student, instructor, admin)
  2. Tabel: Courses
     - course_id (Primary Key)
     - course_name
     - instructor_id (Foreign Key ke user_id di tabel Users)
     - description
     - start_date
     - end_date
  3. Tabel: Enrollments
     - enrollment_id (Primary Key)
     - user_id (Foreign Key ke user_id di tabel Users)
     - course_id (Foreign Key ke course_id di tabel Courses)
     - enrollment_date
  4. Tabel: Lessons
     - lesson_id (Primary Key)
     - course_id (Foreign Key ke course_id di tabel Courses)
     - lesson_name
     - content
     - lesson_order
  5. Tabel: Quizzes
     - quiz_id (Primary Key)
     - lesson_id (Foreign Key ke lesson_id di tabel Lessons)
     - quiz_name
     - questions
  6. Tabel: Submissions
     - submission_id (Primary Key)
     - user_id (Foreign Key ke user_id di tabel Users)
     - quiz_id (Foreign Key ke quiz_id di tabel Quizzes)
     - submission_date
     - score

  Relasi antar tabel:  
  - Tabel Users memiliki relasi dengan tabel Enrollments melalui user_id.
  - Tabel Courses memiliki relasi dengan tabel Enrollments melalui course_id.
  - Tabel Courses memiliki relasi dengan tabel Lessons melalui course_id.
  - Tabel Lessons memiliki relasi dengan tabel Quizzes melalui lesson_id.
  - Tabel Users memiliki relasi dengan tabel Submissions melalui user_id.
  - Tabel Quizzes memiliki relasi dengan tabel Submissions melalui quiz_id.

  Contoh Query DDL (Data Definition Language):  
  1. Membuat tabel Users:  
     CREATE TABLE Users (  
        user_id INT PRIMARY KEY AUTO_INCREMENT,  
        username VARCHAR(50) UNIQUE NOT NULL,  
        password VARCHAR(50) NOT NULL,  
        email VARCHAR(100) UNIQUE NOT NULL,  
        role ENUM('student', 'instructor', 'admin') NOT NULL  
     );  
  2. Membuat tabel Courses:  
     CREATE TABLE Courses (  
        course_id INT PRIMARY KEY AUTO_INCREMENT,  
        course_name VARCHAR(100) NOT NULL,  
        instructor_id INT,  
        description TEXT,  
        start_date DATE,  
        end_date DATE,  
        FOREIGN KEY (instructor_id) REFERENCES Users(user_id)  
     );  
  3. Membuat tabel Enrollments:  
     CREATE TABLE Enrollments (  
        enrollment_id INT PRIMARY KEY AUTO_INCREMENT,  
        user_id INT,  
        course_id INT,  
        enrollment_date DATE,  
        FOREIGN KEY (user_id) REFERENCES Users(user_id),  
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)  
     );  
  4. Membuat tabel Lessons:  
     CREATE TABLE Lessons (  
        lesson_id INT PRIMARY KEY AUTO_INCREMENT,  
        course_id INT,  
        lesson_name VARCHAR(100) NOT NULL,  
        content TEXT,  
        lesson_order INT,  
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)  
     );  
  5. Membuat tabel Quizzes:  
     CREATE TABLE Quizzes (  
        quiz_id INT PRIMARY KEY AUTO_INCREMENT,  
        lesson_id INT,  
        quiz_name VARCHAR(100) NOT NULL,  
        questions TEXT,  
        FOREIGN KEY (lesson_id) REFERENCES Lessons(lesson_id)  
     );  
  6. Membuat tabel Submissions:  
     CREATE TABLE Submissions (  
        submission_id INT PRIMARY KEY AUTO_INCREMENT,  
        user_id INT,  
        quiz_id INT,  
        submission_date DATE,  
        score DECIMAL(5,2),  
        FOREIGN KEY (user_id) REFERENCES Users(user_id),  
        FOREIGN KEY (quiz_id) REFERENCES Quizzes(quiz_id)  
     );  
  
  Itulah beberapa contoh skema database, relasi antar tabel, dan query DDL untuk aplikasi e-learning. Anda dapat menyesuaikan skema ini sesuai dengan kebutuhan aplikasi Anda.

- Hasil :  
  **Jawab :**  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_priority_one_1.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_priority_one_2.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_priority_one_3.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_priority_one_4.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_priority_one_5.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_priority_one_6.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_priority_one_7.png)  
  ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/21_Introduction-AI-on-Data-Engineer/screenshots/output_priority_one_8.png)  

- Penjelasan :  
  **Jawab :**  
  ChatGPT memberikan output yang sesuai dengan input yang saya berikan yaitu membuatkan schema database untuk aplikasi e-learing yang dalam output tersebut terdapat 6 tables yang akan digunakan yaitu table users, courses, enrollments, lessons, quizzes, dan submissions dan sudah dijelaskan juga mengenai relasinya jadi memudahkan saat membuat ERD nya. Dengan menggunakan chatGPT dapat membantu tugas dari data engineer menjadi lebih efisien karena output yang diberikan bisa menjadi referensi dalam membuat schema dalam real kasus.   
