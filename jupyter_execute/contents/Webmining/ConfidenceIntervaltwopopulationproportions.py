#!/usr/bin/env python
# coding: utf-8

# # Interval Kepercayaan untuk selisih antara dua Proporsi
# 
# Seandainya anda ingin menghitung selisih antaraproporsi pria dan wanita yang mendukung gagasan bahwa minggu kerja seharusnya hanya 3 hari, bukan 5.
# Seandainya anda ingin mengestimas selisih antara populasi laki dan perempuan $ p_m -p_w$. Anda dapat pmengambil secara acak setiap populasi dan menggunakan selisih antara dua sample populasi $\hat p_m-\hat p_w$ plus atau minus margin error yang dapat dinyatakan dengan persamaan berikut:
# 
# $$
# \widehat{p_{m}}-\widehat{p_{w}} \pm \mathrm{z} * \sqrt{\frac{\widehat{p_{m}}\left(1-\widehat{p}_{m}\right)}{n_{m}}+\frac{\widehat{p_{w}}\left(1-\widehat{p_{w}}\right)}{n_{w}}}
# $$
# 
# 
# karena kita tahu dari sebelumnya  $z$ dapat dihtunga tabel $z$ , yang sama dengan 1.96 dalam kasus interval kepercayaan 95 persen.  Marilah diskripsi diatas kita gunakan python untuk implementasinya dengan menetapkan parameter paramternya.

# In[1]:


import numpy as np

# In[2]:


p_m = 0.64
p_w = 0.43
n_m = 100
n_w = 120
z_value = 1.96

# Kita tentukan selisih antara rata-ratanya.

# In[3]:


difference = p_m - p_w
first_term = (p_m* (1-p_m))/n_m
second_term = (p_w*(1-p_w))/n_w

# Dan kita hitung batas atas dan batas bawah menggunakan persamaan diatas 

# In[4]:


lower_bound = difference - (z_value*(np.sqrt(first_term + second_term)))
upper_bound = difference + (z_value*(np.sqrt(first_term + second_term)))
lower_bound,upper_bound

# Selisih $  p_m - p_w$ adalah **0.210**
# 
# Kita dapat menafsirkan hasilnya dengan mengatakan dengan 95 persen
# keyakinan bahwa persentase pria lebih tinggi daripada wanita
# mendukung minggu kerja 3 hari, dan ada perbedaan diantaranya

# # Distribusi t dan Interval kepercayaan
# 
# Pada bab ini kita telah mengasumsikan distribusi normal. Tetapi sekarang, mari kita bahas distribusi lain yang umum ditemukan yang disebut, distribusi t.  Selainjuga dikenal sebagai Student-Distribution,  distritbusi t adalah distribusi probabilitas yang memiliki ekor lebih berat dari distribusi normal,
# yang memberi ruang bagi nilai-nilai yang lebih ekstrem untuk ditemukan
# 
# Selama ini, kami telah menggunakan z-score dan
# tabel-z. Namun, kita harus tahu bahwa untuk menghitung
# z-score, kita perlu mengetahui standar deviasi yang sebenarnya,
# yang biasanya tidak diketahui. Jadi, kita hanya ingin menegaskan  bahwa semua perhitungan yang yang dilakukan menggunakan StatsModels didasarkan pada distribusi-t 

# In[ ]:



