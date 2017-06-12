from CountingVotesWithInf import XYSwingCountInf
from CountingVotesWithInf import thoughtProcess
from excel import createDict1
from CountingVotes import XYSwingCount
import networkx as nx
import sys
import csv

import matplotlib.pyplot as plt
fd = open('out.txt','w')
old_stdout = sys.stdout




def createDict(inputFile):


    edges = []

    # Open the input file for reading

    with open(inputFile, mode='r') as fileRead:
        # read the data into dict
        dictAsNodeFrnd = dict()
        dictAsNodeValue = dict()

        for eachRow in fileRead:
            # Row has data separated by a space, Split the data by space
            rowData = eachRow.split()
            dictAsNodeFrnd.setdefault((int(rowData[0])), []).append((int(rowData[1])))
            dictAsNodeValue[(int(rowData[0]))] = (int(rowData[1]))

            edges.append((int(rowData[0]), int(rowData[1])))

    mydict = dict()
    mydict,diff,res = createDict1()
    #print("diff",diff)


    edges1 = []
    for key in mydict:
        values = mydict[key]
        for eachVal in values:
            edges1.append((key,eachVal))
    #print("edges1",edges1)


    #getting the influential nodes

    infList = getInfNodeList(edges1)
    outWithInf = []
    i=0
    a=0
    infdict = dict()

    outWithInf.append((0, -diff))
    infdict['0'] = (diff, res)


    while i < 9:
        XInf = YInf = a = 0
        XInf, YInf = XYSwingCountInf(dictAsNodeFrnd, infList[i])
        #print("Xinf", XInf, YInf)

        print("\nRunning for",i+1,"Influetial node...!")
        a = XInf - YInf
        if a > 0:
            diff = diff - a
            if diff < 0:
                print("\nY wins by", -diff, "votes")
                outWithInf.append((i + 1, -diff))
                infdict['i'] = (diff, 'X')
            else:
                print("\nX wins by", diff, "votes")
                outWithInf.append((i + 1, -diff))
                infdict['i'] = (diff, 'X')
        else:
            diff = diff - a
            print("\nY wins by", -diff, "votes")
            outWithInf.append((i + 1, -diff))
            infdict['i'] = (diff, 'Y')

        i = i + 1
    print("\ninflist", outWithInf)

    with open('output.csv', 'w') as outcsv:
        writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['No of Votes', 'By How Many'])
        for item in outWithInf:
            # Write item to outcsv
            writer.writerow([item[0], item[1]])


def getInfNodeList(edges):
    GA = nx.from_edgelist(edges)
    #print(nx.info(GA))

    degree_central = nx.degree_centrality(GA)
    degreesort = sorted(degree_central.items(), key=lambda x: x[1], reverse=True)
    degreesort1 = sorted(GA.degree().items(), key=lambda x: x[1], reverse=True)
    #print(degreesort[:9])
    #print(degreesort1[:9])


    infNodeList = []
    degreeList = []
    listDict = dict()
    i = 0
    while i < 9:
        #print(degreesort1[i][0])
        #infNodeList.append(degreesort1[i][0])
        #degreeList.append(degreesort1[i][1])
        listDict.setdefault(degreesort1[i][1], []).append(degreesort1[i][0])
        i = i + 1

    #print(infNodeList)
    #print(degreeList)
    #print(listDict)

    infList = []
    for node in listDict:
        values = listDict[node]
        values.sort()
        for value in values:
            infList.append(value)

    #print(infList)
    #print(type(degreesort))
    #highest_degree = [node[0] for node in degreesort[:2000]]
    #sub = GA.subgraph(highest_degree)
    return infList

def main():
    #get the input file
    #inputFile = "C:/Users/sreejay/Desktop/problem/problem/g1_edgelist.txt"
    inputFile = sys.argv[1]
    Graph = createDict(inputFile)


if __name__ == "__main__":
    main()