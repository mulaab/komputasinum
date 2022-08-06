# Pengantar

Pada tutorial ini, kita akan belajar tentang pemodelan topik, beberapa aplikasinya dan juga lebih mendalam dibahas salah satu model tentang teknik Latent Direchlet Allocation (LDA)

Untuk mempelajari tutorial ini diharapkan memahami terlebih dahulu distribusi probabilitas multivariate.



## 2. Pemodelan Topik



### 2.1. Apa itu  Topic Modeling?

Dalam penambangan teks,  kumpulan dokumen, seperti posting blog atau artikel berita, yang telah dikumpulkan menjadi beberapa kelompok  sehingga kita dapat memahaminya secara terpisah. Pemodelan topik adalah metode untuk mengelompokkan dokumen dengan pembelajaran tak terawasi, mirip dengan pengelompokan pada data numerik, yang menemukan kelompok item pada suatu data

Ringkasnya, Topic modeling adalah metode pembelajaran terawasi dan inputnya adalah corpus dari suatu kumpulan dokumen dan untuk menghasilkan topik-topik tertentu. Setelah model topik dibuat, kita dapat menyatakan suatu dokumen sebagai kombinasi dari topik topik yang diperoleh.  Marilah lihat contoh berikut

![img](https://www.baeldung.com/wp-content/uploads/sites/4/2020/11/topic_modeling_1.png)



Pada contoh ini, setiap dokumen dihubungkan dengan setiap topik sesuai dengan bobot-bobotnya. Oleh karena itu, kita dapat merepresentasikan dokumen sebagai vektor, dimana kolom-kolomnya adalah derajat keterkaitan dengan setiap topik. 

Misalkan kita ingin memodelkan "Jurassic Park" sebagai kombinasi dari topik topik dalam proporsi seperti ini.

- Dinosaurs”: 97%
- “Amusement Parks”: 49%
- “Extinction”: 10%



Dalam kasus tersebut, representasi vektor dokumen ini menjadi [0.97, 0.49, 0.1]

Apaa yang telah kita bahas adalah pemodelan topik yang  dapat digunakan untuk mendapatkan **embedding vector** dari  suatu dokumen.



### 2.2. Applications



Topic modeling memiliki beberapa bentuk aplikasi yang menarik diantaranya adalah :

- Memahami bidang
- Menemukan perubahan atau trend baru dalam bidang kita
- Melakukan Encode text sebagai  [vector embeddings](https://www.baeldung.com/cs/convert-word-to-vector)
- Search Personalization
- Pemodelan users’ preference untuk pencarian 
- [Membandingkan dokumen](https://www.baeldung.com/cs/ml-similarities-in-text)
- Menemukan penulis dari dokumen tertentu
- Memprediksi dan menginterpretasikan aktifitas sosial and Interpretation of social activity
- [Analisa Sentimen](https://www.baeldung.com/cs/sentiment-analysis-practical)
- Mesin penterjemah

### 2.3. Teknik Pemodelan Topik



terdapat beberapa teknik yang sering digunakan untuk pemodelan topik  diantaranya adalah

- [NMF](https://towardsdatascience.com/topic-modeling-articles-with-nmf-8c6b2a227a45) (Non-Negative Matrix Factorization)
- [LSA](https://en.wikipedia.org/wiki/Latent_semantic_analysis) (Latent Semantic Analysis)
- [PLSA](https://towardsdatascience.com/topic-modelling-with-plsa-728b92043f41) (Probabilistic Latent Semantic Analysis)
- LDA (Latent Dirichlet Allocation)
- [lda2vec](https://paperswithcode.com/method/lda2vec)
- [tBERT](https://paperswithcode.com/paper/tbert-topic-models-and-bert-joining-forces) (Topic BERT)



## 3. Latent Dirichlet Allocation

### 3.1. Introduction

Latent Dirichlet Allocation (LDA) adalah model a **statistical generative ** yang menggunkan Dirichlet distributions.

Kita mulai dengan corpus dari  $M$  dokumen dan berapak banyak topik $K$ yang akan ditemukan dalam corpus-corpus tersebut. Keluaran dari topik model adalah $M$ dokumen tersebut dinyatkan sebagai kombinasi dari $K$ topik

Singkatnya, semua yang dilakukan algoritma algoritma pemodelan topik adalah menemukan bobot hubungan antara dokumen dan topik dan antara topik dan kata-kata 

Ada tiga  *hyperparameter* pada  LDA:

 

1. *Faktor padat Dokumen-topik*  ($\alpha $) artinya proporsi topik-topik setiap dokumen
2. *Faktor pada topik-kata* ($\beta$) artinya banyaknya kata-kata yang ada pada setiap topik
3. *Banyaknya topik yang diharapkan*($K$). artinya berapa banyak topik yang dihasilkan dari kumpulan dokumen-dokumen tersebut



Hyperparameter $\alpha$  menentukan seberapa banyak subyek yang terkandung pada dokumen. Semakin rendah nilai $\alpha$  menunjukkan dokumen memilki beberapa subjek didalamnya, kemudian semakin tinggi nilai $\alpha$ menunjukkan bahwa dokumen-dokumen tersebut akan memiliki banyak topik didalamnya.  

Hyperparemeter $\beta$ menentukan seberapa banyak distribusi kata pada masing masing subjek atau topik. Subyek dengan nilai $\beta$ rendah biasanya memiliki beberapa kata, selanjutnya topik dengan nilai $\beta$ tinggi akan memungkinkan memiliki banyak kata-kata.

 Hyperparameter $K$ menyatakan banyaknya topik yang ada pada kumpulan dokumen. $K$ biasanya ditentukan nilainya berdasarkan pakar bidang tertentu. Pilihan lainnya  adalah untuk melatih model LDA dengan beberapa variasi dari nilai $K$ kemudian menghitung  'Coherence Score.'

Berikut contoh pemodelan topik *Blei et al.* dimana kata-kata untuk setiap topik (arts, budgets, children, and education) . Teks yang berwarna pada bagian bawah dari gambar adalah menunjukkan suatu dokumen dengan terdiri dari beberapa kumpulan kata kata dari beberapa topik



```{figure} ./images/topikmodel.png
---
height: 500px
name: directive-figa
---
Pemodelan Topik
```





The parameters shown previously are:

1. the number of topics is equal to **num_topics**
2. the *[distribution of the]* number of words per topic is handled by **eta**
3. the *[distribution of the]* number of topics per document is handled by **alpha**

To print topics found, use the following:



```
0: 0.024*"base" + 0.018*"data" + 0.015*"security" + 0.015*"show" + 0.015*"plan" + 0.011*"part" + 0.010*"activity" + 0.010*"road" + 0.008*"afghanistan" + 0.008*"track" + 0.007*"former" + 0.007*"add" + 0.007*"around_world" + 0.007*"university" + 0.007*"building" + 0.006*"mobile_phone" + 0.006*"point" + 0.006*"new" + 0.006*"exercise" + 0.006*"open"1: 0.014*"woman" + 0.010*"child" + 0.010*"tunnel" + 0.007*"law" + 0.007*"customer" + 0.007*"continue" + 0.006*"india" + 0.006*"hospital" + 0.006*"live" + 0.006*"public" + 0.006*"video" + 0.005*"couple" + 0.005*"place" + 0.005*"people" + 0.005*"another" + 0.005*"case" + 0.005*"government" + 0.005*"health" + 0.005*"part" + 0.005*"underground"2: 0.011*"government" + 0.008*"become" + 0.008*"call" + 0.007*"report" + 0.007*"northern_mali" + 0.007*"group" + 0.007*"ansar_dine" + 0.007*"tuareg" + 0.007*"could" + 0.007*"us" + 0.006*"journalist" + 0.006*"really" + 0.006*"story" + 0.006*"post" + 0.006*"islamist" + 0.005*"data" + 0.005*"news" + 0.005*"new" + 0.005*"local" + 0.005*"part"
```



*[the first 3 topics are shown with their first 20 most relevant words]*Topic 0 seems to be about military and war.
Topic 1 about health in India, involving women and children.
Topic 2 about Islamists in Northern Mali.

To print the % of topics a document is about, do the following:



```
[(14, 0.9983065953654187)]
```



The first document is 99.8% about topic 14.

Predicting topics on an unseen document is also doable, as shown below:



```
[(1, 0.5173717951813482), (3, 0.43977106196150995)]
```



This new document talks 52% about topic 1, and 44% about topic 3. Note that 4% could not be labelled as existing topics.



https://rpubs.com/Argaadya/topic_lda

https://morioh.com/p/2a01aa34c758 lda pakai python

https://medium.com/analytics-vidhya/topic-modelling-using-lda-aa11ec9bec13 pakai python

# https://www.baeldung.com/cs/latent-dirichlet-allocation

https://builtin.com/data-science/dirichlet-distribution








