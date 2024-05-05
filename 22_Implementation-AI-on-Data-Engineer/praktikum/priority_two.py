from integration_openai import generate

prompt = "Buatkan SQL query untuk menghitung total penjualan per kategori produk setiap bulan di table transaksi yang memiliki kolom tanggal transaksi, jumlah penjualan (qty), harga, jenis kategori produk, total"
result = generate(prompt)
print("Perintah : \n", prompt)
print("output : \n", result)
