import requests
import json

# Based off of https://babelnet.org/guide , the HTTP API
# The Python APIs for BabelNet are shafted, so HTTP it is.
# Register your own key to test things out.
def addTag(tagText,tagContent):
    queue = []
    if type(tagContent)==str:
        queue.append(tagContent)
    if type(tagContent)==list:
        queue = tagContent
    out = ""
    for t in queue:
        out+=tagText.format(t)
    return out

def getVersion(key):
    return json.loads(requests.get("https://babelnet.io/v5/getVersion?key={}".format(key)).text)


def getSynsetIds(lemma,searchLang,targetLang,pos,key):
    # Source doesn't matter, so not included
    c = "https://babelnet.io/v5/getSynsetIds?lemma={lemma}&searchLang={searchLang}&key={key}"
    if targetLang!=None:
        c+=addTag("&targetLang={}",targetLang)
    if pos!=None:
        c+=addTag("&pos={}",pos)
    return json.loads(requests.get(c.format(lemma = lemma, searchLang = searchLang, key = key)).text)


def getSynset(synsetId,targetLang,key):
    c = "https://babelnet.io/v5/getSynset?id={synsetId}&key={key}"
    if targetLang!=None:
        c+=addTag("&targetLang={}",targetLang)
    return json.loads(requests.get(c.format(synsetId = synsetId, key = key)).text)


def getSenses(lemma,searchLang,targetLang,pos,key):
    c = "https://babelnet.io/v5/getSenses?lemma={lemma}&searchLang={lang}&key={key}"
    if targetLang!=None:
        c+=addTag("&targetLang={}",targetLang)
    if pos!=None:
        c+=addTag("&pos={}",pos)
    return json.loads(requests.get(c.format(lemma = lemma, lang = searchLang, key = key)).text)


def getSynsetIdsFromResourceId(rid,searchLang,targetLang,pos,source,wnVersion,key):
    c = "https://babelnet.io/v5/getSynsetIdsFromResourceID?id={lemma}&source={source}&key={key}"
    if source=="WIKI" or source=="WIKIQU":
        if searchLang!=None:
            c+="&searchLang={searchLang}".format(searchLang = searchLang)
        if pos!=None:
            c+=addTag("&pos={}",pos)
    elif source=="WN":
        if wnVersion!=None: #Source must be WN
            c+="&wnVersion={wnVersion}".format(wnVersion = wnVersion)
    if targetLang!=None:
            c+=addTag("&targetLang={}",targetLang)
    return json.loads(requests.get(c.format(lemma = rid, source = source, key = key)).text)


def getEdges(rid,key):
    c = "https://babelnet.io/v5/getOutgoingEdges?id={synsetId}&key={key}"
    data = json.loads(requests.get(c.format(synsetId = rid, key = key)).text)
    ret = []
    for x in data:
        ret.append(x["target"])
    return ret


