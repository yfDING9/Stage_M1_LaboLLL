# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:49:17 2020

@author: 64584
"""

import xml.etree.ElementTree as ET
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import Birch
import numpy as np

class Cluster():
    def corpus(self):
        tree = ET.parse('39.eaf')
        root = tree.getroot() #récupérer la racine
        
        self.title_dict = {}
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
            c = 0
            for token in b:
                text_new.append(token)
                c = c+1

            
            index = 0
            for token in text_new :
                self.title_dict[index] = token
                index +=1
        
            cv = CountVectorizer(analyzer = "char", strip_accents="unicode",vocabulary=ipa)
            cv_fit = cv.fit_transform(text_new)
            self.weight = cv_fit.toarray()
            
        print(c)
            

    def birch_cluster(self):
        print ('start cluster Birch -------------------' )
        self.cluster = Birch(threshold=0.6,n_clusters=None)
        self.cluster.fit_predict(self.weight)
    
    def get_title(self):
        cluster_dict = {}
        for index,value in enumerate(self.cluster.labels_):
            if value not in cluster_dict:
                cluster_dict[value] = [index]
            else :
                cluster_dict[value].append(index)
        
        
       
        
        
        result_dict = {}
        for indexs in cluster_dict.values():
            latest_index = indexs[0]
            similar_num = len(indexs)
            if len(indexs)>=2:
                min_s = np.sqrt(np.sum(np.square(self.weight[indexs[0]]-self.cluster.subcluster_centers_[self.cluster.labels_[indexs[0]]])))
                for index in indexs:
                    s = np.sqrt(np.sum(np.square(self.weight[index]-self.cluster.subcluster_centers_[self.cluster.labels_[index]])))
                    if s<min_s:
                        min_s = s
                        latest_index = index
            
            title = self.title_dict[latest_index]
            
            result_dict[title] = similar_num
        
        

        
        print(sorted(result_dict.items(),key = lambda item:item[1],reverse = True))
        return result_dict
    
    def run(self):
        self.corpus()
        self.birch_cluster()
        self.get_title()


if __name__=='__main__':
    cluster = Cluster()
    cluster.run()
    