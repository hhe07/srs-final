# Includes test calls :)
import pickle
key = "" # PASTE YOUR KEY HERE!
import babelquery as bq


pickle.dump(bq.getSynsetIds("apple","EN",None,"NOUN",key),open("getSynsetIds.p","wb"))

pickle.dump(bq.getSynset("bn:14792761n","ZH",key),open("getSynset.p","wb"))

pickle.dump(bq.getSenses("apple","EN","ZH","NOUN",key),open("getSenses.p","wb"))

# Wiki/Wikiquote v
pickle.dump(bq.getSynsetIdsFromResourceId("apple","EN","ZH","NOUN","WIKI",None,key),open("wikiSynset.p","wb"))
# WordNet/Other sources v
pickle.dump(bq.getSynsetIdsFromResourceId("wn:02398357v",None,"ZH",None,"WN","WN_21",key),open("wnSynset.p","wb"))

pickle.dump(bq.getEdges("bn:00005054n",key),open("edges.p","wb")) # Extremely long terminal printout :)