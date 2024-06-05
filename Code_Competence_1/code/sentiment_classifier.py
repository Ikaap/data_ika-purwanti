import pandas as pd

class SentimentClassifier:
    def __init__(self):
        self.file_source = "D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_1/data_source/file.csv"
    
    def load_data(self):
        df_all_data = pd.read_csv(self.file_source)
        return df_all_data
    
    def classify_sentiment(self, data_all):
        df_tweets_good = data_all[data_all['labels'] == 'good']
        df_tweets_bad = data_all[data_all['labels'] == 'bad']
        df_tweets_neutral = data_all[data_all['labels'] == 'neutral']
        
        return df_tweets_good, df_tweets_bad, df_tweets_neutral
    
    def save_to_csv(self, df_tweets_good, df_tweets_bad, df_tweets_neutral):
        try:
            df_tweets_good.to_csv('D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_1/file/sentiment_good.csv', index=False)
            df_tweets_bad.to_csv('D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_1/file/sentiment_bad.csv', index=False)
            df_tweets_neutral.to_csv('D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_1/file/sentiment_neutral.csv', index=False)
            
            print("Data berhasil disimpan ke dalam file CSV: sentiment_good.csv, sentiment_bad.csv, dan sentiment_neutral.csv")
        except:
            print("Data tidak berhasil disimpan ke dalam file CSV")
    
    def summarize_counts(self, df_tweets_good, df_tweets_bad, df_tweets_neutral):
        counts = [len(df_tweets_good), len(df_tweets_bad), len(df_tweets_neutral)]
        df_counts = pd.DataFrame({'Kategori': ['Good', 'Bad', 'Neutral'], 'Jumlah Tweets': counts})
        df_counts.to_csv('D:/Alterra Academy/tugas/data_ika-purwanti/Code_Competence_1/file/sentiment_counts.csv', index=False)
        print("Data berhasil disimpan ke dalam file CSV: sentiment_counts.csv")


data_sentiment_tweets = SentimentClassifier()
load_Data = data_sentiment_tweets.load_data()
df_tweets_good, df_tweets_bad, df_tweets_neural = data_sentiment_tweets.classify_sentiment(load_Data)
data_sentiment_tweets.save_to_csv(df_tweets_good, df_tweets_bad, df_tweets_neural)
data_sentiment_tweets.summarize_counts(df_tweets_good, df_tweets_bad, df_tweets_neural)