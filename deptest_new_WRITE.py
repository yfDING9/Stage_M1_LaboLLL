# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 23:33:25 2020

@author: 64584
"""

from xml.etree.ElementTree import SubElement,Element
import xml.etree.ElementTree as ET
import datetime
from xml.dom import minidom

tree_origin = ET.parse("19a.eaf")



tree_new_bee = Element("ANNOTATION_DOCUMENT")
tree_new_bee.set("xmlns:xsi","http://www.w3.orgn/2001/XMLSchema-instance")
tree_new_bee.set("AUTHOR"," ")
tree_new_bee.set("DATE",str(datetime.date.today()))
tree_new_bee.set("FORMAT","3.0")
tree_new_bee.set("VERSION","3.0")
tree_new_bee.set("xsi:noNamespaceSchemaLocation","http://www.mpi.nl/tools/elan/EAFv3.0.xsd")



header = SubElement(tree_new_bee,"HEADER")
header.set("MEDIA_FILE", "")
header.set("TIME_UNITS","milliseconds")
prop = SubElement(header,"PROPERTY")
prop1 = SubElement(header,"PROPERTY")
prop.set("NAME","URN")
prop.text = tree_origin.findtext(".//HEADER/PROPERTY[@NAME ='URN']")
prop1.set("NAME","lastUsedAnnotationId")
prop1.text = tree_origin.findtext(".//HEADER/PROPERTY[@NAME ='lastUsedAnnotationId']")



time_order = SubElement(tree_new_bee,"TIME_ORDER")
temps = []
temps_value = []
for a in tree_origin.findall(".//TIME_ORDER/TIME_SLOT"):
    temps.append(a.attrib['TIME_SLOT_ID'])
    temps_value.append(a.attrib['TIME_VALUE'])

for i in range(0,len(temps)):
    slot = SubElement(time_order,"TIME_SLOT")
    slot.set("TIME_SLOT_ID",temps[i])
    slot.set('TIME_VALUE',temps_value[i])



def set_parent (tier_name,xpath_time,xpath_text):
    line = SubElement(tree_new_bee,"TIER")
    line.set("ANNOTATOR","kp")
    line.set("LINGUISTIC_TYPE_REF","default-lt")
    line.set("TIER_ID",tier_name)
    
    ts1 = []
    ts2 = []
    
    for b in tree_origin.findall(xpath_time):
        ts1.append(b.attrib["TIME_SLOT_REF1"])
        ts2.append(b.attrib["TIME_SLOT_REF2"])
        
    
    text = tree_origin.findall(xpath_text)
    for i in range(0,len(ts1)):
        annotation = SubElement(line,"ANNOTATION")
        align = SubElement(annotation,"ALIGNABLE_ANNOTATION")
        align.set("TIME_SLOT_REF1",ts1[i])
        align.set("TIME_SLOT_REF2",ts2[i])
        annotation_value = SubElement(align, "ANNOTATION_VALUE")
        annotation_value.text = text[i].text

set_parent("portion",".//TIER[@TIER_ID='portions']/ANNOTATION/ALIGNABLE_ANNOTATION",".//TIER[@TIER_ID='portions']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
set_parent("sequence",".//TIER[@TIER_ID='sequence']/ANNOTATION/ALIGNABLE_ANNOTATION",".//TIER[@TIER_ID='sequence']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
set_parent("ENONCE",".//TIER[@TIER_ID='ENONCE']/ANNOTATION/ALIGNABLE_ANNOTATION",".//TIER[@TIER_ID='ENONCE']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")

a = 0
def set_child(tier_name,xpath_text):
    line = SubElement(tree_new_bee,"TIER")
    line.set("LINGUISTIC_TYPE_REF","annotation")
    line.set("PARENT_REF","ENONCE")
    line.set("TIER_ID",tier_name)
    
    text = tree_origin.findall(xpath_text)
    
    for i in range(0,len(text)):
        annotation = SubElement(line,"ANNOTATION")
        ref = SubElement(annotation,"REF_ANNOTATION")
        ref.set("ANNOTATION_ID",str(a+1))
        ref.set("ANNOTATION_REF","")
        VALUE = SubElement(ref,"ANNOTATION_VALUE")
        VALUE.text = text[i].text
        
    return a

a = set_child("id",".//TIER[@TIER_ID='id']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("TYPEPRODUCTION",".//TIER[@TIER_ID='TYPEPRODUCTION']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("INTERVENTION",".//TIER[@TIER_ID='INTERVENTION']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("LOCUTEUR",".//TIER[@TIER_ID='LOCUTEUR']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("ORIGINE",".//TIER[@TIER_ID='ORIGINE']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("POPULATIONANNEXE",".//TIER[@TIER_ID='POPULATIONANNEXE']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("CLASSE",".//TIER[@TIER_ID='CLASSE']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("VALENCE",".//TIER[@TIER_ID='VALENCE']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("COMMENT",".//TIER[@TIER_ID='COMMENT']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("REFERENTA0",".//TIER[@TIER_ID='REFERENTA0']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("INTEGRATIONSYNTAXIQUE",".//TIER[@TIER_ID='INTEGRATIONSYNTAXIQUE']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("FORMESN",".//TIER[@TIER_ID='FORMESN']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("TRADUCTION",".//TIER[@TIER_ID='TRADUCTION']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("FORMESUJET",".//TIER[@TIER_ID='FORMESUJET']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("PREDICAT",".//TIER[@TIER_ID='PREDICAT']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("CLITIQUEOBJET",".//TIER[@TIER_ID='CLITIQUEOBJET']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("FORMEVERBE",".//TIER[@TIER_ID='FORMEVERBE']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_child("INDICATIONSCENIQUE",".//TIER[@TIER_ID='INDICATIONSCENIQUE']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")

def set_included_in(tier_name,xpath_time,xpath_text):
    line = SubElement(tree_new_bee,"TIER")
    line.set("LINGUISTIC_TYPE_REF","Annot")
    line.set("PARENT_REF","ENONCE")
    line.set("TIER_ID",tier_name)
    
    ts1 = []
    ts2 = []
    
    for b in tree_origin.findall(xpath_time):
        ts1.append(b.attrib["TIME_SLOT_REF1"])
        ts2.append(b.attrib["TIME_SLOT_REF2"])
        
    
    text = tree_origin.findall(xpath_text)
    for i in range(0,len(ts1)):
        annotation = SubElement(line,"ANNOTATION")
        align = SubElement(annotation,"ALIGNABLE_ANNOTATION")
        align.set("ANNOTATION_ID",str(a+1))
        align.set("TIME_SLOT_REF1",ts1[i])
        align.set("TIME_SLOT_REF2",ts2[i])
        annotation_value = SubElement(align, "ANNOTATION_VALUE")
        annotation_value.text = text[i].text
    
    return a

a = set_included_in("Enonce-token",".//TIER[@TIER_ID='Enonce-token']/ANNOTATION/ALIGNABLE_ANNOTATION",".//TIER[@TIER_ID='Enonce-token']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_included_in("LEMME",".//TIER[@TIER_ID='LEMME']/ANNOTATION/ALIGNABLE_ANNOTATION",".//TIER[@TIER_ID='LEMME']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_included_in("HypForte",".//TIER[@TIER_ID='HypForte']/ANNOTATION/ALIGNABLE_ANNOTATION",".//TIER[@TIER_ID='HypForte']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_included_in("HypFaible",".//TIER[@TIER_ID='HypFaible']/ANNOTATION/ALIGNABLE_ANNOTATION",".//TIER[@TIER_ID='HypFaible']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_included_in("SUPPORT",".//TIER[@TIER_ID='SUPPORT']/ANNOTATION/ALIGNABLE_ANNOTATION",".//TIER[@TIER_ID='SUPPORT']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")
a = set_included_in("Commentaire-V",".//TIER[@TIER_ID='Commentaire-V']/ANNOTATION/ALIGNABLE_ANNOTATION",".//TIER[@TIER_ID='Commentaire-V']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE")


    



n = 1
for elem in tree_new_bee.findall("./TIER/ANNOTATION/ALIGNABLE_ANNOTATION"):
    elem.set("ANNOTATION_ID","a"+str(n)) #mettre l'annotation_id dans les balises
    n+=1

for elem in tree_new_bee.findall("./TIER/ANNOTATION/REF_ANNOTATION"):
    elem.set("ANNOTATION_ID","a"+str(n)) #mettre l'annotation_id dans les balises
    n+=1
    
    

default = SubElement(tree_new_bee,"LINGUISTIC_TYPE")
default.set('GRAPHIC_REFERENCES','false')
default.set('LINGUISTIC_TYPE_ID','default-lt')
default.set('TIME_ALIGNABLE','true')

imp = SubElement(tree_new_bee,"LINGUISTIC_TYPE")
imp.set('GRAPHIC_REFERENCES','false')
imp.set('LINGUISTIC_TYPE_ID','imported-sep')
imp.set('TIME_ALIGNABLE','true')

sa =  SubElement(tree_new_bee,"LINGUISTIC_TYPE")
sa.set("CONSTRAINTS","Symbolic_Association")
sa.set('GRAPHIC_REFERENCES','false')
sa.set('LINGUISTIC_TYPE_ID','annotation')
sa.set('TIME_ALIGNABLE','false')

inc = SubElement(tree_new_bee,"LINGUISTIC_TYPE")
inc.set('GRAPHIC_REFERENCES','false')
inc.set('LINGUISTIC_TYPE_ID','Annot')
inc.set('TIME_ALIGNABLE','true')


xml_string = ET.tostring(tree_new_bee)

xml = minidom.parseString(xml_string)

xml = xml.toprettyxml(indent = "\t")

file = open("deptest.eaf","w",encoding = "utf-8")
file.write(xml)
file.close()


#




