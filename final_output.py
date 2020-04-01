from finaltrans import transsent
from finaltrans import translate
from textblob import TextBlob
from newdict.newdict import Definition, retrieve
en = open("1000en.txt", encoding="utf-8")

tb_file = open("ibm10002.txt", "w", encoding="utf-8")
base_file = open("basefile2.txt", "w", encoding="utf-8")
markov_file = open("markov10002.txt", "w", encoding="utf-8")
markov_extra = open("markov_extra2.txt", "w", encoding="utf-8")
for x in range(0, 193):
    line = en.readline()
for x in range(194, 250):
    print(x)
    
    line = en.readline()
    
    print(line)
    
    ref = translate(line, None, None, False)[0] + "\n"
    print(ref)
    tb_file.write(ref)

    markov = transsent(line, False)+"\n"
    print(markov)
    markov_file.write(markov)

    markov_e = transsent(line, True) + "\n"
    print(markov_e)
    markov_extra.write(markov_e)
    base = ""
    l = line.split(" ")
    for x in l:
        tr = translate(x, None,None, False)
        if tr!=[]:
            if tr[0] == " [English letter names are called as in English, no other standard Mandarin name exists]":
                base += l
            else:
                base += tr[0]
    base += "\n"
    print(base)
    base_file.write(base)
