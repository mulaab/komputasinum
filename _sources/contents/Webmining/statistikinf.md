

# Seleksi Fitur Chi-squre

# Uji chi-square  dan uji Fisher's exact  

Uji Fisher's exact dan uji chi-squared test adalah **uji statistik yang paling umum untuk independensi dari variabel categorical **:

- Uji Fisher's adalah uji tepat (**exact test**) karena kita tahu distribusi sampling sesungguhnya
- Uji chi-squared hanya uji pendekatan (**approximate test**) karena distribusi sampling dari statistik uji hanya pendekatan yang sama dengan distribusi chi-square .



# Uji Chi-Square

Uji Chi-square adalah uji kebebasan dari dua variabel  qualitatif untuk mengetahui apakah adanya keterkaitan antara dua variabel categorical. Dengan kata lain uji ini digunakan untuk mengetahui apakah nilai nilai dari  satu varibel categorical saling bergantung pada nilai nilai  variabel  categorical yang lain

Jika uji ini menunjukkan bahwa dua variabel tidak ada keterkaitan (artinya variabel-variabel tersebut saling bebas) artinya bahwa mengetahui nilai satu variabel tidak akan memberikan informasi tentang nilai dari variabel lain. Sebaliknya, jika uji menunjukkan keterkaitan diantara variabel (artinya variabel saling terkait) itu menunjukkan bahwa mengetahui nilai dari satu variabel akan memberikan informasi nilai dari variabel lain. 



# Hipotesa

Uji independensi Chi-kuadrat adalah uji hipotesa sehingga memiliki hipotesa null ($H_0$) dan hipotesa lainnya  ($H_1$):

* $H_0$ : variabel-variabel saling bebas , **tidak ada**   keterkaitan antara dua variabel  categorical . Mengetahui nilai dari satu variabel tidak membantu untuk memprediksi nilai dari variabel lain.
* $H_1$ : variabel-variabel tesebut adalah saling bergantung, ada keterkaitan antara dua variabel  categorical. Dengan diketahui nilai dari satu variabel membantu untuk memprediksi nilai dari variabel lainnya

# Bagaimana uji tersebut bekerja?

Uji independensi Chi-square bekerja dengan membandingkan frekewensi yang diamati dengan frekwensi yang diharapkan

Jika selisih antara frekwensi pengamatan dengan frekwesni yang diharapkan adalah kecil, kita tidak dapat menolah hipotesa null dan kita tidak dapat menolak bahwa dua variabel tidak saling berkaitan.  Sebaliknya jika selisih antara frekwensi pengamatan dan frekwensi diharapkan adalah besar, kita dapat menolak hipotesa null dan kita dapat menyimpulkan bahwa dua variable saling berkaitan



Nilai ambang antara dari besar kecilnya selisih adalah diperoleh dari distribusi  Chi-square. Nilai ini disebut sebagai nilai kritis, bergantung pada tingkat signifikan $\alpha$ (biasanya sama dengan  5%) dan derajat kebebasan. Nilai kritis ini dapat ditemukan pada tabel statistik distribusi Chi-square.

# Contoh

Untuk contoh, perhatikan padata data berikut, apakah ada keterkaitas secara statistik antara merokok dan menjadi atlet profesional. Merokok memiliki nilai  "yes" atau"no" dan menjadi atlet profesioal memiliki nilia  "yes" atau"no". Dua variebel tersebut adalah dua variabel kualitastif sehingga kita perlu menggunakan uji independensi Chi-square  dan data yang dikumpulkan sebanya  28 orang.

Perhatikan bahwa kami memilih variabel biner (variabel biner = variabel kualitatif dengan dua level) demi kemudahan, tetapi uji independensi Chi-kuadrat juga dapat dilakukan pada variabel kualitatif dengan lebih dari dua level. Misalnya, jika variabel merokok memiliki tiga tingkat: (i) bukan perokok, (ii) perokok sedang dan (iii) perokok berat, langkah dan interpretasi hasil tes serupa dibandingkan dengan dua tingkat.



|             | non-smoker | smoker | total |
| ----------- | ---------- | ------ | ----- |
| Athlete     | 14         | 4      | 18    |
| Non-Athlete | 0          | 10     | 10    |
|             | 14         | 14     | 28    |

## Frekwensi Harapan

