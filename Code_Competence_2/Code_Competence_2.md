# Dokumentasi Pengerjaan

1. Persiapan lingkungan pengembangan (venv, dataset)
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/prepare_development.png)  

2. Data Ingestion dan Persiapan Data Lake / Data Werehouse (data_ingestion.py)  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/code_data_ingestion.png)  
   - output  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/output_data_ingestion_1.png)  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/output_data_ingestion_2.png)  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/output_data_ingestion_3.png)  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/output_data_ingestion_4.png)  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/output_data_ingestion_5.png)  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/output_data_ingestion_6.png)  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/output_data_ingestion_7.png)  

3. Data Ingestion dan Persiapan Data Lake / Data Werehouse (5 file)  
   - events.parquet  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/file_events_parquet.png)  
   - tickets.parquet  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/file_tickets_parquet.png)  
   - customers.parquet  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/file_customer_parquet.png)  
   - transactions.parquet  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/file_transactions_parquet.png)  
   - customer_feedback.parquet  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/file_customer_feedback_parquet.png)  

4. Transformasi Data dan Pemuatan ke Data Warehouse (data_transformation.py)  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/code_data_transformation.png)  
   - create bucket  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/create_bucket_cc2.png)  
   - output  
     - output terminal
     ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/output_data_transformation.png)  
     - GCP 
     ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/9d3b94a25d0db50605b6053753ecce834d537ef2/Code_Competence_2/screenshots/output_data_transformation_gcp.png)  
     - file Ticket_sold_per_event.parquet  
     ![preview](D:\Alterra Academy\tugas\data_ika-purwanti\Code_Competence_2\screenshots\output_file_ticket_sold_per_event.png)  
     - file Revenue_per_event.parquet  
     ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/output_file_revenue_per_events.png)  
     - File Feedback_analysis.parquet  
     ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/output_file_feedback_analisis.png)  

5. Orkestrasi Workflow dengan Apache Airflow  
   - Download file docker compose  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/download_file_docker_compose.png)  
   - Build custom docker image  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/build_custom_image.png)  
   - Sesuaikan image di file docker compose  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/change_custom_images.png)  
   - Run DAG  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/run_dag_cc2.png)  
   - Log task load  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/log_task_load_data.png)  
   - Log task transform  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/log_task_transform_data.png)  
   - Log task save to warehouse  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/log_task_save_warehouse.png)  
   - Graph  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/Code_Competence_2/screenshots/graph_dag_cc2.png)  
   
