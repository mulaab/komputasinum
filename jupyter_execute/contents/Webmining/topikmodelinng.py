#!/usr/bin/env python
# coding: utf-8

# # Topic Modeling

# ## Apa itu Topic Modeling?

# - Topic modeling adalah metode pembelajaran tak terawasi (**unsupervised** learning), dimana tujuannya adalah untuk mengektrak pola semantik diantara sekumpulan data. Struktur dasar semantik ini dikenal dengan topik
# - Tentunya, pertama kali yang dilakukan pada proses topic modeling adalah mengektrak fitur dari kata-kata dalam dokumen-dokumen. Selanjutnya menggunakan struktur matematika dan framework misalkan faktorisasi matrik dan SVD (SIngular Value Decompotition) untuk menentukan kelompok kata kata yang memberikan koherensi semantik yang paling besar.
# - Kelompok kata-kata ini membentuk gagasan topik topik.
# - Sementara itu, framewrok matematika juga akan menentukan distribusi **topik** ini untuk setiap dokumen.
# 

# - Secara singkat , topik modelling adalah:
#     - Setiap **dokumen** terdiri dari beberapa  **topik** ( distribusi dari beberapa topik)
#     - Setiap topik berkaitan dengan sekumpulan  **kata-kata** (distribusi dari beberapa kata-kata).

# ## Flowchart untuk  Topic Modeling

# ![](topicpipeline.jpeg)

# ## Persiapan Data dan Praproses

# 

# In[1]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import re
import nltk
import matplotlib.pyplot as plt

pd.options.display.max_colwidth = 200
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Kumpulan dokumen (Corpus)
# 

# - Menggunakan 8 dokumen sebagai contoh 

# In[2]:


corpus = [
    'The sky is blue and beautiful.', 'Love this blue and beautiful sky!',
    'The quick brown fox jumps over the lazy dog.',
    "A king's breakfast has sausages, ham, bacon, eggs, toast and beans",
    'I love green eggs, ham, sausages and bacon!',
    'The brown fox is quick and the blue dog is lazy!',
    'The sky is very blue and the sky is very beautiful today',
    'The dog is lazy but the brown fox is quick!'
]
labels = [
    'weather', 'weather', 'animals', 'food', 'food', 'animals', 'weather',
    'animals'
]

corpus = np.array(corpus)
corpus_df = pd.DataFrame({'Document': corpus, 'Category': labels})
corpus_df = corpus_df[['Document', 'Category']]
corpus_df


# ### Praproses  teks (data)

# - Bergantung pada dokumen yang diproses, praproses disesuaikan dengan kebutuhan terhadap kumpulan data tersebut
# - Pada contoh dilakukan beberapa proses:
#     - menghilangkan simbol dan  tanda baca
#     - menormalisasi huruf (case folding)
#     - menghapus spasi  yang tidak perlu/berlebihan
#     - menghilangkan stopword
# 

# tambahan praproses teks jika diperlukan:
# - menghilangkan  tanda hubung
# - Stemming
# - Menghilangkan kata-kata yang tidak ada di wordnet
# - Melakukan pembakuan kata
# 

# In[3]:


import nltk
nltk.download('stopwords')
wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')


def normalize_document(doc):
    # lower case and remove special characters\whitespaces
    doc = re.sub(r'[^a-zA-Z\s]', '', doc, re.I | re.A)
    doc = doc.lower()
    doc = doc.strip()
    # tokeanize document
    tokens = wpt.tokenize(doc)
    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # re-create document from filtered tokens
    doc = ' '.join(filtered_tokens)
    return doc


normalize_corpus = np.vectorize(normalize_document)


# In[4]:


norm_corpus = normalize_corpus(corpus)
norm_corpus


# - The `norm_corpus` akan dijadikan sebagai input untuk langkah selanjutnya yaitu vektorisasi text.

# ## Vektorisasi teks

# ### Model Bag of Words 

# - Pada  topic modeling, cara paling sederhana vektorisasi teks adalah membentuka fitur berbasis model Bag-of-Words .
# - Ciri dari model  BOW
#     - membentuk vektorisasi teks kedalam representasi merik menggunakan daftar banyaknya kemunculan kata 
#     - Urutan kata yang  dalam teks diabaikan.
#     
# - Gunakan vektorisasi berbasi  **jumlah** pada  topik modeling karena sebagian besar topik modelling menggunakan pembobotan dalam proses komputasinya

# In[5]:


from sklearn.feature_extraction.text import CountVectorizer
# get bag of words features in sparse format
cv = CountVectorizer(min_df=0., max_df=1.)
cv_matrix = cv.fit_transform(norm_corpus)
cv_matrix


# In[6]:


