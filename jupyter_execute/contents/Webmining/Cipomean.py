#!/usr/bin/env python
# coding: utf-8

# # Pendugaa/Estimasi Parameter Populasi
# 
# Fokus dari pembahasan adalah pengembangan metode untuk menentukan estimasi titik dan interval dari parameter populasi
# 
# 
# ### Topik yang dibahas :
# 
# 
# - Penduga interval untuk selisih rata-rata dua populasi normal
# - Penduga interval untuk varians dari populasi normal
# - Penduga interval untuk rasio varians dua populasi normal
# - Metode Estimasi: metode momen dan metode kemungkinan maksimum
# - Penaksir titik dan interval untuk parameter binomial
# - Prediksi: melakukan estimasi pengamatan masa yang akan datang
# 
# ### Tujuan Pembelajaran:
# 
# Setelah mempelajari bab ini pembaca dapat memahami
# - Memahami peran estimasi dalam statistik terapan
# - Menentukan estimasi titik dan interval untuk berbagai parameter distribusi diskrit dan kontinu
# - Memahami konsep koefisien kepercayaan dan menafsirkan interval kepercayaan.
# - Memahami perbedaan antara signifikansi statistik dan praktis
# - Menerapakan bahasa python untuk menentukan interval kepercayaan dari
#   parameter dari berbagai distribusi.
#   
# Catatan: silahkan download slide kulish di [ppt](https://github.com/mulaab/saindata/tree/main/_sources/contents/Webmining/Estimasi_Paramter_fix.ppt)
# 
# Kita sering menghadapi masalah statistik dari seperti berikut: kita memiliki banyak atau besar objek populasi sehingga jika pengukuran dilakukan pada setiap objek maka tentunya kita akan memiliki distribusi dari pengukuran dari semua objek dalam populasi tersebut.  Karena kita tidak memungkinkan untuk melakukan pengukuran pada semua objek dalam populasi, distribusi ini tentu saja tidak diketahui. Hal terbaik yang dapat kita lakukan dalam praktiknya adalah memperkirakan berbagai karakteristik (atau biasa disebut sebagai parameter) dari informasi distribusi  terkandung dalam pengukuran yang dilakukan dalam sampel acak objek  populasi. Misalnya, jika kita ingin mengestimasi mean dan varians dari distribusi populasi,  kita dapat menggunakan rata-rata sampel dan varians sampel sebagai penduga untuk besaran-besaran tersebut. Jika kita ingin menaksir median populasi, kita dapat menggunakan median sampel. Tentu saja, parameter lain dari distribusi populasi seperti, standar deviasi, atau proporsi populasi dapat diperkirakan atau ditaksir dari pengukuran sample acak obyek yang telah dilakukan.  Hal inilah Masalah ini
# jenis adalah fokus dari bab ini.
# 
# KIta membahas dua macam penduga untuk paramater populasi, yaitu penduga titik dan penduga interval. Lebih tepatnya, misalkan  $(X_1,X_2, X_3 \ldots)$  adalah sample acak dari populasi yang memiliki parameter yang diharapkan, misalnya  $\theta$ . Jika $\hat \theta=\varphi(X_1,X_2,X_3 \ldots, X_n)$ adalah fungsi benilai tunggal (single-values) dari $X_1,X_2,X_3, \ldots,X_n$ sehingga $\hat \theta$  itu sendiri adalah variabel acak, maka kita menyebut $\theta$ sebagai statistik. Selanjutnya, jika 
# 
# $$
# E\left(\varphi\left(X_{1}, \ldots, X_{n}\right)\right)=E(\hat{\theta})=\theta
# $$
# 
# 
# kita sebut  $\hat \theta $ adalah unbiasaed estimator dari $\theta$. Statistik $\hat \theta $  biasnya disebut dengan estimator titik ( point estimator) untuk parameter $\theta$. Jika $\hat \theta_l= \varphi_l(X_1,X_2, \ldots,X_n)$ dan $\hat \theta_u= \varphi_u(X_1,X_2, \ldots,X_n)$ adalah dua statistik sehingga 
# 
# $$
# P\left(\hat{\theta}_{l}<\theta<\hat{\theta}_{u}\right)=1-\alpha \label{eq1}
# \tag{8.1.2}
# $$
# 
# kita katakan bahwa interval acak $(\hat \theta_l,\hat \theta_u)$ adalah $100(1-\alpha)\%$ interval kepercayaan untuk parameter $\theta$ . Pasangan statistik $(\hat \theta_l,\hat \theta_u)$ kadangkala disebut sebagai penduga interval (estimator interval) untuk $\theta$. Titik ujung  ($\hat \theta_l  $ dan $ \hat \theta_u$) dari interval kepercayaan $(\hat \theta_l,\hat \theta_u)$ kadangkala disebut batas kepercayaan  $100(1-\alpha)\%$ dari $\theta$  dan $\hat \theta_l  $ , $ \hat \theta_u$ masing masing disebut sebagai batas bawah kepercayaan dan batas atas kepercayaan. Probabilitas $1-\alpha$  dalam persamaan (8.1.2)  disebut  koefisien kepercayaan ( confidence coefficient) , sedangkan $ 100(1-\alpha)\%$ disebut tingkat kepercayaan (confidence level). Juga selisih $\hat \theta_l -\hat \theta_u$ disebut lebar interval kepercayaan.
# 
# 
# # Selang Kepercayaan ( Confidence Interval)
# Pada bagian ini akan membahas apa artinya selang kepercayaan(confidence interval). Maka kita akan melihat bagaimana kita akan mendefinisikan confident interval pada rata-rata populasi.
# Setelah itu, kita akan memahami arti dari selang kepercayaan untuk selisih antara dua  rata-rata dan dan diantara dua proporsi. Terakhir, kita akan membahas hubungan  antara  distribusi t dan selang kepercayaan.
# 
# ## Arti interval kepercayaan
# Kita dapat mendefinisikan interval kepercayaan (CI) sebagai seberapa besar kita tidak yakin tentang hasil uji statistik pada sampel jika diterapkan pada seluruh populasi. Definisi lain yang lebih sederhana dari interval kepercayaan sebagai kisaran nilai yang kita yakini.
# 
# Misalnya, kita dapat memilih secara acak 40 pria dan mengukur tinggi badan mereka. Kita tahu tinggi rata-ratanya adalah 175 cm, dan diperoleh standar deviasinya  20 cm. Jika kita memutuskan untuk menggunakan interval kepercayaan 95 persen, kita akan mendapatkan hasilnya yaitu 175 ± 6,2 cm, yang berarti bahwa
# 95 persen, kita akan menemukan orang-orang yang tingginya berada di antara
# 168,8 cm dan 181,2 cm. Kita akan melihat di bagian selanjutnya bagaimana kita
# menghitung angka ini.
# 
# ## Interval Kepercayaan untuk rata-rata Populasi
# Mengikuti contoh diatas, sekarang kita akan menghitung
# interval kepercayaan untuk rata-rata populasi  dengan
# angkah-langkah berikut:
# 1. Pilih interval kepercayaan yang dinginkan. Dalam kasus kami, itu adalah 95 persen.
# 2. Temukan nilai-z pada  tabel z. Pada kasus ini  adalah 1,96. 
# 3. Hitung rentang menggunakan $\bar{X} \pm Z \frac{s}{\sqrt{n}}$  dimana $ \bar X $ adalah rata-rata,  $z$ adalah nilai $z$ yang dipilih , $s$ adalah standar deviasi, dan $n$ adalah banyaknya pengamatan.  Sehingga kita mendapatkan $175 \pm 1.96 \frac{20}{\sqrt{40}}$ atau $175 \pm 6.2$
# 
# Sekarang, marilah kita lihat bagaimaan untuk mensimulasikan yang lebih komplek menggunakan Python. 
# 
# Referensi : Ebook-Statistics for Beginners in Data Science

