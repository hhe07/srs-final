# Uses the brand new stuff from wikitionary! \0/

import re, pickle, os
import hanzidentifier as hz
from zhon import hanzi
import string


class Definition:
    def __init__(self,text):
        # Expects a single string line.
        if type(text) != str:
            raise TypeError
            pass
        self.original = text
        self.english = []
        self.pos = "" # Incorrect standard (not Penn Treebank), but you can't have everything.
        self.meta = "" # Perhaps can be used to provide some sort of sentiment information
        self.chinese = []
        self.zh_extra = []
        self.singleletter = "[English letter names are called as in English, no other standard Mandarin name exists]"
        self.parse(self.original)
    
    def parse(self,text):
        # Expects a single string line
        td = text.split("::") # Splits into English/Chinese sections
        eng = td[0] # English part
        zh = td[1] # Chinese part
        # English Component
        if "{" in eng:
            pos = re.search(" \{.*?\} ",eng).group() 
            eng = eng.replace(pos,"")
            self.pos = pos.replace("{","")
            self.pos = self.pos.replace("}","").lower()
        if "(" in eng:
            meta = re.search("\(.*?\) ",eng).group()
            eng = eng.replace(meta,"")
            self.meta = meta.replace("(","")
            self.meta = self.meta.replace(")","").lower()
        english = eng.replace("{"+self.pos+"}","")
        english = english.replace("("+self.meta+")","")
        self.english.append(english.replace(self.meta,"").lower())

        # Chinese component
        if self.singleletter in zh:
            replacesec = re.search("name of the letter \w",self.meta)
            self.chinese.append(zh.replace(replacesec.group(),""))
        else:
            allzh = zh.split(",")
            for x in allzh:
                isSimplified = hz.identify(x) is hz.SIMPLIFIED or hz.identify(x) is hz.BOTH
                if isSimplified:
                    s = re.search("[{}]+".format(hanzi.characters),x)
                    e = re.search("\(.*\)",x)
                    if s!=None:
                        self.chinese.append(s.group())
                    if e!=None:
                        self.zh_extra.append(e.group().lower())
    def __eq__(self,other):
        if isinstance(other,Definition):
            engequal = self.english==other.english
            zhequal = self.chinese = other.chinese
            return (engequal and zhequal)
        else:
            return False
## Test the definition class:
#f = open("en-cmn-enwiktionary.txt","r",encoding = "utf-8").read().split("\n")
#x = Definition(f[2915])


class Dictionary:
    def __init__(self,filename):
        # Expects a validly formatted file name.
        self.filename = filename
        self.terms = [] # TODO: Pickle?
        self.d(self.filename)
        self.terms.sort(key = lambda x: x.english[0][0:1].lower())
        self.div()

    def d(self,filename):
        # Expects a validly formatted file name.
        f = open(filename,"r",encoding = "utf-8")
        l = f.read().split("\n") # lines
        count = 0
        while True:
            text = l[count]
            isValid = re.search("^#",text)
            if isValid==None:
                self.terms.append(Definition(text))
            count+=1
            if count>=len(l)-1:
                break
        f.close()
    
    def div(self):
        # Expects nothing, other than that d didn't fail.
        try:
            os.mkdir(r"C:\Users\lge.DESKTOP-NNQ148M\programming\srs\use\newdict\div")
        except FileExistsError:
            pass
        os.chdir(r"C:\Users\lge.DESKTOP-NNQ148M\programming\srs\use\newdict\div")
        fl = self.terms[0].english[0][0:1]
        tmp = []
        letters = []
        count = 0
        for x in self.terms:
            l = x.english[0][0:1]
            if l !=fl:
                letters.append(fl)
                pickle.dump(tmp,open(fl+".p","wb"))
                #print(tmp[0].english)
                #print(tmp[len(tmp)-1].english)
                print("%s: %i" % (fl, len(tmp)))
                count+=len(tmp)
                fl = l
                tmp = [x]
            else:
                tmp.append(x)
        letters.append(fl)
        pickle.dump(tmp,open(fl+".p","wb"))
        print("%s: %i" % (fl, len(tmp)))
        count+=len(tmp)
        fl = l
        print("Length of Dumped: %i" % count)
        print("Length of Constructed: %i" % len(self.terms))
        #print(self.terms[0].english)
        #print(self.terms[len(self.terms)-1].english)
        print(list(dict.fromkeys(letters)))
        pickle.dump(self.terms,open("all.p","wb"))
                

    
def retrieve(text):
    os.chdir(r"C:\Users\lge.DESKTOP-NNQ148M\programming\srs\use\newdict\div")
    fl = text[0:1]
    try:
        l = pickle.load(open(fl+".p","rb"))
        for d in l:
            if text == d.english[0]:
                os.chdir(r"C:\Users\lge.DESKTOP-NNQ148M\programming\srs\use")
                return d
        os.chdir(r"C:\Users\lge.DESKTOP-NNQ148M\programming\srs\use")
        return None
    except FileNotFoundError:
        os.chdir(r"C:\Users\lge.DESKTOP-NNQ148M\programming\srs\use")
        return None
    except OSError:
        os.chdir(r"C:\Users\lge.DESKTOP-NNQ148M\programming\srs\use")
        return None
    
#x = Dictionary("en-cmn-enwiktionary.txt")
#print(retrieve("an").chinese)


#x.checkFiles()
#os.chdir(r"C:\Users\lge.DESKTOP-NNQ148M\programming\srs\use\newdict\div")
#t = pickle.load(open("a.p","rb"))
#print(len(t))
#checkFiles()

## Test out a div. Also, oh my God the Python commenting system sucks

#os.chdir(r"C:\Users\lge.DESKTOP-NNQ148M\programming\srs\newdict\div")
#x = pickle.load(open("b.p","rb"))
#print(x[len(x)-1].english)
#print(x[0].english)
