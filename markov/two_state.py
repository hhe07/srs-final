# System for making simple, two-state probability models.
import pickle


def removeAllOccurances(l,element):
    return list(filter((element).__ne__,l))

class twoState:
    def __init__(self,name):
        # Transitions should be a list of Transition classes.
        self.name = name
        self.finalStates = {}

    def updateFinalStates(self,fr,to):
        if fr in self.finalStates.keys():
            if to in self.finalStates[fr].keys():
                self.finalStates[fr][to]["occurances"]+=1
            else:
                self.finalStates[fr][to] = {"occurances":1,"prob":None}
        else:
            self.finalStates[fr] = {to: {"occurances":1,"prob":None},"occurances":0}
        self.finalStates[fr]["occurances"]+=1
    def calcProbs(self):
        for fr in self.finalStates.keys():
            if fr!="occurances":
                for to in self.finalStates[fr].keys():
                    if to!="occurances":
                        occur = self.finalStates[fr][to]["occurances"]
                        self.finalStates[fr][to]["prob"] = occur / self.finalStates[fr]["occurances"]

    def preserve(self):
        # Creates a loadable file of the two_state
        pickle.dump(self.finalStates,open(self.name+".p","wb"))
    
    def filterLofels(self,key,lofels):
        # filter probabilities under key for list of elements
        ret = {}
        for x in self.finalStates[key]:
            if x in lofels:
                ret[x] = self.finalStates[key][x]
        return ret
            

#x = twoState("test")
#x.updateFinalStates("a","b")
#x.updateFinalStates("a","c")
#x.calcProbs()
#print(x.finalStates)
#print(x.filterLofels("a","c"))