# 

# In[1]:


import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import random


# Kita membuat  100 ribu data dengan  rata-rata 4
# dan standar deviasi 2.82

# In[2]:


shape, scale = 2.0, 2.0 
s = np.random.gamma(shape, scale, 100000)
mu = shape*scale
sigma = scale*np.sqrt(shape)
print(mu)
print(sigma)


# Setelah itu, kita hitung rata-rata sample dengan ukuran sample 500

# In[3]:


sample_mean = []
sample_size = 500
for j in range(0,5000):
    random_sample = random.choices(s, k=sample_size)
    sample_mean.append(sum(random_sample)/len(random_sample))


# Kemudian kita ploting data

# In[4]:


plt.figure(figsize=(20,10))
plt.hist(sample_mean, 200, density=True, color='lightgreen')
plt.show()


# Akhirnya kita mendapatkan interval kepercayaan pada grafik berikut

# In[5]:


plt.figure(figsize=(20,10))
plt.hist(sample_mean, 200, density=True, color='lightgreen')
plt.plot([mu,mu],[0, 3.2], 'k-', lw=4, color='blue')
plt.plot([mu-(1.96*sigma/np.sqrt(sample_size)),mu-(1.96*sigma/np.sqrt(sample_size))],[0, 3.2], 'k-', lw=2, color='black')
plt.plot([mu+(1.96*sigma/np.sqrt(sample_size)),mu+(1.96*sigma/np.sqrt(sample_size))],[0, 3.2], 'k-', lw=2, color='black')
plt.show()


