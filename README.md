<div align="center">
  <img src="img.png" alt="Samsung Review Summarizer Logo" width="200">
  <h1>Samsung Review Summarizer</h1>
  <p><i>Sistem Ringkasan Review Handphone Samsung Menggunakan Unsupervised Machine Learning (Topic Modelling)</i></p>
</div>

---

## 📌 Program Description
**Samsung Review Summarizer** adalah sistem yang dirancang untuk merangkum **kelebihan** dan **kelemahan** dari produk handphone Samsung berdasarkan ulasan pengguna di **Amazon**. Sistem ini memanfaatkan pendekatan **Natural Language Processing (NLP)** dengan **FASTopic** sebagai metode **Unsupervised Topic Modelling** untuk mengekstrak topik utama dari teks ulasan tanpa proses pelabelan data.

---

## 📖 Problem Background
Produk handphone Samsung memiliki jumlah ulasan yang sangat besar di platform e-commerce seperti Amazon. Ulasan tersebut mengandung banyak informasi berharga terkait pengalaman pengguna, namun disajikan dalam bentuk teks panjang dan tidak terstruktur. Hal ini membuat calon pembeli maupun pihak bisnis kesulitan untuk memahami **pola kelebihan dan kelemahan utama** dari suatu produk secara cepat.

Membaca satu per satu ulasan membutuhkan waktu yang lama dan tidak efisien. Oleh karena itu, diperlukan sebuah sistem yang mampu **merangkum opini pengguna secara otomatis** dengan cara mengekstrak topik-topik utama yang sering dibahas dalam ulasan.

---

## 🎯 Project Objective
Tujuan dari proyek ini adalah:

- Mengembangkan sistem ringkasan review handphone Samsung berbasis NLP.
- Mengimplementasikan **FASTopic** sebagai metode topic modelling berbasis **unsupervised learning**.
- Menghasilkan ringkasan **kelebihan dan kelemahan** untuk setiap tipe handphone Samsung.
- Mengevaluasi kualitas topik menggunakan **Coherence Score (c_v)**.

---

## 📊 Dataset Information
Dataset yang digunakan berasal dari **Amazon Product Reviews** untuk kategori handphone Samsung. Data kemudian difilter dan diproses sebelum dilakukan pemodelan.

(**Belum Lengkap)**
---

## ⚙️ Methodology & Pipeline

### 1. Data Acquisition
- Mengambil dataset **Amazon Product Reviews** untuk produk handphone Samsung menggunakan metode Scraping.

---
### 2. Data Cleaning

**Belum Lengkap**

---

### 3. Exploratory Data Analysis (EDA)

**Belum Lengkap**

---

### 4. Data Filtering
- Data difilter hanya untuk **setiap produk handphone Samsung**.
- Ulasan dibagi berdasarkan rating:
  - **Pros (Kelebihan)** -> rating **4 & 5**
  - **Cons (Kelemahan)** -> rating **1, 2, & 3**

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
- Proses vectorization dilakukan **secara implicit** di dalam pipeline FASTopic melalui **embedding-based text representation**.
- Topic modelling dilakukan secara terpisah untuk:
  - Review kelebihan (pros)
  - Review kelemahan (cons)

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
Output sistem berupa ringkasan topik utama yang merepresentasikan opini pengguna untuk setiap tipe handphone Samsung, meliputi:

- Topik kelebihan produk
- Topik kelemahan produk

Contoh hasil:
> **Samsung Galaxy A Series**  
> **Kelebihan:** 
> **Kelemahan:**

**Belum Lengkap**

---

## 🛠️ Technology Stack & Libraries

| Library | Fungsi |
|---|---|
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| NLTK | Text preprocessing |
| FASTopic | Topic modelling |
| Gensim | Coherence score (c_v) |
| Matplotlib / Seaborn | Data visualization |
| WordCloud | Topic visualization |

---

## 📂 Project Structure

**Belum Lengkap**