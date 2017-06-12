from CountingVotes import XYSwingCount

import csv

def createDict1():
    mydict = dict()

    with open('main1.csv', mode='r') as infile:
        reader = csv.reader(infile)
        with open('coors_new.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            mydict = {rows[0]: rows[1] for rows in reader}
            for rows in reader:
                key = int(rows[0])
                value = int(rows[1])
                mydict.setdefault(key, []).append(value)
    #print("mydict",mydict)

    #print("\nAm running for all 10000 nodes")
    print("Runnig without Influential Nodes")
    X1, Y1 = XYSwingCount(mydict)
    if X1 > Y1:
        # global diff
        diff = X1 - Y1
        res = 'X'
        #inflist.append((0, -diff))

        print("\n....X wins Y by ....", (X1 - Y1), "votes.....!!!")
    else:
        # global diff
        diff = Y1 - X1
        res = 'Y'
        #inflist.append((0, diff))

        print("\n....Y wins X by ....", (Y1 - X1), "votes.....!!!")

    return mydict,diff,res