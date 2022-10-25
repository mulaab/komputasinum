#!/usr/bin/env python
# coding: utf-8

# # Chi-square menggunakan R

# In[1]:


 data_frame <- read.csv("https://goo.gl/j6lRXD")

# In[6]:


data_frame

# In[5]:


table(data_frame$treatment, data_frame$improvement)

# In[7]:


chisq.test(data_frame$treatment, data_frame$improvement, correct=FALSE)

# ## Kesimpulan
# Berdasarkan hasil  nilai chi-square hitung 5,5569. Kita telah mendapatkan p-Value lebih kecil dari tingkat signifikansi 0,05, sehingga  menolak hipotesis nol (null hypothesis ) dan  menyimpulkan bahwa kedua variabel tersebut adalah saling terkait (dependent)

# In[13]:


from functools import partial
from rpy2.ipython import html
html.html_rdataframe=partial(html.html_rdataframe, table_class="docutils")

# In[14]:


from rpy2.robjects.packages import importr
utils = importr('utils')

dataf = utils.read_csv('https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/'
                       'master/notebooks/data/california_cities.csv')

# In[15]:


import rpy2.ipython.html
rpy2.ipython.html.init_printing()

# In[16]:


dataf

# In[19]:


%load_ext rmagic

# In[20]:


import numpy as np
import matplotlib.pyplot as plt
X = np.array([0,1,2,3,4])
Y = np.array([3,5,4,6,7])
plt.scatter(X, Y)

# In[21]:


%Rpush X Y
%R lm(Y~X)$coef

# In[22]:


Xr = X - X.mean(); Yr = Y - Y.mean()
slope = (Xr*Yr).sum() / (Xr**2).sum()
intercept = Y.mean() - X.mean() * slope
(intercept, slope)

# In[23]:


%R resid(lm(Y~X)); coef(lm(X~Y))

# In[25]:


%R d=resid(lm(Y~X)); e=coef(lm(Y~X))
%R -o d -o e
%Rpull e
print(d)
print(e)
import numpy as np
np.testing.assert_almost_equal(d, a)

# In[26]:


A = np.arange(20)
%R -i A
%R mean(A)

# In[27]:


%Rget A

# In[28]:


from __future__ import print_function
v1 = %R plot(X,Y); print(summary(lm(Y~X))); vv=mean(X)*mean(Y)
print('v1 is:', v1)
v2 = %R mean(X)*mean(Y)
print('v2 is:', v2)

# In[29]:


v = %R plot(X,Y)
assert v == None

# In[ ]:



