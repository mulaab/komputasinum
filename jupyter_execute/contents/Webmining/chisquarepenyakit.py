#!/usr/bin/env python
# coding: utf-8

# 

# In[1]:


# code for loading the format for the notebook
import os

# path : store the current path to convert back to it later
path = os.getcwd()
#os.chdir(os.path.join('..', 'notebook_format'))



# In[2]:


os.chdir(path)
import numpy as np
import pandas as pd

# 1. magic to print version
# 2. magic so that the notebook will reload external python modules
%load_ext watermark
%load_ext autoreload 
%autoreload 2

from sklearn.preprocessing import LabelBinarizer
from sklearn.feature_selection import chi2, SelectKBest
from sklearn.feature_extraction.text import CountVectorizer

%watermark -a 'Ethen' -d -t -v -p numpy,pandas,sklearn

# # Chi-Square Feature Selection

# Seleksi fitur adalah proses dimana secara automatis memilih fitur tersebut pada data anda yang berpengaruh terhadap variabel prediksi atau ouput yang diharapakan. Keuntungan melakukan seleksi fitur sebelum melakukan pemodelan data anda adalah:
# 1. Menghindari overfitting: Data yang lebih sedikit memberikan peningkatan kinerja pada model dan sediti menghasilkan  sedikit peluang untuk membuat keputusan salah
# 2. Mengurangi waktu pelatihan. Data yang lebih sedikit berarti algoritma pelatihan semakin cepat
# 
# 
# 

# In[135]:


# misal kita memiliki data text berikut
X = np.array(['makan nasi soto', 'nasi soto panas', 'warung nasi soto', 'saya makan nasi pecel'])
y = [1, 1, 2, 0]

# kita akan merubah teks tersebut menjadi matrik dokumen-term,
# dan kita  mencetak output yang mudah dibaca
vect = CountVectorizer()
X_dtm = vect.fit_transform(X)
X_dtm = X_dtm.toarray()
X_dtm
datane=pd.DataFrame(X_dtm, columns = vect.get_feature_names())
X_dtm.shape


# Jika kita menambahkan dengan kelas dari masing masing dokumen diperoleh data seperti berikut
# 
# |      | makan| nasi | panas| pecel| saya   | soto    |warung| Kelas |
# | ---- | ---- | ---- | ---- | ---- | ------ | ------- | ---- | ----- |
# | 0    | 1    | 1    | 0    | 0    | 0      | 1       | 0    | 1     |
# | 1    | 0    | 1    | 1    | 0    | 0      | 1       | 0    | 1     |
# | 2    | 0    | 1    | 0    | 0    | 0      | 1       | 1    | 2     |
# | 3    | 1    | 1    | 0    | 1    | 1      | 0       | 0    | 0     |
# 
# 
# 

# 
# Salah satu metode seleksi fitur yang bias digunakan pada data teks adalah seleksi fitur Chi-Square.Uji $\chi^2$ digunakan pada statistik untuk menguji independensi dari dua kejadian (variabel) Khususnya dalam seleksi fitur, metode tersebut digunakan untuk menguji apakah suatu term tertentu yang ada dan kelas tertentu yang ada adalah saling bebas.Secara umum dari dokumen $D$ yang tersedia, kita hitung nilai-nilai berikut untuk setiap term dan merangking tersebut sesuai dengan skor masing-masing
# 
# $$
# \chi^2(D, t, c) = \sum_{e_t \in \{0, 1\}} \sum_{e_c \in \{0, 1\}} 
# \frac{ ( N_{e_te_c} - E_{e_te_c} )^2 }{ E_{e_te_c} }$$
# 
# dimana
# 
# - $N$ adalah  frekwensi pengamatan dan $E$ adalah frekwensi harapan
# - $e_t$ akan bernilai 1 jika dokumen berisi  term $t$ dan 0 jika sebaliknya
# - $e_c$ akan bernilai 1 jika dokumen dalam kelas $c$ dan  0 jika sebaliknya
# 
# Untuk setiap feature (term), jika memilki score $\chi^2$ tinggi maka menunjukkan  hipotesa null  $H_0$ (independence) 

# ## Implementasi

# Kita pertama menghitung jumlah pengamatan pada masing-masing kelas. Dalam hal dilakukan dengan membuat tabel contingency dari input $X$ (nilai nilai feature ) dan $y$ (label kelas). Setiap masukan $i$, $j$ menyatakan fitur $i$ dan kelas  $j$, dan menghitung jumlah nilai fitur ke $i$ dari semua sample yang menjadi anggota kelas $j$.
# 
# Perhatikan bahwa walaupun nilai fitur disini dinyatakan sebagai frekwensi, metode ini juga bekerja dengan baik ketika nilainya adalah nilai tf-idf, karena nilai tf-idf juga merupakan bobot/skala dari frekwensi

# In[54]:


