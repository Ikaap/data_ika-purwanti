# Data Definition Language (DDL)

1. Create database alta_online_shop.  
   **Jawab :**  
   ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_database.png)  

2. Dari schema Olshop yang telah kamu kerjakan di, Implementasikanlah menjadi table pada MySQL.
    1. Create table user.  
    **Jawab :**  
    ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_table_user.png)  
    2. Create table product, product type, operators, product description, payment_method.  
    **Jawab :**  
    - product type  
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_table_product_types.png)  
    - product description
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_table_product_desc.png)  
      - menambahkan FK di table product description yang berelasi 1-to-1 dengan table product  
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_alter_table_product_desc.png)  
    - operator
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_table_operator.png)  
    - payment method
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_table_payment_methods.png)  
    - product
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_table_product.png)  
    3. Create table transaction, transaction detail.  
    **Jawab :**  
    - transaction
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_table_transaction.png)  
    - transaction detail
      ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_table_transaction_detail.png)  

3. Create tabel kurir dengan field id, name, created_at, updated_at.  
   **Jawab :**  
    ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_table_kurir.png)  

4. Tambahkan ongkos_dasar column di tabel kurir.  
   **Jawab :**  
    ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_alter_table_kurir.png)  

5. Rename tabel kurir menjadi shipping.  
   **Jawab :**  
    ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_rename_table_kurir.png)  

6. Hapus / Drop tabel shipping karena ternyata tidak dibutuhkan.  
   **Jawab :**  
    ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_drop_table_shipping.png)  

7. Silahkan menambahkan entity baru dengan relation 1-to-1, 1-to-many, many-to-many. Seperti:
    1. 1-to-1: payment method description.  
    **Jawab :**  
    - create table payment method description  
    ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_table_payment_method_description.png)  
    - menambahkan FK di table payment method description yang berelasi 1-to-1 dengan table payment methods  
    ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_alter_table_payment_method_description.png)  
    2. 1-to-many: user dengan alamat.  
    **Jawab :**  
    - menghapus kolom alamat dulu di table user  
    ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_drop_column_address_in_table_user.png)  
    - create table address  
    ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_table_address.png)  
    3. many-to-many: user dengan payment method menjadi user_payment_method_detail.  
    **Jawab :**  
    - create table user payment method detail  
    ![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/output_create_table_user_payment_method_detail.png)  


## ERD DLL
![preview](https://github.com/Ikaap/data_ika-purwanti/blob/main/08_Relational-Database/screenshots/ERD_DLL.png)  