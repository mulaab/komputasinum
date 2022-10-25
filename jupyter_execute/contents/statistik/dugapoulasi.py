#!/usr/bin/env python
# coding: utf-8

# # Penduga untuk selisih dua populasi
# 
# ## a. Variansi diketahui
# Seandainya $\bar X_1$ dan $S_1^2$ adalah rata-rata dan variansi sample ukuran $n_1$ dari distribusi norma $N(\mu_1,\sigma_1^2)$ dan   $\bar X_2$ dan $S_2^2$ adalah rata-rata dan variansi sample ukuran $n_2$ dari distribusi norma $N(\mu_2,\sigma_2^2)$. Misalkan selisih rata-rata populasi $\mu_1$ dan $\mu_2$ adalah $\delta=\mu_1 -\mu_2$. Estimator titik tidak bias (unbiased) $\delta$ pastinya $\bar X_1-\bar X_2$, karean $E( \bar X_1-\bar X_2)=\mu_1-\mu_2=\delta$. Oleh karena itu, kita punya $\bar X_1-\bar X_2$ didistribusikan dengan   distribusi $N\left(\mu_{1}-\mu_{2}, \sigma_{1}^{2} / n_{1}+\sigma_{2}^{2} / n_{2}\right)$. Jika $\sigma_1^2$ dan $\sigma_2^2$ diketahui, maka 
# 
# $$
# P\left(-z_{\alpha / 2} \leq \frac{\left(\bar{X}_{1}-\bar{X}_{2}\right)-\left(\mu_{1}-\mu_{2}\right)}{\sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}}} \leq z_{\alpha / 2}\right)=1-\alpha
# $$
# 
# atau ekivalen dengan
# 
# $$
# P\left(\left(\bar{X}_{1}-\bar{X}_{2}\right)-z_{\alpha / 2} \sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}} \leq \mu_{1}-\mu_{2} \leq\left(\bar{X}_{1}-\bar{X}_{2}\right)+z_{\alpha / 2} \sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}}\right)=1-\alpha
# $$
# 
# Sehingga kita miliki berikut
# 
# **Theorema 8.4.1**. JIka $\bar X_1​$ adalah rata-rata sample acak ukuran $n_1​$ dari populasi yang memiliki distribusi $N(\mu_1,\sigma_1^2)​$ dan $\bar X_2​$ adalah rata rata sample acak ukuran $n_2​$ yang saling bebas dari $N(\mu_2,\sigma_2^2)​$  dan jika $\sigma_1^2​$  dan $\sigma_2^2​$    diketahui maka 
# $$
# \left(\left(\bar{X}_{1}-\bar{X}_{2}\right)-z_{\alpha / 2} \sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}},\left(\bar{X}_{1}-\bar{X}_{2}\right)+z_{\alpha / 2} \sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}}\right)
# \tag {8.4.2a}
# $$

# Perhatikan bahwa ketika dua populasi normal dengan varians yang diketahui, maka interval kepercayaan untuk selisih dari dua rata-rata populasi, yang ditunjukkan pada Persamaan (8.4.2a)

# **Contoh**. Sample ukuran 10 dari $N(\mu_1,25)$ menghasilkan rata-rata sample $X_1=19.8$ , sedangkan sampel independen berukuran 12 dari $N(\mu-2, 36)$ menghasilkan rata-rata sampel $X_2$ = 24. Tentukan interval kepercayaan untuk $\mu_{1}-\mu_{2}$ 

# **Solusi**
# Pada contoh ini, dua populasi normal dengan diketahui variansinya dengan beberapa hal berikut
# $$
# 1-\alpha=0.90, \alpha / 2=0.05, z_{\alpha / 2}=1.645
# $$
# 
# $$
# \sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}}=\sqrt{\frac{25}{10}+\frac{36}{12}}=\sqrt{5.5}=2.345
# $$
# 
# Dengan menggunakan persamaan (8.4.2a), kita dapatkan 90% interval kepercayaan untuk $\mu_1-\mu_2$ adalah
# $$
# ((19.8-24.0))\pm 1.645 \times 2.345)=(-9.06-1.34)
# $$
# Interpretasi : Kita percaya 90% bahwa selisih antara dua rata-rata populasi $(\mu_1-\mu_2)$ adalah diantara -906 dan -1.34.
# 
# Perhatikan 90% interval kepercayaan untuk $\mu_1-\mu_2$ yaitu tanda batas kepercayaan berubah

