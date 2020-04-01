# Used to find test cases for the "in common"sense finder
import babelquery as bq
r1 = open("1.txt","w",encoding = "utf-8")
r2 = open("2.txt","w",encoding = "utf-8")
a = bq.getEdges("bn:00022678n",key)
for x in a:
    r1.write(str(x["target"])+"\n")
b = bq.getEdges("bn:00067717n",key)
for y in b:
    r2.write(str(y["target"]+"\n"))
r1.close()
r2.close()

bq.getEdges("bn:00022678n",key)
