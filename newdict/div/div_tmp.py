last = "a"
        acount = 0
        l = []
        for t in self.terms:
            fl = t.english[0][0:1].lower()
            if fl=="a":
                acount+=1
            if fl==last:
                l.append(t)
            else:
                pickle.dump(l, open(last+".p","wb"))
                last = fl
                l = []
                l.append(t)
            # TODO: Line 30464 style extra information
            # TODO: Line 650 scenarios
        print(acount)