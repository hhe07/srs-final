import xml.etree.ElementTree as ET
import time
import pickle
def intoPickle(xml_file):
    text = []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for paragraph in root.iter("p"):
        sent = ""
        for sentence in paragraph.iter("s"):
            for word in sentence.iter("w"):
                sent = sent+word.text+""
        text.append(sent)
    pickle.dump(text,open(xml_file+".p","wb"))

#intoPickle("sce.xml")
intoPickle("sce_zh.xml")

def pairData(sce1,sce2):
    paired = []
    sce1 = pickle.load(open(sce1+".p","rb"))
    sce2 = pickle.load(open(sce2+".p","rb"))
    for x in range (0,len(sce1)-1):
        paired.append([sce1[x],sce2[x]])
    pickle.dump(paired,open("paired.p","wb"))

#pairData("sce.xml","sce_zh.xml")