# ## b. Variansi tidak diketahui
# Jika $n_1$ dan $n_2$ adalah besar (keduanya melebihi 30) dan jika $\sigma_1^2$ dan $\sigma_2^2$ tidak diketahui dan kita tidak dapat mengasumsikan $\sigma_1^2=\sigma_2^2$ maka 
# 
# Interval kepercayaan untuk $\mu_1-\mu_2$ dengan koefisien kepercayaan $(1-\alpha)$ bila $\sigma_1^2$ dan\sigma_2^2 tidak diktahuai  dan kita tidak dapat mengasumsikan $\sigma_1^2=\sigma_2^2$ sample besar:
# $$
# \left(\left(\bar{X}_{1}-\bar{X}_{2}\right)-z_{\alpha / 2} \sqrt{\frac{S_{1}^{2}}{n_{1}}+\frac{S_{2}^{2}}{n_{2}}},\left(\bar{X}_{1}-\bar{X}_{2}\right)+z_{\alpha / 2} \sqrt{\frac{S_{1}^{2}}{n_{1}}+\frac{S_{2}^{2}}{n_{2}}}\right)
# $$
# disini persamaan (8.4.3) adalah pendektan $100(1-\alpha)\%$ interval kepercayaan untuk  $\mu_1-\mu_2$

# Jika diasumsikan bahwa $\sigma_1^2=\sigma_2^2=\sigma^2$ dimana $\sigma^2$ tidak diketahui maka
# 
# 
# $$
# \left(\left(\bar{X}_{1}-\bar{X}_{2}\right)-t_{n_{1}+n_{2}-2 ; \alpha / 2} S_{p} \sqrt{\frac{1}{n_{1}}+\frac{1}{n_{2}}},\left(\bar{X}_{1}-\bar{X}_{2}\right)+t_{n_{1}+n_{2}-2 ; \alpha / 2} S_{p} \sqrt{\frac{1}{n_{1}}+\frac{1}{n_{2}}}\right)
# \tag{8.4.10}
# $$
# 
# 
# adalah $100(1-\alpha)\%$ interval kepercayaan untuk $\mu_1-\mu_2$ 

# **Contoh**. Sebuah sampel n1 = 5 bola lampu tipe A memiliki rata-rata panjang umur $\bar X_1 = 1000$  jam dengan simpangan baku $S_1 = 28$  jam. Sebuah sampel $n_2 = 7$  bola lampu tipe B, menghasilkan $\bar X_2 = 980 $ jam, dan $S_2 = 32$  jam. Kita berasumsi bahwa proses terdistribusi normal dengan varians $\sigma_1^2$  dan $\sigma_2^2 $ yang sama, sehingga $\sigma_1^2=\sigma_2^2=\sigma^2$. Tentukan 99% interval kepercayaan untuk $\mu_1-\mu_2= \mu_A-\mu_B$ 

# ## Importing Libraries

# In[ ]:





# In[1]:


import scipy
from scipy import stats
import math
import numpy as np


# __Example 8.3.3__ (Confidence interval for µ when using a large sample) A manufacturing engineer decided
# to check the efficiency of a new technician hired by the company. She records the time taken by the
# technician to complete 100 randomly selected jobs and found that in this sample of 100, the average time
# taken per job was 10 hours with a standard deviation of two hours. Find 95% lower and upper one-sided
# confidence intervals for µ, the average time taken by a technician to complete one job.

# In[2]:


# Normal interval
# parameters: alpha = confidence percentage, loc = sample mean, scale = standard error 
stats.norm.interval(alpha=0.9, loc=10, scale=2/10)


# ### Alternative: making our own function to compute z-intervals (one or two-tailed) 

# In[3]:


def confidence_interval(conf_level, x_bar, stdev, n, alternative='two-sided', mu=0):
    alpha = 1 - conf_level / 100
    
    if alternative == 'two-sided':
        half_alpha = alpha / 2
        z_val = (x_bar - mu) / (stdev / math.sqrt(n))
        z_score = abs(stats.norm.ppf(half_alpha))
        interval = (x_bar - z_score * stdev / math.sqrt(n), x_bar + z_score * stdev / math.sqrt(n))
        
        print("Z:", z_val)
        print("Z-score:", str(z_score))
        print("Interval:", interval)
    
    elif alternative == 'left-tail':
        z_val = (x_bar - mu) / (stdev / math.sqrt(n))
        z_score = stats.norm.ppf(alpha)
        interval = (-math.inf, x_bar + z_score * stdev / math.sqrt(n))
        
        print("Z:", z_val)
        print("Z-score:", str(z_score))
        print("Interval:", interval)
        
    elif alternative == 'right-tail':
        z_val = (x_bar - mu) / (stdev / math.sqrt(n))
        z_score = stats.norm.ppf(alpha)
        interval = (x_bar + z_score * stdev / math.sqrt(n), math.inf)
        
        print("Z:", z_val)
        print("Z-score:", str(z_score))
        print("Interval:", interval)


