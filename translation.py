import babelquery.abstr as ba
import babelquery.babelquery
from newdict.newdict import Definition, retrieve

key = "9c7dbd16-9086-4b7b-82ee-d1393fda04e3"

def translate(word,key,precision): 
    ret = []
    dt = retrieve(word)
    if dt!=None:
        ret.extend(dt.chinese)
    if precision or dt==None:
        bn = ba.getRelatedWords(word,None,key)
        ret.extend(bn)
    ret = list(dict.fromkeys(ret))
    return ret

print(translate("apple",key,True))