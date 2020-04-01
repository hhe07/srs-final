import pickle
from numpy.random import choice

def compareLists(l1, l2):
    # Returns True if l1 contains all elements of l2
    ret = []
    for x in l2:
        if x in l1 and l1.count(x) == l2.count(x):
            ret.append(True)
        if x in l1 and l1.count(x) != l2.count(x):
            ret.append(False)
        if x not in l1:
            ret.append(False)
    return sum(ret)==len(ret)
#print(compareLists(['DT', 'VV', 'DT', 'NN'],['*START*', 'VV']))
class linked:
    def __init__(self, data):
        self.data = data
        self.prob = 0
        self.count = 0
    def addProb(self, prob):
        self.prob = prob/self.count
    def addCount(self,count):
        self.count += count
    def resetProb(self):
        self.prob = 0
    def resetCount(self):
        self.count = 0

def getProbs(zh_mm, working_term, nextlist):
    nextlist = list(dict.fromkeys(nextlist))
    ret = {}
    p = zh_mm[working_term]
    for x in nextlist:
        if x in p.keys():
            ret[x] = p[x]["prob"]
    return ret

def recalProbs(d):
    totalprob = 0
    for k in d.keys():
        totalprob += d[k]
    for k in d.keys():
        d[k] /= totalprob
    return d

def pos_create(start_term, termlist, extras):
    if len(termlist) == 1:
        return termlist
    # Sample Inputs
    # extras: allowable = [("着","AS"),("把","BA"),("的","DEC"),("的","DEG"),("得","DER"),("地","DEV"),("等等","ETC"),("被","LB"),("里","LC"),("个","M"),("所","MSP"),("目前","NT"),("被","SB"),("是","VC"),("有","VE")]
    # termlist: [('This', 'DT'), ('is', 'VV'), ('an', 'DT'), ('test', 'NN'), ('.', 'PU')]
    zh_mm = pickle.load(open("zh_mm.p", "rb")) # Probability Model
    
    bar = len(termlist) + 10 # Maximum sentence length before retry
    orig_req_pos = [x[1] for x in termlist] # Original requirements for POS Tags

    termlist = [linked(x) for x in termlist]
    if extras!=None:
        termlist.extend([linked(x) for x in extras])

    ret = [linked(start_term)]
    cycle = 0
    while True:
        #print("CYCLE: {}".format(cycle))
        retPos = [x.data[1] for x in ret]
        if compareLists(retPos,orig_req_pos):
            #print(retPos)
            #print(orig_req_pos)
            ret = [x.data for x in ret]
            ret.append((".","PU"))
            
            return ret
            break
        
        if len(ret) >= bar:
            return "Retry"
            break
        
        working_term = ret[len(ret) - 1].data[1]

        
        termlist_pos = [x.data[1] for x in termlist]
        p = getProbs(zh_mm, working_term, termlist_pos)  # Returns a dictionary of the applicable probabilities
        p = recalProbs(p)

        #print([x.data[1] for x in termlist])
        #print(p)
        
        for x in range(0,len(termlist)-1):
            currPos = termlist[x].data[1]
            ct = termlist_pos.count(currPos)
            if currPos in p.keys():
                termlist[x].addCount(ct)
                termlist[x].addProb(p[currPos])
            else:
                termlist[x].addCount(1)
                termlist[x].addProb(0)
        if len(termlist) == 1:
            currPos = termlist[x].data[1]
            ct = termlist_pos.count(currPos)
            if currPos in p.keys():
                termlist[x].addCount(ct)
                termlist[x].addProb(p[currPos])
            else:
                termlist[x].addCount(1)
                termlist[x].addProb(0)
        probs = [x.prob for x in termlist]
        deviation = sum(probs)

        if sum(probs) == 0:
            return "Retry"
            break
        for x in range(0, len(probs) - 1):
            probs[x] = probs[x]/deviation


        c = choice(termlist, 1, p=probs).tolist()[0]
        ret.append(c)
        termlist.remove(c)
        for x in range(0, len(termlist) - 1):
            termlist[x].resetCount()
            termlist[x].resetProb()
        
        cycle+=1