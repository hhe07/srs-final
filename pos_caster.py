def castPos(lofpos):
    casts = {"CC": ["CC"], "CD": ["CD"], "DT": ["DT"], "EX": [None], "FW": ["FW"], "IN": ["P", "CS"],
    "JJ": ["VA"], "JJS": ["VA"], "LS": [None], "MD": [None], "NN": ["NN"], "NNP": ["NN"],"NNS":["NN"], "NNPS": ["NN"], "PDT": [None],
    "POS": ["VE"], "PRP": ["PN"], "PP$": ["PN"], "RB": ["AD"], "RBR": ["AD"], "RBS": ["AD"], "RP": ["MSP", "SP"], "SYM": ["X"], "TO": [None],
    "UH": ["IJ"], "VB": ["VV"], "VBD": ["VV"], "VBG":["VV"], "VBN": ["VV"], "VBP": ["VV"], "VBZ": ["VV"], "WDT": ["DT"], "WP": ["PN"], "WP$": ["PN"], "WRB": ["AD"]}
    
    ret = []
    for x in range(0, len(lofpos)):
        t = lofpos[x]
        nxt = None
        if x <= len(lofpos) - 2:
            nxt = lofpos[x+1][1]
        if t[1] in casts:
            add = casts[t[1]][0]
            expt = False
            if t == "NNP":
                if nxt == "CD":
                    ret.append(("OD",None))
                    expt = True
            if add!=None and expt==False:
                ret.append((t[0],add))
        if t[1] in [",", ".", "(", ")", "<", ">", "!", "?", "\'", "\""]:
            ret.append((t[1],'PU'))
    return ret

#print(castPos(["NNP","CD","DT","NNS","VBP","NNS","CC","JJ","NNS","IN","DT","NNP","."]))

def quickPosMap(treebank):
    # Returns a UniversalPOS
    maps = {"CC": ["NOUN"], "CD": ["NOUN"], "DT": ["NOUN"], "EX": ["NOUN"], "FW": [None], "IN": ["ADJ"], "JJ": ["ADJ"], "JJR": ["ADJ"], "JJS": ["ADJ"], "LS": [None], "MD": ["VERB"], "NN": ["NOUN"], "NNS": ["NOUN"], "NNP": ["NOUN"], "PDT": ["NOUN"]
    , "POS": [None], "PRP": ["NOUN"], "PRP$": ["NOUN"], "RB": ["ADV"], "RBR": ["ADV"], "RBS": ["ADV"], "RP": ["VERB"], "SYM": [None], "TO": ["VERB"], "UH": ["NOUN"], "VB": ["VERB"], "VBD": ["VERB"], "VBG": ["VERB"], "VBN": ["VERB"], "VBP": ["VERB"], "VBZ": ["VERB"], "WDT": ["NOUN"], "WP": ["NOUN"], "WP$": ["NOUN"], "WRB": ["ADV"]}
    if treebank in maps.keys():
        return maps[treebank]
    else:
        return None