# In[4]:


# computing a TWO-SIDED confidence z-interval 
confidence_interval(90, 10, 2, 100)


# In[5]:


# computing a LEFT-TAILED confidence z-interval
confidence_interval(95, 10, 2, 100, 'left-tail')


# In[6]:


# computing a RIGHT-TAILED confidence z-interval
confidence_interval(5, 10, 2, 100, 'right-tail')


# __Example 8.3.4__ Consider the following data from a population with an unknown mean µ and unknown
# standard deviation σ:
# `
# 23 25 20 16 19 35 42 25 28 29 36 26 27 35 41 30
# 20 24 29 26 37 38 24 26 34 36 38 39 32 33 25 30
# `
# 
# Use Python to find a 95% confidence interval for the mean µ.

# In[7]:


x = [23,25,20,16,19,35,42,25,28,29,36,26,27,35,41,30,20,24,29,26,37,38,24,26,34,36,38,39,32,33,25,30]


# In[8]:


stats.norm.interval(alpha=0.95, loc=np.mean(x), scale=np.std(x)/np.sqrt(len(x)))


# In[9]:


confidence_interval(95, np.mean(x), np.std(x), len(x))  # the length (len) of x will give us the sample size


# In[10]:


# t interval 
# parameters: alpha = confidence percentage, df = degrees of freedom (n - 1), loc = sample mean, scale = standard error

stats.t.interval(alpha=0.95, df=len(x) - 1, loc=np.mean(x), scale=np.std(x)/np.sqrt(len(x)))


# __Example 8.4.2__ (Constructing a confidence interval for $µ_1 − µ_2$ with unknown but equal variances) A sample of $n_1 = 5$ light bulbs of type A gives an average length of life of $\bar{X_1} = 1000$ hours with a standard deviation of $S_1 = 28$ hours. A sample of $n_2 = 7$ light bulbs of type B, gives $\bar{X_2} = 980$ hours, and $S_2 = 32$ hours. We assume that the processes are normally distributed with variances $σ_1^2$ and $σ_2^2$ that are equal, that is, $σ_1^2 = σ_2^2 = σ^2$. Find a 99% confidence interval for $µ_1 − µ_2 = µ_A − µ_B$.

# In[11]:


stats.ttest_ind_from_stats(mean1=1000, mean2=980, std1=28, std2=32, nobs1=5, nobs2=7, equal_var=True)


# **Pooled Standard Error**
# ![image.png](attachment:image.png)

# In[12]:


mean_difference = 1000 - 980
n1 = 5
s1 = 28
n2 = 7
s2 = 32
# since we are told that population variances are equal for both type A and type B... 
pooled_var = ((n1 - 1)*(s1**2) + (n2 - 1)*(s2**2))/(n1 + n2 - 2)

# calculating standard error
pooled_standard_error = np.sqrt((pooled_var / n1) + (pooled_var / n2))

# calculating t-interval
stats.t.interval(alpha=0.99, df=n1 + n2 - 2, loc=mean_difference, scale=pooled_standard_error)


# __Example 8.4.4__ (Yarn breaking strength test) A sample of 61 strands of type I yarn, when subjected to
# breaking-strength tests, yielded a sample average of $\bar{X}_I = 1400$ psi with a sample standard deviation of $S_I = 120$ psi. A sample of 121 strands of type M yarn was also subjected to the same breaking strength tests and yielded a sample average of $\bar{X}_M = 1250$ psi and a sample standard deviation of $S_M = 80$ psi. Find a 95% confidence interval for $µ_I − µ_M$, assuming normality of breaking strengths of both types of yarn. Assume that $σ^2_I$ $\neq$ $σ^2_M$.

# In[13]:


stats.ttest_ind_from_stats(mean1=1400, mean2=1250, std1=120, std2=80, nobs1=61, nobs2=121, equal_var=False)


# Since we are assuming __normality and unequal variances__, we will calcualte the degrees of freedom using:
# ![image.png](attachment:image.png)

# In[14]:


# variables needed:
mean_difference = 1400 - 1250
n1 = 61
s1 = 120
n2 = 121
s2 = 80

# using unpooled method to calculate standard error
unpooled_se = np.sqrt(s1**2 / n1 + s2**2 / n2)

# calculating degrees of freedom
C = (s1**2/n1) / ((s1**2/n1) + (s2**2/n2))
df = ((n1 - 1) * (n2 - 1)) / ((n2 - 1) * C**2 + (1 - C)**2 * (n1 - 1))

# calculating the interval
stats.t.interval(alpha=0.95, df=df, loc=mean_difference, scale=unpooled_se)


# __Example 8.5.3__ (Confidence interval for $σ^2$ and σ) In a certain car-manufacturing company the time
# taken by a worker to finish a paint job on a car is normally distributed with mean µ and variance $σ^ 2$. Fifteen randomly selected car paint jobs are assigned to that worker and the time taken by the worker to finish each job is jotted down. These data yielded a sample standard deviation of S = 2.5 hours. Find a 95% two-sided confidence interval and one-sided lower and upper confidence intervals for the population variance $σ^2$ and the standard deviation σ.

# In[15]:


# Assign variables
alpha = 0.05
S = 2.5 
n = 15

# To obtain the two-sided confidence interval for σ^2
CI = [(n - 1)* S**2 / stats.chi2.ppf(1 - alpha / 2, n - 1), (n - 1)* S**2 / stats.chi2.ppf(alpha / 2,n - 1)]
print(CI)

# To obtain the two-sided confidence interval for σ
print(np.sqrt(CI))

# To obtain the one-sided confidence interval for σ^2
Lower_limit = (n - 1) * S**2 / stats.chi2.ppf(1 - alpha, n - 1)
print(Lower_limit)

Upper_limit = (n - 1) * S**2 / stats.chi2.ppf(alpha, n - 1)
print(Upper_limit) 

# To obtain the one-sided confidence interval for σ
print(np.sqrt(Lower_limit))
print(np.sqrt(Upper_limit))


# __Example 8.6.1__ (Confidence intervals for the ratio of two population variances) Two random samples of sizes 13 and 16 are selected from a group of patients with hypertension. The patients in the two samples are independently treated with drugs A and B. After a full course of treatments, these patients are evaluated. The data collected at the time of evaluation yielded sample standard deviations $S_A = S_1 = 6.5$ mmHg and $S_B = S_2 = 7.5$ mmHg. Assuming that the two sets of data come from independent normal populations with variances $σ^2_1$ and $σ^2_2$, respectively, determine a 95% two-sided confidence interval for $σ^2_1 / σ^2_2$. Also determine the one-sided confidence intervals for $σ^2_1 / σ^2_2$ and $σ_1/σ_2$.

# In[16]:


# Assign variables
alpha = 0.05
n1 = 13
n2 = 16
S1 = 6.5
S2 = 7.5

CI = [(S1**2 / S2**2) * (1 / stats.f.ppf(1 - alpha / 2,n1 - 1, n2 - 1)), (S1**2 / S2**2) * (1 / stats.f.ppf(alpha / 2,n1 - 1, n2 - 1))]
CI


# In[17]:


# To obtain the two-sided confidence interval for σ_1 / σ_2
np.sqrt(CI)


# __Example 8.7.1__ (Large sample confidence interval for binomial parameter p) A random sample of 400
# computer chips is taken from a large lot of chips and 50 of them are found to be defective. Find a 95% confidence interval for p the proportion of defective chips contained in the lot.

# In[18]:


# Assign variables
alpha = 0.05
T = 50
n = 400
phat = T / n

# To obtain the two-sided confidence interval for p
print([phat - stats.norm.ppf(1 - alpha / 2) * np.sqrt(phat * (1 - phat) / n), phat - stats.norm.ppf(alpha / 2) * np.sqrt(phat * (1 - phat) / n)])


# __Example 8.7.2__ (A large sample confidence interval for the difference of two binomial parameters ($p_1−p_2$)). Two companies A and B claim that a new type of light bulb has a lifetime of more that 5000 hours. In a random sample of 400 bulbs manufactured by company A, 60 bulbs burned out before the claimed lifetime and in another random sample of 500 bulbs manufactured by company B, 100 bulbs burned out before the claimed lifetime. Find a point estimate and a 95% confidence interval for the true value of the difference ($p_1−p_2$), where $p_1$ and $p_2$ are the proportion of the bulbs manufactured by company A and company B, respectively, that burn out before the claimed lifetime of 5000 hours.

# ![image.png](attachment:image.png)

# In[19]:


def two_proprotions_confint(success_a, size_a, success_b, size_b, alpha=0.05):
    prop_a = success_a / size_a
    prop_b = success_b / size_b

    # z critical value
    confidence = 1 - alpha
    z_score = abs(stats.norm.ppf(confidence + alpha / 2))

    se = np.sqrt((prop_a * (1 - prop_a)) / size_a  +  (prop_b * (1 - prop_b)) / size_b)
    
    prop_diff = prop_b - prop_a
    confint = prop_diff + np.array([-1, 1]) * z_score * se
    return confint


# In[20]:


two_proprotions_confint(success_a=60, size_a=400, success_b=100, size_b=500, alpha=0.05)

