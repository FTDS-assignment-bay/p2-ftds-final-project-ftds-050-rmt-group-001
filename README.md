<div align="center">
  <img src="SamRize_Logo.png" alt="SamRize Logo" width="200">
  <h1>Samsung Review Summarizer</h1>
  <p><i>Sistem Ringkasan Review Handphone Samsung Menggunakan Unsupervised Machine Learning (Topic Modelling)</i></p>
</div>

---

## 📌 Program Description
**Samsung Review Summarizer (SamRize)** adalah sistem yang dirancang untuk merangkum **strength** dan **weakness** dari produk handphone Samsung berdasarkan ulasan pengguna di Amazon. Sistem ini memanfaatkan pendekatan **Natural Language Processing (NLP)** dengan **FASTopic** sebagai metode **Unsupervised Topic Modelling** untuk mengekstrak topik utama dari teks ulasan tanpa proses pelabelan data.

---

## 📖 Problem Background
Produk handphone Samsung memiliki jumlah ulasan yang sangat besar di platform e-commerce seperti Amazon. Ulasan tersebut mengandung banyak informasi berharga terkait pengalaman pengguna, namun disajikan dalam bentuk teks panjang dan tidak terstruktur. Hal ini membuat calon pembeli maupun pihak bisnis kesulitan untuk memahami pola kelebihan dan kelemahan utama dari suatu produk secara cepat.

Membaca satu per satu ulasan membutuhkan waktu yang lama dan tidak efisien. Oleh karena itu, diperlukan sebuah sistem yang mampu merangkum opini pengguna secara otomatis dengan cara mengekstrak topik-topik utama yang sering dibahas dalam ulasan.

---

## 🎯 Project Objective
Tujuan dari proyek ini adalah:

- Mengembangkan sistem ringkasan review handphone Samsung berbasis NLP.
- Mengimplementasikan **FASTopic** sebagai metode topic modelling berbasis **unsupervised learning**.
- Menghasilkan ringkasan **strength dan weakness** untuk setiap tipe handphone Samsung.
- Mengevaluasi kualitas topik menggunakan **Coherence Score (c_v)**.

---

## 📊 Dataset Information

Dataset pada proyek ini diperoleh melalui proses web scraping menggunakan SimpleScraper dari halaman produk handphone Samsung di Amazon.  
Data hasil scraping disimpan dalam bentuk CSV dan kemudian melalui tahapan cleaning serta preprocessing sebelum digunakan untuk analisis dan pemodelan.

Dataset berisi kombinasi informasi spesifikasi produk dan ulasan teks pengguna, dengan kolom utama seperti:

- `model_name` -> nama tipe handphone  
- `price` -> harga produk  
- `battery` -> kapasitas baterai (mAh)  
- `ram` -> kapasitas RAM  
- `storage` -> kapasitas penyimpanan  
- `cpu_model` -> jenis prosesor  
- `screen_size` -> ukuran layar  
- `resolution` -> resolusi layar  
- `refresh_rate` -> refresh rate  
- `reviews` -> teks ulasan pengguna  
- `ratings` -> rating (1–5)
- `overall_ratings`

Karena keterbatasan scraping, jumlah review antar model tidak selalu seimbang. Selain itu, beberapa ulasan masih mengandung noise seperti pembahasan pengiriman atau penjual, sehingga diperlukan tahap preprocessing dan filtering tambahan sebelum modelling.

---

## ⚙️ Methodology & Pipeline

### 1. Data Acquisition
- Mengambil dataset produk dan reviews handphone Samsung menggunakan metode Scraping pada website E-Commerce Amazon. 
---
### 2. Data Cleaning
- Menggabungkan dataset hasil scraping BeautifulSoup dengan Simplescraper
- Imputasi data null
- Mengubah tipe data (dtypes)
- Memfilter review produk hanya yang berbahasa Inggris
- Melakukan validasi data menggunakan Great Expectation

---

### 3. Exploratory Data Analysis (EDA)

Tahap EDA dilakukan untuk memahami karakteristik data teks sebelum proses modelling.  
Beberapa analisis yang dilakukan meliputi:

- Distribusi jumlah review untuk setiap tipe handphone Samsung  
- Distribusi rating pengguna (strength vs weakness)  
- Analisis ketidakseimbangan jumlah review antar model  
- Sentence count distribution (panjang kalimat per review)  
- Word count distribution (jumlah kata per review)  
- WordCloud sebelum preprocessing untuk melihat noise kata umum (seller, shipping, return, dll)  
- WordCloud setelah preprocessing untuk melihat kata teknis yang lebih relevan (battery, screen, camera, charge, dll)  

---

### 4. Data Filtering
- Data difilter hanya untuk setiap produk handphone Samsung.
- Ulasan dibagi berdasarkan rating:
  - Strength (Kelebihan) -> rating 4 & 5
  - Weakness (Kelemahan) -> rating 1, 2, & 3

> Rating digunakan hanya sebagai **filter data**, bukan sebagai label supervised learning.

---

### 5. Text Preprocessing
- Case folding
- Pembersihan teks (URL, emoji, simbol, angka)
- Tokenization
- Stopword removal
- Lemmatization

---

### 6. Topic Modelling with FASTopic
- FASTopic digunakan untuk melakukan topic modelling secara **unsupervised**.
- Proses vectorization dilakukan secara implicit di dalam pipeline FASTopic melalui embedding-based text representation.
- Topic modelling dilakukan secara terpisah untuk:
  - Review kelebihan (strength)
  - Review kelemahan (weakness)

---

### 7. Model Evaluation
- Kualitas topik dievaluasi menggunakan **Coherence Score (c_v)**.
- Coherence score digunakan untuk:
  - Mengukur konsistensi semantik antar kata dalam satu topik
  - Menentukan jumlah topik yang optimal

---

## 🧠 Machine Learning Approach
- **Learning Type**: Unsupervised Machine Learning
- **Method**: Topic Modelling (FASTopic)
- **Vectorization**: Implicit embedding-based vectorization (built-in FASTopic)

---

## 📊 Project Output

[SamRize App](https://huggingface.co/spaces/fluqs1808/Final_Project_Samrize)

---

## 🛠️ Technology Stack & Libraries

| Library | Fungsi |
|---|---|
| SimpleScraper | Data Scraping |
| BeautifulSoup | Data Scraping |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| NLTK | Text preprocessing |
| FASTopic | Topic modelling |
| Gensim | Coherence score (c_v) |
| Matplotlib / Seaborn | Data visualization |
| WordCloud | Text visualization |

---

## 📂 Project Structure

```text
├── Deployment/               # Kumpulan file untuk deployment di HuggingFace
├── Data_Scraped/             # Kumpulan file json hasil scrapping dan script pembersihan
├── GX/                       # Script validasi data
├── EDA.ipynb                 # Notebook Explorayoty Data Analysis
├── modeling.ipynb            # Notebook implementasi FASTopic
└── README.md                 # Dokumentasi proyek
```

---

## 📩 Contact Information

Jika Anda memiliki pertanyaan mengenai proyek ini atau ingin berkolaborasi, silakan hubungi tim kami:

| Nama Anggota | Kontak | GitHub | LinkedIn|
| :--- | :--- | :--- | :--- |
| **Septa Fariza Mahandani** |septafariza@gmail.com | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Septafm15) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/septa-fariza-mahandani-54806b117/) |
| **Daniel Christopher Miarsa** | danielmiarsa@gmail.com | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Daniel-M2) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniel-cm21/) |
| **Kaydee Havel Gregory** | kaydee.havel.gregory@gmail.com | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/kaydeehg) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kaydee-havel-gregory-155420373/) |