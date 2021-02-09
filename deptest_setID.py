# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 21:45:12 2020

@author: 64584
"""

import xml.etree.ElementTree as ET
tree = ET.parse("deptest.eaf")
enonce = tree.findall(".//TIER[@TIER_ID = 'ENONCE']/ANNOTATION/ALIGNABLE_ANNOTATION")
EN = []
for e in enonce :
    EN.append(e.attrib['ANNOTATION_ID'])

i = 0
for a in tree.findall(".//TIER[@TIER_ID='id']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i+1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='TYPEPRODUCTION']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='INTERVENTION']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='LOCUTEUR']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='ORIGINE']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='POPULATIONANNEXE']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='CLASSE']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='VALENCE']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='COMMENT']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='REFERENTA0']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='INTEGRATIONSYNTAXIQUE']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='FORMESN']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='TRADUCTION']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='FORMESUJET']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='PREDICAT']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='CLITIQUEOBJET']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='FORMEVERBE']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1

i = 0
for a in tree.findall(".//TIER[@TIER_ID='INDICATIONSCENIQUE']/ANNOTATION/REF_ANNOTATION"):
    a.set("ANNOTATION_REF", EN[i])
    i = i + 1
    

tree.write("deptest.eaf")