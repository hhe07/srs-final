import pickle
import markov.two_state as mt
zh_model= mt.twoState("zh_mm")

zh = pickle.load(open("zh.p", "rb"))
zhpos = []

for x in range(0, len(zh) - 1):
    zh[x] = [y for y in zh[x] if y != ("（", "PU")]
    zh[x] = [y for y in zh[x] if y != ("）", "PU")]
    zh[x] = [y for y in zh[x] if y != ("(", "PU")]
    zh[x] = [y for y in zh[x] if y != (")", "PU")]
for x in zh:
    if x[1][1]=="PU":
        print(x[0],x[1])

for y in zh:
    app = []
    for sent in y:
        if sent == "*START*":
            app.append("*START*")
        else:
            app.append(sent[1])
    zhpos.append(app)

for sent in zhpos:
    for x in range(0, len(sent) - 1):
        curr = sent[x]
        nxt = sent[x + 1]
        zh_model.updateFinalStates(curr, nxt)
zh_model.calcProbs()

zh_model.preserve()