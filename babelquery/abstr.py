# Use getSynset for get translation
import babelquery.babelquery as bq
import hanzidentifier as hz

key = ""
def getRelatedWords(text,pos,key):
    # Attempts to get a related translated word
    senses = bq.getSenses(text, "EN", "ZH", None, key)
    if senses == {'message': 'Your key is not valid or the daily requests limit has been reached. Please visit http://babelnet.org.'}:
        return None
    related = []
    for x in senses:
        s = x["properties"]["synsetID"]
        if s["pos"]==pos:
            a = x["properties"]["simpleLemma"]
            b = x["properties"]["fullLemma"]
            if hz.identify(a)==hz.BOTH or hz.identify(a)==hz.SIMPLIFIED:
                related.append(a)
            if hz.identify(b)==hz.BOTH or hz.identify(b)==hz.SIMPLIFIED:
                related.append(b)
    related = list(dict.fromkeys(related))
    return related

#print(getRelatedWords("print","VERB",key)) # Still includes Japanese, non-simplified, fix later



def getRelatedByEdges(rid1,rid2,pos,limit,key):
    # Constantly yeets through edges until it finds something matching and immediately dies.
    if limit is None:
        limit = 2 # Probably self-destructive honestly
    score = 0 # Number of edges it has to go to to find something.
    common = []
    queue1 = [{"layer":0,"ids":[rid1]}]
    queue2 = [{"layer":0,"ids":[rid2]}]
    # Init the Queues
    for x in range (1,limit):
        queue1.append({"layer":x,"ids":[]})
        queue2.append({"layer":x,"ids":[]})
    while score<limit-1: # This is most definitely BAD
        #print(len(queue1[score]["ids"]))
        r1 = [bq.getEdges(x, key) for x in queue1[score]["ids"]]
        r1 = list(dict.fromkeys(r1[0]))
        r2 = [bq.getEdges(x, key) for x in queue2[score]["ids"]]
        r2 = list(dict.fromkeys(r2[0]))
        queue1[score+1]["ids"].extend(r1)
        queue2[score+1]["ids"].extend(r2)
        for x in queue1[score+1]["ids"]:
            for y in queue2[score+1]["ids"]:
                if x==y:
                    common.append(x)
        if len(common)!=0:
            return {"common":common,"score":score,"all":[queue1,queue2]}
            break
        score+=1
    return None
        


#print(getRelatedByEdges("bn:00022678n","bn:00067717n",None,3,key))