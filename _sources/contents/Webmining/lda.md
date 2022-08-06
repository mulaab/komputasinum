# Pemodelan Topik  LDA

# https://petamind.com/understanding-latent-dirichlet-allocation-lda/


https://medium.com/analytics-vidhya/topic-modeling-with-latent-dirichlet-allocation-lda-196c287e221

https://github.com/raffg/harry_potter_nlp

https://bab2min.github.io/tomotopy/v0.12.2/en/

https://www.analyticsvidhya.com/blog/2021/06/part-18-step-by-step-guide-to-master-nlp-topic-modelling-using-lda-probabilistic-approach/  the best........................................................................................................

https://datascienceplus.com/topic-modeling-and-latent-dirichlet-allocation-lda/

implementasi

https://www.youtube.com/watch?v=BaM1uiCpj_E

https://www.baeldung.com/cs/topic-modeling-coherence-score

https://highdemandskills.com/topic-model-evaluation/

Pada tutorial ini, kita akan belajar tentang pemodelan topik, beberapa aplikasinya dan juga lebih mendalam dibahas salah satu model tentang teknik Latent Direchlet Allocation (LDA)

Untuk mempelajari tutorial ini diharapkan memahami terlebih dahulu distribusi probabilitas multivariate.



## 2. Pemodelan Topik



### 2.1. Apa itu  Topic Modeling?

<div style="text-align: justify"> 
Dalam penambangan teks,  kumpulan dokumen, seperti posting blog atau artikel berita, yang telah dikumpulkan menjadi beberapa kelompok  sehingga kita dapat memahaminya secara terpisah. Pemodelan topik adalah metode untuk mengelompokkan dokumen dengan pembelajaran tak terawasi, mirip dengan pengelompokan pada data numerik, yang menemukan kelompok item pada suatu data  </div>

<div style="text-align: justify"> 
Ringkasnya, Topic modeling adalah metode pembelajaran terawasi dan inputnya adalah corpus dari suatu kumpulan dokumen dan untuk menghasilkan topik-topik tertentu. Setelah model topik dibuat, kita dapat menyatakan suatu dokumen sebagai kombinasi dari topik topik yang diperoleh.  Marilah lihat contoh berikut  </div>

