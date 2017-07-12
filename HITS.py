# Created by Sushant

from sets import Set
import operator
from math import log
from elasticsearch import Elasticsearch

# Root Set
R = Set()

# Base Set
S = Set()

InlinkGraph = {}
OutlinkGraph = {}

f = open('Inlinkgraph_deli.txt', 'r')
l = f.readlines()

lineNumb = 1
for line in l:
    try:
        lineSP = line.split('<:>')
        InlinkGraph[lineSP[0]] = Set(lineSP[1:])
        if(len(InlinkGraph)!= lineNumb):
            print "Not equal" + str(lineNumb)
        lineNumb += 1
    except Exception, e:
        print e , lineNumb


f.close()

#Loading Outlink Graph
f = open('out-linkgraph_deli.txt', 'r')
l = f.readlines()

for line in l:
    try:
        lineSP = line.split('<:>')
        OutlinkGraph[lineSP[0]] = Set(lineSP[1:])

    except Exception, e:
        print e + "ou"

f.close()

#Loading Root Set

f = open('root-set.txt', 'r')
l = f.readlines()

for line in l:
    try:
        R.add(line)

    except Exception, e:
        print e + "ou"

f.close()

print len(InlinkGraph)
print len(OutlinkGraph)
print len(R)
