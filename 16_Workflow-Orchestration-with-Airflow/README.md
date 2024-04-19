# (16) Workflow Orchestration with Apache Airflow

## Deskripsi  

## Workflow  
**Workflow** merupakan sekumpulan tugas yang terhubung satu sama lain untuk mencapai tujuan tertentu. Workflow nantinya akan digambarkan kedalam sebuah DAG dalam apache airflow.
- **Task** merupakan sebuah tugas yang diselesaikan dari sebuah workflow.
- **Operator** merupakan sebuah komponen yang digunakan untuk menjalankan sebuah task.

## Directed Acyclic Graph (DAG)
**DAG** merupakan sebuah graf yang digunakan untuk menggambarkan sebuah workflow.
### Sifat-sifat DAG
- Bersifat satu arah
- Dapat terdiri dari berbagai task dengan operator yang berbeda
- Satu task dapat melakukan percabangan ke task lainnya
- Beberapa task dapat menuju satu task yang sama

## Apache Airflow
**Apache Airflow** merupakan sebuah tools yang dapat digunakan untuk mengelola workflow. Installasi apache airflow dapat dilakukan dengan 2 cara yaitu emnggunakan [PyPI](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html) dan [Dokcer](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).
### Alasan menggunakan Apache Airflow
- Apache Airflow memiliki fitur yang lengkap
- Memiliki setup yang mudah
- Apache Airflow bersifat open source
- Apache Airflow juga bersifat scalable

### Istilah yang sering ditemukan dalam implementasi DAG
- **XCOM**, merupakan sebutan dari cross communication yang memungkinkan antar task dapat bertukar atau mengirim data. Biasanya XCOM digunakan untuk push(memberikan) dan pull(mengambil) sebuah value. XCOM cocok digunakan untuk data dengan ukuran kecil dan sederhana.
- **Taskflow**, dapat digunakan untuk membuat sebuah data pipeline di airflow.