# view dense representation
# warning might give a memory error if data is too big
cv_matrix = cv_matrix.toarray()
cv_matrix


# In[7]:


# Mendapatkan kata-kata dari corpus
vocab = cv.get_feature_names()
# menampilkan vektor  dokumen-fitur
pd.DataFrame(cv_matrix, columns=vocab)


# ## Latent Dirichlet Allocation

# ###  LDA (Latent Dirichlet  Allocation)

# - Latent Dirichlet [diʀiˈkleː] Allocation mempelajari hubungan antara  **kosa kata**, **topik**, and **dokumen** dengan mengasumsikan suatu dokumen dibuat dengan model probabilitas tertentu.
# - Topik pada LDA adalah berdistribusi multinomial distribution terhadap kosa kata-kosa kata  dari kumpulan dokumen (corpus). (Suatu topik tertentu, dinyatakan dengan kosakata-kosatakat tertentu)

# - Dengan LDA kita tahu:
#     - Kosa kata apa yang lebih memungkinkan terkait dengan topik tertentu? (Topic by Word Matrix)
#     - Topik-topik yang mana yang lebih memungkinkan terkait dengan suatu dokumen tertentu? (Document by Topic Matrix)
#     

# - Untuk menginterpretasikan topik dalam LDA, kita memperhatikan daftar peringkat dkata-kata yang paling mungkin (N teratas) dalam topik itu.
# - Kata-kata umum dalam korpus yang sering muncul pada  bagian atas kata untuk setiap topik, yang terkadang membuat sulit untuk membedakan arti dari topik ini.
# - Saat memperhatikan peringkat kata untuk setiap topik, kita dapat menggunakan dua jenis informasi yang disediakan oleh LDA:
#     - Frekuensi kata-kata pada setiap topik
#     - Eksklusivitas kata-kata terhadap topik (yaitu, sejauh mana kata itu muncul dalam topik tertentu dengan mengesampingkan yang lain).

# ### Membangun model LDA 

# - Mengunakan `CountVectorizer`, tidak menggunakan`TfidfVectorizer` karena  LDA didasarkan pada jumlah kata dan jumlah dokumen. 
# 

# In[8]:


get_ipython().run_cell_magic('time', '', 'from sklearn.decomposition import LatentDirichletAllocation\n\nlda = LatentDirichletAllocation(n_components=3, max_iter=10000, random_state=0)\ndoc_topic_matrix = lda.fit_transform(cv_matrix)\n')


# In[9]:


import tmplot as tmp
import pickle as pkl
import pandas as pd


# In[10]:


phi = tmp.get_phi(doc_topic_matrix)
print(phi)


# ### Ukuran performansi Model 

# - Uji model menggunakan  **perplexity** dan **log-likelihood**.
#     - Semakin tinggi log-likelihood, semakin baik.
#     - Semakin rendah perplexity, semakin baik .
#     
#     $$
#     \mathcal L (\boldsymbol w)
#     = \log p(\boldsymbol w | \boldsymbol \Phi, \alpha)
#     = \sum_d \log p(\boldsymbol w_d | \boldsymbol \Phi, \alpha).
#     $$
#     
#     
#     $$
#     \text{perplexity}(\text{test set } w) =
#         \exp \left\{
#         - \frac{\mathcal L( w)}{\text{count of tokens}}
#         \right\}
#     $$
#     
#     
#         
#     lihat referensi http://qpleple.com/perplexity-to-evaluate-topic-models/

# In[11]:


# log-likelihood
print(lda.score(cv_matrix))
# perplexity
print(lda.perplexity(cv_matrix))


# ## Interpretasi

# - Untuk menginterpretasikan dengan benar hasil yang diberikan oleh LDA, kita perlu mendapatkan dua matriks penting:
#     - Matrik **Document-by-Topic** : ini adalah matriks yang dikembalikan oleh `LatentDirichletAllocation`  ketika menggunakan model `fit_transform()` pada data.
#     - Matrik **Word-by-Topic**: Kami dapat mengambil matriks ini dari hasil LatentDirichletAllocation.components

# ### Matrik Document-by-Topic 

# - Pada matrik **Document-by-Topic** , dapat dilihat bagaiman setiap dokumen terkait dengan suatu topik-topik
# - Tentunya, nilainya menyatakan nilai probabilitas dokumen terhadapa topik tertentu

# In[12]:


## doc-topic matrix
doc_topic_df = pd.DataFrame(doc_topic_matrix, columns=['T1', 'T2', 'T3'])
doc_topic_df


# ### Matrik Topic-by-Word

# - Pada matrik  **Topic-by-Word** , dapat dilihat bagaiman masing masing topik berkaitan degan setiap kata-kata dalam  BOW.
# - Tentunya,  nilainya  menyatakan pentingnya suatu kata terhadap masing masing topik 

# In[13]:


topic_word_matrix = lda.components_


# In[16]:


pd.DataFrame(topic_word_matrix, columns=vocab)


# - Kita lakukan transport matrik dari data diatas untuk mempermudah analisanya

# In[18]:


pd.DataFrame(np.transpose(topic_word_matrix), index=vocab)


# ### Interpretasi makna  Topik

# - Ini adalah langkah mendasar dalam topic modeling.LDA tidak memberikan label untuk setiap topik
# - Seorang Analislah yang menentukan makna topik..
# - Keputusan ini didasarkan pada kata-kata pada masing masing topik yang memperlihatkan bobot penting yang paling tinggi 

# In[19]:


## This function sorts the words importances under each topic
## and the selectional criteria include (a) ranks based on weights, or (b) cutoff on weights
def get_topics_meanings(tw_m,
                        vocab,
                        display_weights=False,
                        topn=5,
                        weight_cutoff=0.6):
    for i, topic_weights in enumerate(tw_m):  ## for each topic row
        topic = [(token, np.round(weight, 2))
                 for token, weight in zip(vocab, topic_weights)
                 ]  ## zip (word, importance_weight)
        topic = sorted(topic,
                       key=lambda x: -x[1])  ## rank words according to weights
        if display_weights:
            topic = [item for item in topic if item[1] > weight_cutoff
                     ]  ## output words whose weights > 0.6
            print(f"Topic #{i} :\n{topic}")
            print("=" * 20)
        else:
            topic_topn = topic[:topn]
            topic_topn = ' '.join([word for word, weight in topic_topn])
            print(f"Topic #{i} :\n{topic_topn}")
            print('=' * 20)


# - Untuk menggunakan fungsi diatas :
#   - Jika kita ingin menampilkan bobot  kata-kata, maka kita perlu menetapkan  `weight_cutoff`.
#   - JIka akan menampilkan hanya N kata teratas, maka kita tetapkan dengan  `topn`.

# In[20]:


get_topics_meanings(topic_word_matrix,
                    vocab,
                    display_weights=True,
                    weight_cutoff=2)


# In[54]:


get_topics_meanings(topic_word_matrix, vocab, display_weights=False, topn=3)


# ## Topik topik dalam dokumen-dokumen

# - Setelah kita, menentukan makna topik, kita dapat menganalisa bagaimana masing masing dokumen terkait dengan topik topik
# - Perhatikan matrik **Document-by-Topic** 

# In[21]:


topics = ['weather', 'food', 'animal']
doc_topic_df.columns = topics
doc_topic_df['corpus'] = norm_corpus
doc_topic_df


# - Kita dapat memvisualisasikan distribusi topik untuk setiap dokumen 

# In[22]:


x_axis = ['DOC' + str(i) for i in range(len(norm_corpus))]
y_axis = doc_topic_df[['weather', 'food', 'animal']]

fig, ax = plt.subplots(figsize=(15, 8))

# Plot a stackplot - https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/stackplot_demo.html
ax.stackplot(x_axis, y_axis.T, baseline='wiggle', labels=y_axis.columns)

# Move the legend off of the chart
ax.legend(loc=(1.04, 0))


# ## Melakukan pengelopokkan Clustering dokuemn menggunakan fitur  topic modeling

# In[23]:


from sklearn.cluster import KMeans

km = KMeans(n_clusters=3, random_state=0)
km.fit_transform(doc_topic_matrix)
cluster_labels = km.labels_
cluster_labels = pd.DataFrame(cluster_labels, columns=['ClusterLabel'])
pd.concat([corpus_df, cluster_labels], axis=1)


# ## Prediksi Topik

# - Model yang sudah dibuat dapat digunakan untuk memprediksi topik pada dokumen baru

# In[24]:


new_texts = ['The sky is so blue', 'Love burger with ham']

new_texts_norm = normalize_corpus(new_texts)
new_texts_cv = cv.transform(new_texts_norm)
new_texts_cv.shape


# In[26]:


new_texts_doc_topic_matrix = lda.transform(new_texts_cv)
topics = ['weather', 'food', 'animal']
new_texts_doc_topic_df = pd.DataFrame(new_texts_doc_topic_matrix,
                                      columns=topics)
new_texts_doc_topic_df['predicted_topic'] = [
    topics[i] for i in np.argmax(new_texts_doc_topic_df.values, axis=1)
]

new_texts_doc_topic_df['corpus'] = new_texts_norm
new_texts_doc_topic_df


# ## Evaluasi topik modelling

# - The following codes demonstrate how to find the optimal topic number based on the coherence scores of the topic models.

# ## Refensi
# 
# - Sarkar (2019), Chapter 6: Text Summarization and Topic Models
