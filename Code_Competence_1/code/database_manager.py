from pymysql import connect
import pandas as pd

class DatabaseManager:
    def __init__(self):
        self.connection = connect(
            host="localhost",
            port=3308,
            db="sentiment_chatgpt",
            user="root",
            password=""
        )
        if self.connection:
            print("Koneksi Berhasil")
    
    def create_tables(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS sentiments(
                                sentiment_id INT AUTO_INCREMENT PRIMARY KEY, 
                                sentiment_label VARCHAR(15) NOT NULL
                                );
                            """)
            
            cursor.execute("""CREATE TABLE IF NOT EXISTS tweets(
                                id  INT AUTO_INCREMENT PRIMARY KEY, 
                                text TEXT NOT NULL,
                                sentiment_id INT NOT NULL,
                                FOREIGN KEY (sentiment_id) REFERENCES sentiments (sentiment_id) ON DELETE NO ACTION ON UPDATE CASCADE
                                );
                            """)
            
            self.connection.commit()
            print("Table Berhasil dibuat!")
        except :
            print("Tidak Berhasil Membuat Table!!")    
    
    def insert_from_csv(self):
        df_data_all = pd.read_csv("D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_1/data_source/file.csv")
        
        cursor = self.connection.cursor()
        try:
            # Insert data sentiment
            df_data_sentiment = df_data_all['labels'].unique()
            for label in df_data_sentiment:
                cursor.execute("""INSERT INTO sentiments(sentiment_label)
                                VALUES(%s)""", (label,))
            
            # Insert data tweet
            for index, data in df_data_all.iterrows():
                if data['labels'] == 'neutral':
                    sentiment_id = 1
                elif data['labels'] == 'good':
                    sentiment_id = 2
                elif data['labels'] == 'bad':
                    sentiment_id = 3
                cursor.execute("""INSERT INTO tweets(text, sentiment_id)
                                VALUES(%s, %s)""", (data['tweets'], sentiment_id))
                
            self.connection.commit()
            print("Insert Data Berhasil!")
        except Exception as e:
            self.connection.rollback()
            print("Gagal Insert Data:", e)


database_manage = DatabaseManager()
database_manage.create_tables()
database_manage.insert_from_csv()