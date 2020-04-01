# Includes test calls :)
key = "" # PASTE YOUR KEY HERE!
import babelquery as bq
print(bq.getVersion(key)) # Should return something simple even w/o key, see https://babelnet.org/guide for about what to expect.

print(bq.getSynsetIds("apple","EN",None,"NOUN",key)) # See website ^ for sample returns of this and all other calls

print(bq.getSynset("bn:14792761n","ZH",key))

print(bq.getSenses("apple","EN","ZH","NOUN",key))

# Wiki/Wikiquote v
print(bq.getSynsetIdsFromResourceId("apple","EN","ZH","NOUN","WIKI",None,key))
# WordNet/Other sources v
print(bq.getSynsetIdsFromResourceId("wn:02398357v",None,"ZH",None,"WN","WN_21",key))

print(bq.getEdges("bn:00005054n",key)) # Extremely long terminal printout :)