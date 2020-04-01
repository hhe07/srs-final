from pos_caster import castPos, quickPosMap
#from translation import translate
from newdict.newdict import Definition, retrieve
from markov import pos_creator
from stanfordcorenlp import StanfordCoreNLP

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#from textblob import TextBlob
#from textblob.exceptions import NotTranslated

#import babelquery.abstr as ba
#import babelquery.babelquery

#key = 
allowable = [("着", "AS"), ("把", "BA"), ("的", "DEC"), ("的", "DEG"), ("得", "DER"), ("地", "DEV"), ("等等", "ETC"), ("被", "LB"), ("里", "LC"), ("个", "M"), ("所", "MSP"), ("目前", "NT"), ("被", "SB"), ("是", "VC"), ("有", "VE")]

authenticator = IAMAuthenticator() # Get your own key!

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')


def translate(word,pos,key,precision): 
    ret = []
    dt = retrieve(word)
    if dt!=None:
        ret.extend(dt.chinese)
        if dt.chinese == [" [English letter names are called as in English, no other standard Mandarin name exists]"]:
            ret = []
    if precision or dt == None or ret == []:
        translation = language_translator.translate(text=word, model_id='en-zh').get_result()["translations"]
        ret.extend([x["translation"] for x in translation])
        #bn = ba.getRelatedWords(word, pos, key)
        #print(bn)
        #if bn!=None:
        #    ret.extend(bn)
    ret = list(dict.fromkeys(ret))
    return ret

#print(translate("test", None,key, False))


def transsent(sentence, extra):
    if len(sentence) <= 2:
        return sentence
        pass
    with StanfordCoreNLP(r"C:\Users\lge.DESKTOP-NNQ148M\programming\srs\use\stanford-corenlp-full-2018-10-05", lang="en", memory="6g") as en_tagger:
        en_postags = en_tagger.pos_tag(sentence)
    
    print(en_postags)
    for x in range(0, len(en_postags) - 1):
        if en_postags[x][0] not in [",", ".", "(", ")", "<", ">", "!", "?", "\'", "\""]:
            pos = quickPosMap(en_postags[x][1])
            tr = translate(en_postags[x][0], pos, key, False)
            if tr!=[]:
                if tr[0] == " [English letter names are called as in English, no other standard Mandarin name exists]":
                    tr[0] = en_postags[x][0]
            en_postags[x]= (tr,en_postags[x][1])

    zh_req = castPos(en_postags)
    if (".", "PU") in zh_req:
        zh_req.remove((".", "PU"))
    # Ordering
    if extra:
        while True:
            zh_postags = pos_creator.pos_create(("*START*", "*START*"), zh_req, allowable)
            if zh_postags != "Retry":
                break
    elif not extra:
        while True:
            zh_postags = pos_creator.pos_create(("*START*", "*START*"), zh_req, None)
            if zh_postags != "Retry":
                break
    
    final_ret = ""
    for x in zh_postags:
        if x[0] != "*START*":
            if x[0] != []:
                final_ret += x[0][0]
    return final_ret
print(transsent("This is a test.",False))