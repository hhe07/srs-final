from stanfordcorenlp import StanfordCoreNLP
def proc(line, lang, dr):
    with StanfordCoreNLP(dr,lang = lang,memory = "6g") as tagger:
        return tagger.pos_tag(line)