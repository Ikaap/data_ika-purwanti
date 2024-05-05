from integration_openai import generate
import pandas as pd

data = pd.read_csv(f"D:/Alterra Academy/tugas/data_ika-purwanti/22_Implementation-AI-on-Data-Engineer/praktikum/source/Data Penjualan.csv")
prompt = f"Berdasarkan data berikut : \n{data}\n1. berilah analisis yang berfokus pada analisis tren penjualan, segmentasi pelanggan, dan prediksi penjualan.untuk mendapatkan insight dari data tersebut."
result = generate(prompt)
print("Perintah : \n", prompt)
print("output : \n", result)

