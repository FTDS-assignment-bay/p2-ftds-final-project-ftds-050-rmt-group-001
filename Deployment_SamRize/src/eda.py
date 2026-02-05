import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image #Python image library

def run():
    # membuat title
    st.title('Samsung Phone Ratings Analysis Based on Various Variable')

    # membuat subheader
    st.header('EDA for Samsung Phone Ratings Analysis')

    # menambahkan deskripsi
    st.write('In this page, we gonna analyze the phone ratings based on price and phone specifications likes battery life, storage capacity, and other specifications')

    df = pd.read_csv('src/clean.csv')

    # EDA 1
    st.subheader('Top 5 Phone Model Based on Rating')

    top5_models = (
        df[['model_name', 'overall_rating']]
        .drop_duplicates()
        .sort_values(by='overall_rating', ascending=False)
        .head(5)
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(
        data=top5_models,
        x='model_name',
        y='overall_rating',
        palette='viridis',
        order=top5_models['model_name'],
        ax=ax
    )

    for p in ax.patches:
        ax.annotate(
            f"{p.get_height():.2f}",
            (p.get_x() + p.get_width()/2., p.get_height()),
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.xticks(rotation=30)
    ax.set_xlabel("Model")
    ax.set_ylabel("Overall Rating")
    st.pyplot(fig)

    st.write('**Analysis:**')
    st.write("""
    - **Galaxy S25 FE** memiliki *overall rating* tertinggi sebesar **4.60**, menunjukkan tingkat kepuasan pengguna paling tinggi di antara lima model teratas.
    - **Galaxy Z Flip7 FE** dan **Galaxy Z Fold7** berada tepat di bawahnya dengan rating yang sama, yaitu **4.50**, menandakan kualitas pengalaman pengguna yang setara meskipun berbeda segmen dan desain.
    - **Samsung Galaxy S22+** dan **Samsung Galaxy S23 FE** memperoleh rating **4.40** dan **4.30**, yang tetap menunjukkan performa dan kepuasan pengguna yang sangat baik.
    - **Secara keseluruhan**, perbedaan rating antar model relatif kecil, mengindikasikan bahwa kelima ponsel memiliki tingkat kepuasan pengguna yang konsisten.
    """)

    # EDA 2
    st.subheader("Phone Price Distribution")

    # Harga unik per model
    price_per_model = df[['model_name', 'price']].drop_duplicates()

    # Buat figure
    fig, ax = plt.subplots(figsize=(8, 6))

    sns.histplot(
        price_per_model['price'],
        bins=30,
        kde=True,
        ax=ax
    )

    ax.set_title("Price Distibution")
    ax.set_xlabel("Price")
    ax.set_ylabel("Frequency")

    st.pyplot(fig)

    st.write('**Analysis:**')
    st.write("""
    - Sebagian besar model handphone berada pada **rentang harga rendah hingga menengah**, dengan konsentrasi tertinggi di kisaran **200**–**450**$.
    - Jumlah model dengan **harga tinggi relatif sedikit**, dibandingkan dengan model di segmen harga menengah.
    - Distribusi harga terlihat **miring ke kanan (right-skewed)**, menandakan adanya beberapa model dengan harga sangat tinggi.
    - Garis **KDE** menunjukkan bahwa pasar didominasi oleh **model dengan harga terjangkau hingga menengah**.
    - Secara keseluruhan, terdapat **variasi harga yang cukup besar**, namun mayoritas model difokuskan pada **segmen pasar menengah**.
    """)


    # EDA 3
    st.subheader("Correlation Between Phone Specifications and Price")

    numeric_cols = [
        'price',
        'ram',
        'battery',
        'weight_gr',
        'cpu_speed',
        'storage'
    ]

    df_corr = df[numeric_cols]

    # Hitung korelasi
    corr_matrix = df_corr.corr()

    # Plot heatmap
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5,
        ax=ax
    )

    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)

    st.write('**Analysis:**')
    st.write("""
    - **Harga handphone** memiliki korelasi paling kuat dengan **kecepatan CPU (0,61)** dan **kapasitas storage (0,57)**, menunjukkan bahwa performa prosesor dan ruang penyimpanan menjadi faktor utama penentu harga.
    - **RAM** memiliki korelasi **sedang** terhadap harga (**0,36**), sehingga masih berkontribusi namun tidak sekuat CPU dan storage.
    - **Battery** dan **berat perangkat (`weight_gr`)** menunjukkan korelasi yang **relatif lemah** terhadap harga, menandakan bahwa kedua faktor ini tidak terlalu berpengaruh langsung pada harga jual.
    - Terdapat **korelasi negatif lemah** antara **battery** dan **`cpu_speed` (-0,20)**, yang mengindikasikan bahwa ponsel dengan performa tinggi tidak selalu dibekali kapasitas baterai yang lebih besar.
    """)

    # EDA 4
    st.subheader("Price vs Rating")

    # Ambil data unik
    df_harga_rating = df[['model_name', 'price', 'overall_rating']].drop_duplicates()

    # Buat figure
    fig, ax = plt.subplots(figsize=(10, 7))

    sns.scatterplot(
        data=df_harga_rating,
        x='overall_rating',
        y='price',
        ax=ax
    )

    # Tambahkan label model di tiap titik
    for _, row in df_harga_rating.iterrows():
        ax.text(
            row['overall_rating'] + 0.01,
            row['price'],
            row['model_name'],
            fontsize=8,
            alpha=0.7
        )

    ax.set_title("Pricevs Rating")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Price")

    st.pyplot(fig)

    st.write('**Analysis:**')
    st.write("""
    - Scatter plot menunjukkan **tidak adanya korelasi linear yang kuat** antara **harga** dan **rating** handphone.
    - Ponsel dengan **rating di atas 4.3** tersebar di berbagai **rentang harga**, mulai dari kelas menengah hingga sangat mahal.
    - Terlihat satu model dengan **harga sangat tinggi**, yaitu **Z Fold 7** (di atas **2000**), namun ratingnya **tidak jauh berbeda** dibandingkan model dengan harga lebih rendah seperti **Galaxy Z Flip7 FE** dan **Galaxy S25 FE**.
    - Temuan ini mengindikasikan bahwa **harga mahal tidak selalu menjamin rating yang jauh lebih baik**.
    - Kepuasan pengguna cenderung lebih dipengaruhi oleh **keseimbangan fitur, performa, dan value for money**, bukan harga semata.
    """)

    # EDA 5
    st.subheader("All Handphone Model Specification")

    spec_comparison = (
        df.groupby('model_name')
        .agg({
            'price': 'max',
            'battery': 'max',
            'ram': 'max',
            'storage': 'max',
            'screen_size': 'max',
            'refresh_rate': 'max',
            'weight_gr': 'max'
        })
        .round(2)
        .sort_values(by='price', ascending=False)
        .reset_index()
    )

    # Tampilkan sebagai tabel interaktif
    st.dataframe(
        spec_comparison,
        hide_index=True,
        height=500
    )


    # EDA 6
    st.subheader("WordCloud Positive Review Before Preprocessing")

    # Penglabelan rating
    df['rating_label'] = np.where(
        df['ratings'].between(4, 5),
        'Positive',
        'Negative'
    )

    # Gabungkan teks review positif
    text_positive = df[df['rating_label'] == 'Positive']['reviews'].dropna().values
    text_positive = " ".join(text_positive)

    # Generate WordCloud
    wordcloud_positive = WordCloud(
        background_color='black',
        colormap='cool',
        collocations=False,
        width=2000,
        height=1000
    ).generate(text_positive)

    # Plot WordCloud
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.imshow(wordcloud_positive)
    ax.axis('off')
    ax.set_title("Positive Review Words", fontsize=20)

    st.pyplot(fig)

    st.write('**Analysis:**')
    st.write("""
    - WordCloud menunjukkan bahwa kata **“phone”** dan **“screen”** paling dominan, menandakan bahwa perangkat secara keseluruhan dan **kualitas layar** merupakan aspek yang paling sering diapresiasi pengguna.
    - Kata-kata seperti **“good”**, **“great”**, **“excellent”**, dan **“love”** mencerminkan **sentimen kepuasan pengguna yang tinggi**.
    - Kemunculan kata **“battery”** dan **“camera”** mengindikasikan bahwa **daya tahan baterai** dan **kualitas kamera** menjadi faktor tambahan yang memengaruhi ulasan positif.
    - Secara keseluruhan, WordCloud menunjukkan bahwa **kombinasi kualitas layar, performa, dan fitur utama** menjadi alasan utama tingginya kepuasan pengguna terhadap ponsel Samsung.
    """)


    # EDA 7
    st.subheader("WordCloud Negative Review Before Preprocessing")
    text_negative = (
        df[df['rating_label'] == 'Negative']['reviews']
        .dropna()
        .values
    )
    text_negative = " ".join(text_negative)

    # Generate WordCloud
    wordcloud_negative = WordCloud(
        background_color='black',
        colormap='flare',
        collocations=False,
        width=2000,
        height=1000
    ).generate(text_negative)

    # Plot WordCloud
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.imshow(wordcloud_negative)
    ax.axis('off')
    ax.set_title("Negative Review Words", fontsize=20)

    st.pyplot(fig)

    st.write('**Analysis:**')
    st.write("""
    - WordCloud negatif didominasi oleh kata **“phone”**, **“screen”**, dan **“time”**, yang menunjukkan bahwa keluhan paling sering berkaitan dengan **fungsi perangkat** dan **pengalaman penggunaan dalam jangka waktu tertentu**.
    - Kata-kata seperti **“issue”**, **“problem”**, **“locked”**, dan **“unlock”** mengindikasikan adanya **masalah sistem**, khususnya terkait **penguncian perangkat atau keamanan**.
    - Kemunculan kata **“Amazon”**, **“seller”**, **“return”**, dan **“refund”** menunjukkan bahwa sebagian review negatif dipengaruhi oleh **pengalaman pasca-pembelian**, seperti layanan penjual, proses pengembalian, atau kondisi produk (misalnya **refurbished**).
    - Kata **“battery”**, **“camera”**, dan **“network”** menandakan adanya keluhan terkait **performa perangkat**.
    - Secara keseluruhan, insight ini menunjukkan bahwa **review negatif tidak hanya disebabkan oleh spesifikasi teknis**, tetapi juga oleh **kualitas unit produk dan layanan distribusi**.
    """)

    # EDA 8
    st.subheader("WordCloud Positive Review After Preprocessing")
        
    st.image(
        "src/positive after.png",  # ganti dengan path PNG kamu
        caption="WordCloud Positive Review After Preprocessing",
        use_container_width=True
    )

    st.write('**Analysis:**')
    st.write("""
    - WordCloud pada **strength reviews** setelah proses **text preprocessing** menampilkan kata-kata yang lebih **spesifik dan informatif** dibandingkan sebelumnya.
    - Kata-kata umum atau **noise** seperti nama brand, istilah transaksi, dan **stopwords** telah berkurang, sehingga aspek produk yang benar-benar penting menjadi lebih menonjol.
    - Kata **“screen”**, **“camera”**, **“battery”**, **“charge”**, **“fast”**, **“feature”**, dan **“quality”** muncul lebih dominan, menunjukkan apresiasi pengguna terhadap **layar**, **kamera**, **daya tahan baterai**, dan **fitur perangkat secara keseluruhan**.
    - Hasil ini mengindikasikan bahwa proses **preprocessing berhasil** dalam menghilangkan kata tidak relevan dan menyoroti **selling points utama produk**.
    """)


    # EDA 9
    st.subheader("WordCloud Negative Review After Preprocessing")
    st.image(
        "src/negative after.png",  # ganti dengan path PNG kamu
        caption="WordCloud Positive Review After Preprocessing",
        use_container_width=True
    )
    
    st.write('**Analysis:**')
    st.write("""
    - WordCloud pada **weakness reviews** setelah proses **text preprocessing** menampilkan kata-kata yang lebih **terfokus pada masalah dan keluhan pengguna**.
    - Setelah **noise** dan kata umum dihapus, istilah yang muncul menjadi lebih **spesifik** dan merepresentasikan **pain points utama** pengguna.
    - Kata seperti **“issue”**, **“problem”**, **“return”**, **“fix”**, **“receive”**, **“call”**, **“charge”**, dan **“repair”** muncul dominan, menunjukkan keluhan terkait **kerusakan perangkat**, **baterai/pengisian daya**, serta **layanan purna jual** (pengembalian dan perbaikan).
    - Dibandingkan **strength reviews** yang menonjolkan fitur dan performa, **weakness reviews** lebih menekankan pada **pengalaman negatif dan hambatan penggunaan**.
    """)

if __name__ == '__main__':
    run()