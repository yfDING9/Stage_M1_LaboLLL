# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sklearn.feature_extraction.text import CountVectorizer
import xml.etree.ElementTree as ET
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


tree = ET.parse('25a.eaf')
root = tree.getroot() #récupérer la racine


vectorizer = CountVectorizer(min_df=1)
ipa = ["a","ɑ","ɐ","e","ɛ","ɜ","i","ɪ","o","ɔ","ɒ","u","ʊ","y",
       "ʏ","ə","ø","ɵ","œ","ɶ","ã","ɑ̃","ẽ","ɛ̃","æ̃","õ","ɔ̃","œ̃",
       "b","p","d","t","g","k","v","f","z","s","ʒ","ʃ","m","n",
       "ɲ","ŋ","r","ɹ","ʀ","ʁ","x","χ","l","j","ʎ","w","ɥ"]

text = []
for a in root.findall(".//TIER[@TIER_ID='ENONCE']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE"):
    text.append(a.text)

text_new = []
for item in text :
    item = item.replace(' ','')
    item = item.replace("+","/")
    b = item.split("/")
    for token in b:
        text_new.append(token)
        
cv = CountVectorizer(analyzer = "char", strip_accents="unicode",vocabulary=ipa)
cv_fit = cv.fit_transform(text_new)
C = cv_fit.toarray()
print(C)

def train (X,vectorizer, true_k = 500, showLable = True):
    km = KMeans(n_clusters=true_k,init='k-means++',n_init = 1, verbose = False)
    km.fit(X)
    result = list(km.predict(X))
    print(dict([(i,result.count(i))for i in result]))
    if showLable:
        print("Top terms per cluster:")
        order_centroids = km.cluster_centers_.argsort()[:, ::-1]
        terms = text_new
        for i in range(true_k):
            print("Cluster %d:" % i, end='')
            print("\n") 
            for ind in order_centroids[i]:
                print(' %s' % terms[ind], end='\n')
    
    return km.inertia_

def test():
    dataset = text_new
    true_ks = []
    scores = []
    for i in range(3,80,1):
        score = train(cv_fit,cv,true_k = i)/len(dataset)
        print(i,score)
        true_ks.append(i)
        scores.append(score)
    
    plt.figure(figsize = (8,4))
    plt.plot(true_ks,scores,label = "error", color = "red", linewidth = 1)
    plt.xlabel("n_features")
    plt.ylabel("error")
    plt.legend()
    plt.show()

train(cv_fit,cv)