# Seperti yang kita lihat diatas, interval kepercayaannnya adalah $4\pm 0.24792$  

# ## Estimasi titik untuk rata-rata populasi dan variansi
# Pada bagian ini kita bahas estimasi titik yang umum digunakan yaitu estimator untuk mean dan varians dari populasi. Misalkan, suatu populasi
# di mana variabel yang diukura adalah variabel X dengan nilai  variabel acak kontinu dan memiliki fungsi kepadatan probabilitas (p.d.f.) $f(x)$. Rata-rata populasi dan variansi dinyatakan sebagai berikut:
# 
# 
# $$ 
# \mu = \int _ { - \infty } ^ { \infty } x f ( x ) d x
# $$
# 
# dan 
# $$
# \sigma ^ { 2 } = \int _ { - \infty } ^ { \infty } ( x - \mu ) ^ { 2 } f ( x ) d x
# $$
# 
# Untuk kasus populasi dimana $X$ adalah variabel acak diskrit dan memiliki fungsi probabilitas (p.f) $p(x)$ , kita mendefinisikan sama  $\mu$ dan $\sigma^2$ dengan menggunakan operasi dari penjumlahan. Jika populasi distribusi tidak diketahui, maka $\mu$ dan $\sigma^2$ maka bagaimana kita menduga $\mu$ dan $\sigma^2$ dari variabel acak $(X_1, \ldots,X_n)$ yang diambil dari populasi?. Terdapat banyak cara untuk menduga estimator. Estimator titik sederhana untuk $\mu$  dan banyak digunakan adalah rata-rata sample $\hat X$ . Rata-rata sample $\hat X$ adalah variabel acak yang memiliki distribusi sendiri, oleh karena itu sample memiliki mean dan variansi
# 
# $$
#  E ( \overline { X } ) = \mu 
#  \tag {8.2.3}
# $$
# 
# $$
# \operatorname { Var } ( \overline { X } ) = \sigma ^ { 2 } / n 
# \tag {8.2.4}
# $$
# 
# Itu harus diperhatikan bahwa statistik $\bar X$ memiliki nilai unik untuk sample tertentu dan dapat dinyatakan sebagai titik pada sumbu $\mu$.  Jika kita perhatikan jumlahnya yang tak terbatas dari sample dari populasi ini, masing masing ukuran  n, maka persamaan (8.2.3) pada dasarnya menyatakan bahwa jika kita rata-rata X dari sampel ini, rata-rata tersebut akan sama dengan $\mu$.  Selanjutnya, kita perhatikan dari persamaan (8.2.4) yaitu jika kita telah menentkan variansi dari semua ini $\bar X$, hasilnya akan menjadi $\sigma^2/n$, yang memberikan indikasi  bagaimana semua $\bar x$  ini  akan berdistribusi disekitar nilai $\mu$.  Catatan bahwa semakin besari nilai $n$, lebih mendekati nilai $\bar X$ dan akan mengelompok disekitar $\mu$. Sehingga dalam cara sama, varianasi sample $S^2$ dimana 
# $$
# S^2= \frac{\sum_{i=1}^n(X_i-\bar X)^2}{n-1}
# $$
# 
# dapat digunakan sebagai estimator titik untuk variansi populasi $\sigma^2​$. Statistik $S^2​$ adalah variabel acak dengan distribusi tersendiri dan mean dari distribusi ini adalah $\sigma^2​$. Yaitu
# $$
# E(S^2)=\sigma^2
# \tag {8.2.5}
# $$
# 
# 
# 

