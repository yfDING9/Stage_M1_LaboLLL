# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 23:30:49 2020

@author: 64584
"""

import xml.etree.ElementTree as ET
import difflib


tree = ET.parse('25b.eaf')
root = tree.getroot() #récupérer la racine

text = []
for a in root.findall(".//TIER[@TIER_ID='ENONCE']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE"):
    text.append(a.text)

text_new = []
com = 0
for item in text :
    item = item.replace(' ','')
    item = item.replace("+","/")
    b = item.split("/")
    for token in b:
        text_new.append(token)
        com = com+1

        

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

a = []
phrase = input("phrase ciblée(en API) : ")
for item in text_new :
    a.append(string_similar(phrase,item))


c = []
for i,element in enumerate(a):
    if element >=0.7 :
        c.append(i)

for n in c :
    print(text_new[n:n+5])

name = input("locuteur: ")
index = []
for i,element in enumerate(text):
    if name in element :
        index.append(i)

locuteur = root.findall(".//TIER[@TIER_ID='LOCUTEUR']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
for i, element in enumerate(locuteur):
    for n in index :
        if n == i :
            print(element.text)

print(com)
#les noms qui est dedans : boucle sens inverse à partir des noms, rechercher des contextes
#noter les prénoms