from integration_openai import generate
import pandas as pd

data = pd.read_csv(f"D:/Alterra Academy/tugas/data_ika-purwanti/22_Implementation-AI-on-Data-Engineer/praktikum/source/Data Penjualan.csv")
prompt = f"Berdasarkan data berikut : \n{data}\n1. berilah analisis (jenis produk paling banyak terjual dengan jumlahnya, dan analisis lainnya yang bisa didapatkan dari data yang ada) berdasarkan data tersebut.\n2. Dari analisis yang didapat buat rencana implementasi strategi untuk meningkatkan penjualan atau efisiensi operasional.\n3. Cara meningkatkan kepuasan pelanggan dan loyalitas."
result = generate(prompt)
print("Perintah : \n", prompt)
print("output : \n", result)
