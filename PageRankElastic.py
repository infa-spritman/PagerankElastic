# Created by Sushant

from collections import defaultdict
from sets import Set
import operator
from math import log

# Code for Inlinks File

f = open('linkgraph_WithoutQuery.txt', 'r')
l = f.readlines()

# print l.__len__()

# data Structures:
# M is the dictionary containing the docID as the key and value as the inlinks to that ID
# L is the dictionary where docID as the key and value is number of outlinks for given DOCID
# PR is dictionary containing pagerank for a specific page
# newPR is a dictionary used as temp variable for pagerank
# P is the set of all pages
# S is the set of sink nodes, i.e., pages that have no out links
# perplexity is the list of all perplexity values used to calculate convergence

M = {}
L = {}
PR = {}
newPR = {}
P = Set()
S = Set()
perplexityList  =[]

# Function Def

def getPValue():
    entropy =0.0
    for pg in PR.values():
        entropy += pg*log(pg,2)

    return 2**(-1.0*entropy)

def isConverged(count):
    pValue  = getPValue()
    print str(count+1) + " " + str(pValue)
    perplexityList.append(pValue)
    if len(perplexityList)>4:
        if((int(perplexityList[count]))==(int(perplexityList[count-1]))==(int(perplexityList[count-2]))==(int(perplexityList[count-3]))):

            return True
        else:
            return False

    else:
        return False

lnumb  = 1
# Intialising M dictionary with given file
for line in l:
    try:
        lineSP = line.split()
        lnumb +=1
        if len(lineSP) > 0:
            M[lineSP[0]] = Set(lineSP[1:])
            # M[line[0]] = line[1:]
            P.update(lineSP)
    except Exception, e:
        print e,lnumb

# print M.__len__()
# print P.__len__()
# print L.__len__()

#print M['http://suzy123.com']
#Intialising all P with outlinks count

# total number of Pages
N = float(len(P))

# d is the PageRank damping/teleportation factor; use d = 0.85 as is typical
d = 0.85

for p in P:
    PR[p] = 1.0 / N  # initial value
    L[p] = 0.0

# Updating L with outlinks count
for inlinks in M.values():
    for link in inlinks:
        L[link] += 1.0


# Updating S with sink nodes; i.e L[link] = 0
for link, outlink_count in L.items():
    if outlink_count == 0.0:
        S.add(link)


count = 0

while not(isConverged(count)):
    # if j > 100:
    #     break
    sinkPR = 0.0
    for p in S:
        sinkPR += PR[p]

    for p in P:
        newPR[p] = (1.0 - d) / N
        newPR[p] += (d * sinkPR) / N
        if p in M:
            for q in M[p]:
                newPR[p] += (d * PR[q]) / L[q]

    for p in P:
        PR[p] = newPR[p]

    count += 1

sortedPR = sorted(PR.iteritems(), key=operator.itemgetter(1), reverse=True)

i = 1

# for link,score in sortedPR:
#     if i>1000:
#         break
#     print str(i) + ". " + link + str(" : ") + str(score)
#     i += 1

for j in range(500):
    print sortedPR[j]

f.close()