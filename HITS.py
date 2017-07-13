# Created by Sushant

from sets import Set
import random
from ordered_set import OrderedSet
import operator
from math import log
from math import pow
from math import sqrt
from elasticsearch import Elasticsearch

# Root Set
R = OrderedSet()

# Base Set
S = Set()

InlinkGraph = {}
OutlinkGraph = {}

# Hub and Authority

A = {}
H = {}

perplexityA = []
perplexityH = []
####################################################################

def getAValue():
    entropy =0.0
    for pg in A.values():
        if pg!=0.0:
            entropy += pg*log(pg,2)

    return 2**(-1.0*entropy)

def getHValue():
    entropy =0.0
    for pg in H.values():
        if pg != 0.0:
            entropy += pg*log(pg,2)

    return 2**(-1.0*entropy)

def isConverged(count):
    aValue  = getAValue()
    hValue = getHValue()
    #print str(count+1) + " " + str(pValue)
    perplexityA.append(aValue)
    perplexityH.append(hValue)
    if len(perplexityA)>4 and len(perplexityH)>4:
        if(((int(perplexityA[count]))==(int(perplexityA[count-1]))==(int(perplexityA[count-2]))==(int(perplexityA[count-3]))) and
               ((int(perplexityH[count])) == (int(perplexityH[count - 1])) == (int(perplexityH[count - 2])) == (
               int(perplexityH[count - 3])))):
            print str(count+1) + " " + str(aValue) + " " + str(hValue)
            return True
        else:
            return False

    else:
        return False


#####################################################################



##Loading Inlink Graph
f = open('Inlinkgraph_deli.txt', 'r')
l = f.readlines()

lineNumb = 1
for line in l:
    try:
        lineSP = line.strip('\n').split('<:>')
        lineSP = [y for y in lineSP if y != '']
        InlinkGraph[lineSP[0]] = Set(lineSP[1:])
        lineNumb += 1
    except Exception, e:
        print e, lineNumb

f.close()

# Loading Outlink Graph
f = open('out-linkgraph_deli.txt', 'r')
l = f.readlines()

for line in l:
    try:
        lineSP = line.strip('\n').split('<:>')
        lineSP = [y for y in lineSP if y != '']
        OutlinkGraph[lineSP[0]] = Set(lineSP[1:])

    except Exception, e:
        print e

f.close()

# Loading Root Set

f = open('root-set.txt', 'r')
l = f.readlines()

for line in l:
    try:
        R.add(line.strip())

    except Exception, e:
        print e + "ou"

f.close()

# print len(InlinkGraph)
# print len(OutlinkGraph)
# print len(R)

d = 200

# Filling S set with R values
S.update(R)

# Expanding Base Set
f = open('root-set.txt', 'r')
l = f.readlines()

ln = 1

for line in l:
    try:
        p = line.strip()
        if len(S) > 10000:
            break
        if p in OutlinkGraph:
            S.update(OutlinkGraph[p])

        if p in InlinkGraph:
            inlink_set = InlinkGraph[p]
            if len(inlink_set) <= d:
                S.update(inlink_set)
            else:
                S.update(random.sample(inlink_set, d))


    except Exception, e:
        print e + "ou"

f.close()

# for p in R:
#     if len(S) > 10000:
#         break
#     if p in OutlinkGraph:
#         S.update(OutlinkGraph[p])
#
#     if p in InlinkGraph:
#         inlink_set = InlinkGraph[p]
#         if len(inlink_set) <= d:
#             S.update(inlink_set)
#         else:
#             S.update(random.sample(inlink_set, d))

print len(S)

for p in S:
    A[p] = 1.0
    H[p] = 1.0

count = 0

while not (isConverged(count)):
    if count>100:
        break
    norm = 0.0
    for p in S:
        A[p] = 0.0
        if p in InlinkGraph:
            for q in InlinkGraph[p]:
                if q in H:
                    A[p] += float(H[q])
        norm += float(pow(A[p], 2.0))

    norm = float(sqrt(norm))

    for p in S:
        A[p] = float(A[p]) / norm

    ###############3
    norm = 0.0
    for p in S:
        H[p] = 0.0
        if p in OutlinkGraph:
            for r in OutlinkGraph[p]:
                if r in A:
                    H[p] += float(A[r])
        norm += float(pow(H[p], 2.0))

    norm = float(sqrt(norm))

    for p in S:
        H[p] = float(H[p]) / norm

    count += 1

sortedA = sorted(A.iteritems(), key=operator.itemgetter(1), reverse=True)
sortedH = sorted(H.iteritems(), key=operator.itemgetter(1), reverse=True)

print "Authority Links"

for j in range(500):
    print sortedA[j]

#Printing Hub Links

print "Hub Links"

for j in range(500):
    print sortedH[j]