Ingat bahwa untuk uji independensi Chi-square kita butuh menentukan apakah jumlah pengamatan adalah sangat signifikan berbeda dari jumlah yang kita harapkan jika tidak ada hubungan antara dua variabel. Kita memiliki jumlah yang diamati (lihat tabel di atas), jadi kami sekarang perlu menghitung jumlah yang diharapkan dalam kasus variabel independen. Frekuensi yang diharapkan ini dihitung untuk setiap subkelompok satu per satu dengan rumus berikut::


$$
\text{frekwensi harapan} = \frac{\text{total # dari pengamatan. pada baris} \cdot \text{total # pengamatan. pada kolom}}{\text{banyaknya pengamatan keseluruhan}}
$$


Berikut adalah tabel frekwensi harapan yang telah dihitung untuk setiap subgroup:

|                 | Non-smoker         | Smoker             | Total |
| --------------- | ------------------ | ------------------ | ----- |
| **Athlete**     | (18 * 14) / 28 = 9 | (18 * 14) / 28 = 9 | 18    |
| **Non-athlete** | (10 * 14) / 28 = 5 | (10 * 14) / 28 = 5 | 10    |
| **Total**       | 14                 | 14                 | 28    |

Perhatikan bahwa uji independensi Chi-square hanya dapat dilakukan bila frekwensi harapan pada semua group adalah sama atau lebih besar dari 5. Asumsi ini telah dipenuhi pada tabel kita diatas. Jika tidak memenuhi asumsi diatas maka dapat dihitung menggunakan uji  Fisher’s 

## Statistik Uji

Kita telah memilki frekwensi pengamatan dan harapan. Kita perlu untuk membandingkan frekwensi frekwesni ini untuk menentukan apakah frekwensi frekwensi berbeda secara sigfinikan. Perbedaan antara frekwensi pengamatan dan frekwensi harapan, disebut dengan statistika uji ( t-statistik) dan dinyatakan dengan $\chi^2$  dihitung sebagai berikut:

$$
\chi^2 = \sum_{i, j} \frac{\big(O_{ij} - E_{ij}\big)^2}{E_{ij}}
$$

dimana $O$  menyatakan frekwensi pengamatan dan $E$   frekwensi harapan. Mari kita hitung dari contoh diatas sesuai dengan formula berikut:

- dalam sub group athlete dan non-smoker $\frac{(14 - 9)^2}{9} = 2.78$ 
- dalam subgroup  non-athlete dan non-smoker $ \frac{(0 - 5)^2}{5} = 5$ 
- dalam subgropu athlete dan smoker $\frac{(4 - 9)^2}{9} = 2.78$ 
- dalam  subgroup  non-athlete dan smoker $\frac{(10 - 5)^2}{5} = 5$ 

kemudian kita jumlahkan semua untuk mendapatkan statistik uji:
$$
\chi^2 = 2.78 + 5 + 2.78 + 5 = 15.56
$$

## Nilai kritis

Statistik uji sendiri tidak cukup  untuk menyimpulkan independensi atau kebergantungan antara dua variabel. Seperti disebutkan sebelumnya, statistik uji  harus dibandingan dengan nilai kritis untuk menentukan apakah selish atau beda tersebut besar atau kecil. Seseorang tidak dapat mengatakan bahwa statistik uji adalah besar atau kecil tanpa menempatkannya dalam perspektif dengan nilai kritis.

Jika statistik uji diatas nilai kritis, itu berarti bahwa kemungkinan mengamati perbedaan antara frekuensi yang diamati dan yang diharapkan tidak mungkin terjadi. Dengan kata lain, jika statistik uji di bawah nilai kritis, itu berarti kemungkinan untuk mengamati perbedaan seperti itu. Jika kemungkinan untuk mengamati perbedaan ini, kita tidak dapat menolak hipotesis bahwa kedua variabel itu independen, jika tidak, kita dapat menyimpulkan bahwa ada hubungan antara variabel-variabel tersebut.

Nilai kritis dapat ditemukan pada tabel statistik distribusi chi-square dan bergantung pada tingkat signifikan, dinyatakan dengan $\alpha$, dan derajat kebebasan dinyatakan dengan $ df$ . Tingkat signifikan biasanya ditetapkan 5% . Derajat kebebasan untuk uji Chi-square dari independesni ditemukan sebagai berikut:

$$
df = (\text{banyaknya baris} - 1) \cdot (\text{banyaknya kolom} - 1)
$$

Pada contoh, derajat kebebasan adalah $ df=(2−1)⋅(2−1)=1 $  karena ada dua baris dan dua kolom pada tabel  contingency 

Kita sekarang memiliki semua informasi yang diperlukan untuk menemukan nilai kritis pada tabel Chi-Square $\alpha=0.05$ dn $df=1$ . Untuk menemukan nilai kritis kita perlu mencari baris $df=1$ dan kolom $\chi^2_{0.050}$  karena $\alpha =0.05$  dalam gamber dibawah berikut.  Nilai kritisnya adalah 3.84146



```{figure} ./images/chi.png
---
height: 200px
name: directive-fig
---
Nilai kritis!
```


## Kesimpulan dan interpretasi

Kita telah memiliki statistik uji dan nilai kritis, kita dapat membandingkannya untuk mengecek apakah hipotesa null dari independensi dari variabel direject atau tidak. 

Pada contoh statistik uji = $15.56$  nilai kritis =$3.84146$  sehingga  statistik uji > nilai kritis , maka kita dapat menolah hipotesa null pada tingkat kepercayaan yang diberikan.  Pada kasus ini kita dapat menolak hipotesa null dengan tingkat kepercayaan 5% sehingga ada keterkaitan signifikan natara merokok dan menjadi atlit atau tidak.





# Uji Fisher’s exact 

Uji Fisher’s exact digunakan untuk menyelidik hubungan antar dua variabel categorical dalam tabel  contingency 

Uji Fisher’s exact digunakan jika ukuran sample kecil  (katakan, < 1000). Sedangkan Uji  Chi-square adalah cocok ketika ukuran sample besar. Uji  Fisher’s exact khusus digunakan lebih dari 20% sel memiliki  frekuensi yang diharapkan <5

Uji Fisher’s Exact Test menggunakan hipotesa null dan hipotesa alternatif:

- **H0: (null hypothesis)**  kedua variabel saling bebas (independent).
- **H1: (alternative hypothesis)** kedua variabel adalah tidak saling bebas ( dependent)

Suppose we have the following 2×2 table:

## Rumus uji Fisher’s exact 

Uji Fisher’s exact tabel contingency  2 ✕ 2 contingency dihitung dengan 

|                     | Kolom 1(group 1) | Kolom 2(group 2) | Total     |
| ------------------- | ---------------- | ---------------- | --------- |
| Baris 1(categori 1) | a                | b                | a+b       |
| Baris 2(categori 2) | c                | d                | c+d       |
|                     | a+c              | b+d              | N=a+b+c+d |

 one-tailed p value dihitung dengan

$$
p=\frac{(a+b) !(c+d) !(a+c) !(b+d) !}{N ! a ! b ! c ! d !}
$$

dengan 

$p $ = nilai p sesungguhnya ($p$ value exact) 



#### Odds Ratio (OR)

Peluang suatu peristiwa (Odds Ratio)  adalah perbandingan antara frekuensi terjadinya suatu peristiwa dengan banyaknya peristiwa yang gagal.
Peluang suatu kejadian untuk baris pertama dan baris kedua adalah masing masing a/b dan c/d, respectively. Dan odd Ratio dinyatakan dengan :

$$
O R=\frac{\frac{a}{b}}{\frac{c}{d}}=\frac{a d}{b c}
$$


Menghitung x% confidence interval untukt log(Odds Ratio) dari suatu populasi 
$$
\log ({O R}) \pm Z_{\alpha/2}* \sqrt{\frac{1}{a}+\frac{1}{b}+\frac{1}{c}+\frac{1}{d}}
$$
Untuk mendapatkan Odds Ratio sesungguhnya perlu dilakukan exponential sehingga 

$\alpha$ % tingkat kepercayaan (confidence interval:) 

$$
exp(\log ({O R}) \pm Z_{\alpha/2} * \sqrt{\frac{1}{a}+\frac{1}{b}+\frac{1}{c}+\frac{1}{d}})
$$


dimnana $z_{\alpha/2}$ adalah nilai kritis dari distribusi  pada $\alpha/2$ . Untuk  confidence level  95%, $\alpha$ adalah 0.05 dan nilai kritisnya adalah 1.96

Logarithma formula diatas adalah  natural logarithms, yaitu, log base e, kadangkala dinyatakan dengan $ln()$ 

Semakin tinggi tingkat kepercayaan (confidence interval), semakin yakin Anda bahwa interval tersebut berisi rasio odds yang sebenarnya.

Jika  [*p* value](https://www.reneshbedre.com/blog/how-to-calculate-p-value.html) (two-tailed) yang didapat dari uji Fisher's exact signifikan  akan menolak hipotesa null jika nilai $p$ kurang dari  $\alpha$ 



# Tabel Chi-square

```{figure} ./images/chitable.png
---
height: 500px
name: directive-fig
---
Tabel Chi-square
```






