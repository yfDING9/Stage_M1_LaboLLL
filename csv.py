# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:12:00 2020

@author: 64584
"""

"""permet de générer le temps de début 
et le temps de fin à base de nombre du mot dans chaque énoncé (séparé par / ou +)
exemple : 16a.csv
"""


import pandas as pd
#from lxml import etree

data = []
data = pd.read_csv("IV.01.csv","\t", usecols = [3])
enonce = data.values.tolist()#récupérer le contenu d'une colonne

tree = etree.parse("26.eaf")

c = []

for item in enonce :
    for token in item :
        compteur = len(token)
        c.append(compteur)

dictTimecodes = {}
for timecode in tree.findall("//TIME_ORDER/TIME_SLOT"):
    dictTimecodes[timecode.get("TIME_SLOT_ID")] = timecode.get("TIME_VALUE")
             
    
y =  tree.findall(".//TIER[@TIER_ID='sequences']/ANNOTATION/ALIGNABLE_ANNOTATION/")
for x in y :
   partie = x.find("ANNOTATION_VALUE").text
   if "28-125" in partie :
       start = int(dictTimecodes[x.get("TIME_SLOT_REF1")])
       end = int(dictTimecodes[x.get("TIME_SLOT_REF2")])
 

time = int(end) - int(start)
t = time // (sum(c))

b=[]
b.append(start)
for i in c[:-1] :
    start = int(start) + (t*i)
    b.append(start)
test = pd.DataFrame(b) #transformer liste au format tableur
test.to_csv("IV.01.csv", mode = "a", index = False)








    



    
    

        