# $S^2$ adalah estimator titik tidak bias (unbiased) untuk $\sigma^2$.  Kita dapat meringkas hasil diatas dalam teorema berikut:
# 
# **Teorema**. Jika $\bar X$ dan $S^2$ ditentukan dari variabel acak ukuran $n$ dari populasi dengan tidak diketahui rata rata ($\mu$ ) dan tidak diketahui variansi ($\sigma^2$), maa $\bar X$  adalah estimator titik tidak bias untuk $\mu$ yang memiliki variansi $\sigma_\bar X^2=\sigma^2/n$ . Sehingga $S^2$ adalah estimator titik tidak bias untuk $\sigma^2$ 

# ## Sifat-sifat Estimator titik
# 
# Ada beberapa sifat dari estimator titik yang baik yang sering ditemukan, seperti unbiasedness,minimum variansinya, efisien dan, konsisten. Sifat yang akan dibahas pada bagian ini lebih detail yaitu
# 
# - unbiasedness
# - Minimum variansi
# 
# Misalkan $f(x,\theta)$ adalah p.d.f dari suatu populasi dengan parameter $\theta $ yang tidak diketahui dan $X_1, \ldots,X_n$  adalah variabel acak dari populasi tesebut. Jika $\hat \theta =\varphi(X_1,\ldots,X_n)$ adalah titik estimator dari parameter $\theta$ yang tidak diketahui. Maka kita dapatkan
# 
# **Definisi 8.2.1**. Estimasi titik $\hat \theta =\varphi(X_1,\ldots,X_n)$ dikatakan menjadi estimator tidak bias dari $\theta$ jika dan hanya jika $E(\hat \theta)=\theta$. Jika $E(\hat \theta) \ne \theta$, maka $\hat \theta$ adalah bias dan selisihnya $Bias(\hat \theta)=E(\hat \theta)-\theta$ disebut bias dari $\hat \theta$ 

# Dari theorema 8.2.1 kita nyatakan bahwa $\bar X$  dan $S^2$ adalah estimator unbiased dari rata-rata populasi $\mu$ dan variansi populasi $\sigma^2$. Masih ada pertanyaan penting yang harus dijawab. Jika mean $\mu$ dari populasi tidak diketahui dan jika kita ambil sample acak dari populasi ini dan menghitung rata-rata sample $\bar X$ menggunakan itu sebagai estimator $\mu$, bagaimna kita tahu seberapa dekat estimator $\bar X$ ke nilai sesungguhnya $\mu$?.  Jawaban untu pertanyaan ini bergantung pada ukuran populasi dan ukuran sample. Misalkan $E$ adalah selisih maximum absolute antar estimator $\bar X$ dan nilai sesungguhnya $\mu$ dan $0<\alpha<1$. Kemudian, jika populasinya normal tanpa batasan ukuran sampel atau populasi tak terbatas yang tidak normal dan ukuran sampel besar (n 30),  kita menyebutnya probabilitas $(1-\alpha)$  yaitu 
# $$
# \text {Margin error} : E=z_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt n}
# \tag{8.2.6}
# $$
# dengan mengasumsikan $\sigma$ diketahui.  Besaran $E$ disebut dengan margin error atau batas error estimasi.  Perhatikan bahwa dalam praktetkna,  umumnya ditetapkan $\alpha=0.01, 0.05, \text{atau}  \space  0.1$ karena ini memberikan probabilitas yang cukup tinggi $(1-\alpha ) $ bahwa kesalahan estimasi maksimum adalah
# sama dengan E 
# 
# Hasil pada persamaan (8.2.6) masih valid jika populasi adalah infinite dan sampling dilakukan dengan pengembalian atau jka sampling dilakukan tanpa pengembalian, tetapi ukuran sample kurang dari $5\%$ dari ukuran populasi $(n<0.005N)$. Jika populasi adalah finite dan ukuran sample relatif lebiha besari dari $5\%$, maka menggunakan faktor ektra yang dikenal dengan finite population correction $\sqrt{(N-n)/(N-1))}$ dan selisih absolute maximum antara estimator $\bar X$ dan nilai sesungguhnya $\mu$ adalah
# $$
# \text{Margin error}:E  z _ { \frac { \alpha } { 2 } } \frac { \sigma } { \sqrt { n } } \sqrt { \frac { N - n } { N - 1 } }
# \tag{8.2.7}
# $$