# binarisasi kolom output ,
# disini menghitung nilai pengamatan dengan perkalian titik

y_binarized = LabelBinarizer().fit_transform(y)
print(y_binarized)
print()

# baris menunjukkan jumlah pengamatan setiap kelas
# dan kolom menunjukkan setiap fitur
observed = np.dot(y_binarized.T, X_dtm)
print(observed)

# misalkan. beris kedua dari rangkaian pengamatan diatas menujukkan total jumlah dari term-term yang menjadi kelas 1. Kemudian kita menghitung frekwensi harapan dari setiap term pada masing masing kelas

# In[113]:


# menghitung probabilitas setiap kelas dan jumlah fitur; 
# simpan keduanya sebagai array dua dimensi dengan menggunakan reshape
class_prob = y_binarized.mean(axis = 0).reshape(1, -1)
feature_count = X_dtm.sum(axis = 0).reshape(1, -1)
expected = np.dot(class_prob.T, feature_count)

print(expected)

# In[114]:


class_prob

# In[115]:


feature_count

# In[128]:


chisq = (observed - expected) ** 2 / expected
chisq_score = chisq.sum(axis = 0)
print(chisq_score)

# Kita dapat membutktikan hasil kita dengan library scikit-learn menggunakan fungsi  `chi2`. Kode berikut menghitung nilai chi-square value untuk masing masing fitur. Dari sekumpulan nilai yang dihasilkan element pertama adalah skor chi-square , samakin baik sekor jika semakin besar nilainya dan elemen kedua adalah nilai p, nilai ini semakin baki jika semakin kecil.

# In[184]:


chi2score = chi2(X_dtm, y)
chi2score[0]
chi2score[1]
skorchi = np. reshape(chi2score[0], (1, 7))
phisccore=np. reshape(chi2score[1], (1, 7))


# In[185]:


chi2score[1]

# In[187]:


datascore=pd.DataFrame(skorchi, columns = vect.get_feature_names())
dataphi=pd.DataFrame(phisccore, columns = vect.get_feature_names())

# In[188]:


datascore

# In[190]:


akhirskore = pd.concat([datascore, dataphi])
akhirskore

# Scikit-learn menyediakan kelas `SelectKBest` yang dapat digunakan dengan beberapa uji statistik lain. ini akan meranking fitur sesuai dengan uji statistik yang ditentukan dan memilih k teratas( artinya term-term ini dianggap lebih relevan)

# In[ ]:




# In[192]:


kbest = SelectKBest(score_func = chi2, k = 3)
X_dtm_kbest = kbest.fit_transform(datane, y)
mask = kbest.get_support()
X_dtm_kbest = datane.columns[mask]
X_dtm_kbest

# In[191]:


X_dtm_kbest

# # Kasus berita

# In[193]:


from sklearn.datasets import fetch_20newsgroups
 # newsgroups categories
categories = ['alt.atheism','talk.religion.misc',
              'comp.graphics','sci.space']

posts = fetch_20newsgroups(subset='train', categories=categories,
                           shuffle=True, random_state=42,
                           remove=('headers','footers','quotes'))

# In[194]:


from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(lowercase=True,stop_words='english')
X = vectorizer.fit_transform(posts.data)

# In[195]:


from sklearn.feature_selection import chi2
# menghitung chi2 untuk setiap fitur
chi2score = chi2(X,posts.target)[0]

# In[196]:


from pylab import barh,plot,yticks,show,grid,xlabel,figure
figure(figsize=(6,6))
wscores = list(zip(vectorizer.get_feature_names(),chi2score))
wchi2 = sorted(wscores,key=lambda x:x[1]) 
topchi2 = list(zip(*wchi2[-25:]))
x = range(len(topchi2[1]))
labels = topchi2[0]
barh(x,topchi2[1],align='center',alpha=.2,color='g')
plot(topchi2[1],x,'-o',markersize=2,alpha=.8,color='g')
yticks(x,labels)
xlabel('$\chi^2$')
show()

# In[ ]:




# In[197]:


import pandas as pd
import numpy as np
from scipy import stats
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFpr, chi2, SelectKBest, SelectFwe, f_classif, SelectFdr
import matplotlib.pyplot as plt
%matplotlib inline  
# https://www.kaggle.com/uciml/breast-cancer-wisconsin-data?select=data.csv
df = pd.read_csv("data.csv")
# replace M with 1 and B with 0
my_map = {
          'M':1,
          'B' :0
         }
df['diagnosis'] = df['diagnosis'].map(my_map)
# remove the id column
df.drop(['id'], axis=1, inplace=True)
df

# In[36]:


X = df.drop(['diagnosis'], axis=1)
y = df.diagnosis

# In[37]:


X

# In[19]:


selector = SelectKBest(score_func=chi2, k=7)
new_data = selector.fit_transform(X, y)
mask = selector.get_support()
new_features = X.columns[mask]
new_features