![img](https://www.baeldung.com/wp-content/uploads/sites/4/2020/11/topic_modeling_1.png)



Pada contoh ini, setiap dokumen dihubungkan dengan setiap topik sesuai dengan bobot-bobotnya. Oleh karena itu, kita dapat merepresentasikan dokumen sebagai vektor, dimana kolom-kolomnya adalah derajat keterkaitan dengan setiap topik. 

Misalkan kita ingin memodelkan "Jurassic Park" sebagai kombinasi dari topik topik dalam proporsi seperti ini.

- Dinosaurs”: 97%
- “Amusement Parks”: 49%
- “Extinction”: 10%



Dalam kasus tersebut, representasi vektor dokumen ini menjadi [0.97, 0.49, 0.1]

Apaa yang telah kita bahas adalah pemodelan topik yang  dapat digunakan untuk mendapatkan **embedding vector** dari  suatu dokumen.



### 2.2. Applications

$$
\text{perplexity}(\text{test set } w) =
        \exp \left\{
        - \frac{\mathcal L( w)}{\text{count of tokens}}
        \right\}
$$

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

Algoritma ini daapat dipahami dalam dua karakteristik utuma

- **Every document is a mixture of topics**. We imagine that each document may contain words from several topics in particular proportions. For example, in a two-topic model we could say “Document 1 is 90% topic A and 10% topic B, while Document 2 is 30% topic A and 70% topic B.”
- **Every topic is a mixture of words**. For example, we could imagine a two-topic model of American news, with one topic for “politics” and one for “entertainment.” The most common words in the politics topic might be “President”, “Congress”, and “government”, while the entertainment topic may be made up of words such as “movies”, “television”, and “actor”. Importantly, words can be shared between topics; a word like “budget” might appear in both equally.

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





Algoritma pemodelan topik **Latent Dirichlet Allocation (LDA)**, dikembangkan oleh [**Blei et al.** ](http://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf). Algoritma ini memiliki dua karakteristik 

- **Setiap dokumen adalah gabungan dari topik-topik.**. Kita dapat membayangkan bahwa setiap setiap dokumen mungkin berisi kata-kata dari beberapa topik sesuai proporsinya. Misalkan, dalam model dua topik, kita dapat mengatakan Dokumen 1 adalah 90% topik A dan 10% topik B, kemudian dokumen 2 adalah 30 % topik A dan 70% topik B
- **Setiap tpik adalah gabungan dari kata kata**. Misalkan kita dapat membayangkan model dua topik dengan satu topik politik dan satu topik lainnya 'entartainment'.  Kata yang paling umum dalam topik politik mungkin  “President”, “Congress”, dan “government”, kemudian topik entertainment mungkin dibentuk dari kata kata seperti  “movies”, “television”, dan “actor”. Yang perlu diperhatikan, ada kata-kata dapat berada diantara kedua topik tersebut ; kata seperti  “budget” mungkin muncul pada kedua topik tersebut

## Kelebihan dan kekurangan dari LDA

LDA adalah model probabilistik generatif dari corpus. Dibandingkan dengan metode pemodelan topik lainnya seperti model unigram, Latent Semantic Analysis (LSA), dan Probabilistic Latent Semantic Analysis (pLSA) kelebihan dan kekurangannya LDA adalah sebagai berikut:

**Keuntungan**

- Daoat menemukan topik tersirat (latent topik) didalam dokumen-dokumen
- Pembelajaran terawasi  membutuhkan label sesungguhnya, yang mungkin tidak tersedia
- LDA mudah untuk dilatih
- LDA dapat dipasangkan dengan word2vec untuk mempertahankan representasi kata.
- LDA memberikan topik yang dapat ditafsirkan

**Kelemahan**

- Hanya menganggap dokumen sebagai kantong kata (bag of word) dan mengabaikan informasi sintaksis (misalnya urutan kata) dan informasi semantik (misalnya makna lain dari  kata tertentu)
- Banyaknya topik tetap
- Topik-topik tidak saling berkaitan ( Distribusi topik Dirichlet tidak dapat tidak dapat menangkap korelasi)
- Statik( tidak ada perubahan topik dari waktu ke waktue)



Kita akan masuk ke konsep pertama. LDA tidak memberikan jawaban yang jelas apakah suatu dokumen termasuk dalam topik tertentu karena dokumen dianggap sebagai campuran topik. Dalam satu dokumen, kita mungkin menemukan beberapa topik. Sebuah berita tentang krisis keuangan tahun 2008 dapat terdiri dari topik ekonomi, politik dan sosial, digabung dalam satu artikel yang membahas tentang nilai pasar, respon pemerintah dan dampak dari tingkat pengangguran yang tinggi. Sehingga misalkan dokument tersebut dapat terdiri dari 30% ekonomi, 60% politik, dan 10% topik sosial. Persentase masing-masing topik pada dokumen mewakili probabilitas dokumen terhadap topik tertentu Oleh karena itu, kita dapat membayangkan gabungan topik sebagai distribusi probabilitas seperti tabel berikut:



| news | economics | politics   | social    |
| ---- | --------- | ---------- | --------- |
| 1    | 0.1437888 | 0.02277825 | 0.8334330 |
| 2    | 0.3941526 | 0.26405274 | 0.3417947 |
| 3    | 0.2044885 | 0.44620952 | 0.3493020 |
| 4    | 0.4415087 | 0.27571751 | 0.2827738 |
| 5    | 0.4702336 | 0.22830737 | 0.3014590 |

Baris pertama dari berita 14% berpeluang ke berita  ekonomi , 2% berita politik dan 83% berita sosial. baris kedua memilik kemungkinan  39% berita ekonomi, 26% berita politik dan 34% berita sosial dan seterusnya. Semakin tinggi peluangnya berarti dokumen tersebut  news and so on. Peluang yang lebih tinggi berarti bahwa dokumen dapat diwakili oleh suatu topik .

Kata Latent di Latent Dirichlet Allocation mengacu pada struktur laten atau tersembunyi di dalam dokumen. Seperti yang telah kita lihat di bagian sebelumnya, kita secara jelas mengatakan  bahwa sekelompok kata dapat memiliki tema atau topik utama. Oleh karena itu, menurut prinsip kedua, topik adalah campuran kata-kata, di mana kata-kata tertentu memiliki asosiasi yang kuat dengan topik tertentu. Misalnya, kata Presiden memiliki sinyal kuat bahwa itu termasuk topik politik, atau kata Pinjaman dan Bunga memiliki sinyal kuat untuk topik ekonomi. Sama seperti sebuah dokumen memiliki distribusi probabilitas untuk setiap topik, sebuah topik juga memiliki distribusi probabilitas untuk setiap kata/istilah. LDA menganggap bahwa sebuah dokumen adalah kumpulan kata, sehingga kita tidak memperdulikan urutan kata. 

Model LDA model dientuk berdasarkan dua prinsip ini dan memiliki struktur seperti berikut: 

```{figure} ./images/ldastruc.jpg
---
height: 400px
name: directive-figa
---
Pemodelan Topik LDA
```



Notation:

- $\alpha$ = Paramter dirichlet untuk proporsi topi per-dokumen
- $\theta_d$ = Distribusi topik dari dokumen $d$
- $Z_{d,n}$ = Tanda suatu topik dengan kata ke $n$ pada dokumen $d$ 
- $W_{d,n}$ = Kata yang diamati dari kata ke-$n$ dalam dokumen $d$
- $\eta$ = hyperparameter topik
- $\beta_k$  = Distribusi kata-kata dari topik $k$ 
- $K$ = Kumpulan topik-topik
- $N$ = Kumapulan kata dalam dokumen
- $D$ = Kumpulan dokumen di corpus

LDA merupakan bagian  model bayesian hierarkis. Model bayesian memiliki prior dan posterior. Prior berarti distribusi probabilitas dari hal-hal tertentu sebelum kita melihat datanya. Sebagai contoh, kita mungkin percaya bahwa distribusi probabilitas untuk pelemparan dadu terdistribusi secara seragam, memiliki probabilitas kemunculan sama pada permukaan mata dadu tersebut. Kami mengasumsikan  ini  melempar dadu. Sedangkan probabilitas posterior mencerminkan distribusi probabilitas setelah kita  melempar dadu. Misalnya, setelah kita melempar dadu sebanyak 10.000 kali, angka 5 muncul lebih dari 5.000 kali. Ini dapat mengubah keyakinan kita bahwa nilai untuk setiap sisi berdistribusi  secara merata, dikarenakan ada satu  satu sisi dadu memiliki peluang tinggi kemunculannya.  Kita dapat menghitung probabilitas posterior menggunakan Teorema Bayes.  Konsep probabilitas prior dan posterior sangat penting untuk memahami proses LDA.

Model LDA terdiri dari 2 macam distribusi prior : distribusi probabilitas topik ke dokumen (probabilitas topik-dokumen) dan distribusi probabilitas kata ke topik (probabilitas topik-kata). Kedua Distribusi probabilitas prior tersebut tidak seragam atau berdistribusi normal, tetapi berdistribusi Dirichlet dengan paramete $\alpha$  dan parameter $\beta$  dan juga jumlah topik sebagai inputan.

Gambar berikut adalah ilustrasi distribusi Dirichlet untuk setiap topik pada setiap dokumen. Misalkan kita memiliki kumpulan dokumen dan kita yakin bahwa pada corpus kita memiliki 3 topik yang berbeda. Setiap titik mewakili satu dokumen dan setiap sisi segitiga mewakili satu topik. Posisi setiap dokumen mewakili distribusi probabilitas untuk setiap topik. Kami secara acak menetapkan posisi setiap dokumen berdasarkan distribusi probabilitasnya. Kita dapat melihat bahwa dokumen A memiliki kedekatan yang dekat dengan topik Sains. Hal ini menunjukkan bahwa dokumen A memiliki probabilitas tinggi untuk masuk ke topik Sains dan probabilitas rendah untuk masuk ke Politik atau Ekonomi. Sementara itu, dokumen B memiliki probabilitas tinggi untuk masuk dalam topik Ekonomi. Dokumen C terletak di antara Sains dan Politik, sehingga memiliki probabilitas yang agak sama untuk topik tersebut dan probabilitas rendah untuk topik Ekonomi. Topik D terletak di tengah segitiga, yang berarti memiliki peluang yang sama untuk ketiga topik.

```{figure} ./images/iluslda.png
---
height: 400px
name: directive-figa
---
Pemodelan Topik prior LDA
```

Tujuan LDA adalah untuk menjadikan setiap dokumen sedekat mungkin dengan topik tertentu, meskipun mungkin tidak selalu tercapai untuk semua dokumen. Jika gambar di atas menyatakan probabilitas prior untuk setiap dokumen untuk setiap topik, gambar berikut menggambarkan probabilitas posterior di mana semua dokumen memiliki hubungan yang kuat dengan topik tertentu. ilusldapos

```{figure} ./images/ilusldapos.png
---
height: 400px
name: directive-figa
---
Pemodelan Topik Posterior LDA
```
Kita jadikan distribusi probabilitasnya kedalam tabel berikut:

| document | sciences | politics | economy |
| -------- | -------- | -------- | ------- |
| A        | 0.8      | 0.10     | 0.10    |
| B        | 0.1      | 0.05     | 0.85    |
| C        | 0.1      | 0.85     | 0.05    |
| D        | 0.1      | 0.80     | 0.10    |

Distribusi prior kedua adalah probabilitas suatu topik terhadap kata kata tertentu yang dimiliki: probabilitas kata-topik. Prior ini berkaitan dengan kata-kata apa yang mewakili topik tertentu? Apakah ada kata-yang memiliki hubungan kuat dengan topik tertentu? Katakanlah kita memiliki 4 istilah: Presiden, Planet, Pasar, dan Energi. Setiap kata akan bertindak sebagai tepi segitiga. Namun, karena kita memiliki lebih dari 3 suku, bentuk distribusinya bukan segitiga lagi, melainkan tetrahedron. Gambar berikut mengilustrasikan secara acak dengan distribusi Dirichlet antara topik dan kata-kata:

```{figure} ./images/ilusldtopkata.png
---
height: 400px
name: directive-figa
---
Pemodelan Topik-kata LDA
```

Some of the well-known topic modelling techniques are Latent Semantic Analysis (LSA), Probabilistic Latent Semantic Analysis (PLSA), Latent Dirichlet Allocation (LDA), and Correlated Topic Model (CTM). In this article, we will focus on LDA, a popular topic modelling technique. 

Contents [[hide](https://petamind.com/understanding-latent-dirichlet-allocation-lda/#)]

- [1 Latent Dirichlet Allocation (LDA)](https://petamind.com/understanding-latent-dirichlet-allocation-lda/#Latent_Dirichlet_Allocation_LDA)
- [2 LDA Algorithm](https://petamind.com/understanding-latent-dirichlet-allocation-lda/#LDA_Algorithm)
- [3 Hyper parameters in LDA](https://petamind.com/understanding-latent-dirichlet-allocation-lda/#Hyper_parameters_in_LDA)
- [4 Coherence score/ Topic Coherence score](https://petamind.com/understanding-latent-dirichlet-allocation-lda/#Coherence_score_Topic_Coherence_score)
- [5 Data preprocessing for LDA](https://petamind.com/understanding-latent-dirichlet-allocation-lda/#Data_preprocessing_for_LDA)
- 6 Some real-world novel applications of LDA
  - [6.1 Share this:](https://petamind.com/understanding-latent-dirichlet-allocation-lda/#Share_this)

## **LATENT DIRICHLET ALLOCATION (LDA)**



Before getting into the details of the **Latent Dirichlet Allocation** model, let’s look at the words that form the name of the technique. The word **‘Latent’** indicates that the model discovers the ‘yet-to-be-found’ or hidden topics from the documents. **‘Dirichlet’** indicates LDA’s assumption that the distribution of topics in a document and the distribution of words in topics are both [Dirichlet distributions](https://en.wikipedia.org/wiki/Dirichlet_distribution). ‘**Allocation’** indicates the distribution of topics in the document.  

LDA assumes that documents are composed of words that help determine the topics and maps documents to a list of topics by assigning each word in the document to different topics. The assignment is in terms of conditional probability estimates as shown in figure 2. In the figure, the value in each cell indicates the probability of a word *wj* belonging to topic *tk*. ‘*j*’ and ‘*k*’ are the word and topic indices respectively. It is important to note that LDA ignores the order of occurrence of words and the syntactic information. It treats documents just as a collection of words or a bag of words. 