# dimana $N$ dan $n$ adalah masing-masing adalah ukuran populasi dan ukuran sample. Jika $\sigma$ tidak diketahu dalam persamaan (8.2.6) dan (8.2.7) kemudan dalam sample besar, hal tersebut dapat diganti dengan standar deviasi sample $S$ 
# 
# **Contoh 8.2.1** (Margin Error) . Perusahan manufaktur ingin menggunkan mean dari sample acak ukuran $n=64$ untuk memperkirakan panjang rata-rata batang yang diproduksi.
# Jika diketahui $\sigma = 0,5 $ cm , tentukan margin of error dengan probabilitas $95\%$

# **Solusi** Karena ukuran sampel besar dan dengan asumsi bahwa jumlah total batang yang diproduksi  cukup besar, maka dari Persamaan (8.2.6)
# $$
# E=z_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt n}
# $$
# disini $1-\alpha = 0.95$ ,$\alpha/2=0.025$, $\alpha=0.5$, $z_{0.025}=1.96$ dan $n=64$ sehingga diperoleh 
# $$
# E = 1.96 \times \frac { 0.5 } { \sqrt { 64 } } = 0.1225 \space cm 
# $$
# perhatikan bahwa nilai nonabsolute E adalah $0.1225$
# 
# Sifat lain yang diinginkan dari penduga tak bias adalah apakah penaksir varians minimum atau tidak. Jika ya, maka akan menghasilkan perkiraan yang lebih mendekati kebenaran
# nilai parameter

# **Definisi 8.2.2.** Perhatika suatu populasi yang memiliki p.d.f $f(x,\theta) $ dengan parameter $\theta$ tidak diketahui. Misalkan $\hat \theta_1,\theta_1,\ldots,\theta_n$ adalah sekumpulan estimator tidak bias dari $\theta$. Maka estimator $\hat \theta_i$ dikatakan sebagai estimator varians minimum tidak bias (UMV) dari $\theta$ jika variansi dari $\hat \theta_i$ kurang dari atau sama dengan variansi dari estimator tidak bias lainnya

# Definisi 8.2.3. Mean Square Error (MSE) estimator $\hat \theta$ dari $\theta$ didefinisikan dengan 
# 
# $$
#  \operatorname { MSE } ( \hat { \theta } ) = E ( \hat { \theta } - \theta ) ^ { 2 } 
# $$
# 
# yang dapat ditulis lagi persamaan (8.2.8) dengan 
# 
# $$
# \operatorname { MSE } ( \hat { \theta } ) = E [ \hat { \theta } - E ( \hat { \theta } ) + E ( \hat { \theta } ) - \theta ] ^ { 2 } = \operatorname { Var } ( \hat { \theta } ) + [ \operatorname { Bias } ( \hat { \theta } ) ] ^ { 2 } 
# $$
# 

# # https://yuvalianda.com/distribusi-t/#:~:text=Distribusi%2Dt%20adalah%20kelompok%20distribusi,standar%20(distribusi%2DZ).

# In[ ]:




