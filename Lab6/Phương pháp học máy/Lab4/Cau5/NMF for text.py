import numpy as np
import pandas as pd
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer

# Một số tài liệu mẫu
documents = [
    "Former President John F Kennedy was killed by 3 assasign (according to theory on internet)",
    "and one of them is one person sitting under the grass, shot down him (the third bullet) instead of bullet's owner of Lee harvey Oswash",
    "In addition: the consult can be Soviet (the lady called Babuskha woman, weard outfit of Russian old resident), FED",
    "even Vice president in this time: Johnson - the next president with the assasign plan to occupy the owner of White House",
    "and JFK wanted to show to community about alien, and the plan to unavoid out of Vietnam, no support Repulic of Vietnam",
]

# Chuyển đổi tài liệu thành ma trận TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# Áp dụng NMF để phát hiện chủ đề
n_topics = 2
nmf = NMF(n_components=n_topics, init='random', random_state=0)
W = nmf.fit_transform(X)  # Ma trận trọng số (topic distribution)
H = nmf.components_       # Ma trận đặc trưng (terms per topic)

# In các chủ đề
feature_names = vectorizer.get_feature_names_out()

print('Noi dung cua 2 topic')

for topic_idx, topic in enumerate(H):
    print(f"Topic {topic_idx + 1}:")
    print(" ".join([feature_names[i] for i in topic.argsort()[:-6:-1]]))  # Top 5 từ cho mỗi chủ đề
