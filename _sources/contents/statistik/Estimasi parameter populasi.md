# Menaksir Parameter Populasi



Fokus dari adalah pengembangan metode untuk menentukan penduga titikdan interval dari parameter populasi

### Topik yang dibahas :

- Penaksir titik untuk mean dan variansi populasi
- Penduga interval untuk rata-rata populasi normal
- Penduga interval untuk selisih rata-rata dua populasi normal
- Penduga interval untuk varians dari populasi normal
- Penduga interval untuk rasio varians dua populasi normal
- Metode Estimasi: metode momen dan metode kemungkinan maksimum
- Penaksir titik dan interval untuk parameter binomial
- Prediksi: melakukan estimasi pengamatan masa yang akan datang

### Tujuan Pembelajaran:

- Setelah mempelajari bab ini pembaca dapat memahami
- Memahami peran estimasi dalam statistik terapan
- Menentukan estimasi titik dan interval untuk berbagai parameter distribusi diskrit dan kontinu
- Memahami konsep koefisien kepercayaan dan menafsirkan interval kepercayaan.
- Memahami perbedaan antara signifikansi statistik dan praktis
- Menerapakan bahasa python untuk menentukan interval kepercayaan dari
  parameter dari berbagai distribusi.

Kita sering menghadapi masalah statistik dari seperti berikut: kita memiliki banyak atau besar objek populasi sehingga jika pengukuran dilakukan pada setiap objek maka tentunya kita akan memiliki distribusi dari pengukuran dari semua objek dalam populasi tersebut.  Karena kita tidak memungkinkan untuk melakukan pengukuran pada semua objek dalam populasi, distribusi ini tentu saja tidak diketahui. Hal terbaik yang dapat kita lakukan dalam praktiknya adalah memperkirakan berbagai karakteristik (atau biasa disebut sebagai parameter) dari informasi distribusi  terkandung dalam pengukuran yang dilakukan dalam sampel acak objek  populasi. Misalnya, jika kita ingin mengestimasi mean dan varians dari distribusi populasi,  kita dapat menggunakan rata-rata sampel dan varians sampel sebagai penduga untuk besaran-besaran tersebut. Jika kita ingin menaksir median populasi, kita dapat menggunakan median sampel. Tentu saja, parameter lain dari distribusi populasi seperti, standar deviasi, atau proporsi populasi dapat diperkirakan atau ditaksir dari pengukuran sample acak obyek yang telah dilakukan.  Hal inilah Masalah ini
jenis adalah fokus dari bab ini.

KIta membahas dua macam penduga untuk paramater populasi, yaitu penduga titik dan penduga interval. Lebih tepatnya, misalkan  $(X_1,X_2, X_3 \ldots)$  adalah sample acak dari populasi yang memiliki parameter yang diharapkan, misalnya  $\theta$ . Jika $\hat \theta=\varphi(X_1,X_2,X_3 \ldots, X_n)$ adalah fungsi benilai tunggal (single-values) dari $X_1,X_2,X_3, \ldots,X_n$ sehingga $\hat \theta$  itu sendiri adalah variabel acak, maka kita menyebut $\theta$ sebagai statistik. Selanjutnya, jika 
$$
E\left(\varphi\left(X_{1}, \ldots, X_{n}\right)\right)=E(\hat{\theta})=\theta
$$


kita sebut  $\hat \theta $ adalah unbiasaed estimator dari $\theta$. Statistik $\hat \theta $  biasnya disebut dengan estimator titik ( point estimator) untuk parameter $\theta$. Jika $\hat \theta_l= \varphi_l(X_1,X_2, \ldots,X_n)$ dan $\hat \theta_u= \varphi_u(X_1,X_2, \ldots,X_n)$ adalah dua statistik sehingga 
$$
P\left(\hat{\theta}_{l}<\theta<\hat{\theta}_{u}\right)=1-\alpha \label{eq1}
\tag{8.1.2}
$$
kita katakan bahwa interval acak $(\hat \theta_l,\hat \theta_u)$ adalah $100(1-\alpha)\%$ *interval kepercayaan* untuk parameter $\theta$ . Pasangan statistik $(\hat \theta_l,\hat \theta_u)$ kadangkala disebut sebagai penduga interval (estimator interval) untuk $\theta$. Titik ujung  ($\hat \theta_l  $ dan $ \hat \theta_u$) dari interval kepercayaan $(\hat \theta_l,\hat \theta_u)$ kadangkala disebut batas kepercayaan  $100(1-\alpha)\%$ dari $\theta$  dan $\hat \theta_l  $ , $ \hat \theta_u$ masing masing disebut sebagai batas bawah kepercayaan dan batas atas kepercayaan. Probabilitas $1-\alpha$  dalam persamaan (8.1.2)  disebut  koefisien kepercayaan ( confidence coefficient) , sedangkan $ 100(1-\alpha)\%$ disebut tingkat kepercayaan (confidence level). Juga selisih $\hat \theta_l -\hat \theta_u$ disebut lebar interval kepercayaan.








