
def XYSwingCountInf(dataDict , infNode ):
    #print(infNode)
    #print("\ndataDict",dataDict)
    totalX = totalY = totalSwing = X = Y = swingPredX = swingPredY = 0
    dictForSwing = dict()
    swingValues = []
    for node in dataDict:
        #check for NodeIds
        lastDigit = node%10
        if node == infNode:
            #print("\n Mine sam eas inf")
            totalY = totalY + 1
            continue
        elif (lastDigit == 0) or (lastDigit == 1) or (lastDigit == 2) or (lastDigit == 3):
            totalX = totalX + 1

        elif (lastDigit == 4) or (lastDigit == 5) or (lastDigit ==6) or (lastDigit ==7):
            totalY = totalY + 1

        else:
            totalSwing = totalSwing + 1
            swingValues = dataDict[node]
            dictForSwing[node] = swingValues
    #print("\n totalSwing",totalSwing)
    #print("\n totalx",totalX)
    #print("\ntotalY",totalY)
    #print(dictForSwing)
    swingPredX, swingPredY = thoughtProcess(dictForSwing,infNode)
    X = swingPredX + totalX
    Y = swingPredY + totalY

    return X,Y


alterGlobalVar = 'X'
predDict = dict()
predDict1 = dict()



def thoughtProcess(dictForSwing,infNode):

    finalPredX = finalPredY = 0
    #predDict = dict()
    i = 1
    while(i<7):


        ax = ay = asw =0

        frndValues = []
        #global alterGlobalVar
        #alterGlobalVar = 'X'

    #check for frnds


        for node in dictForSwing:
            predSwingAsX = predSwingAsY = predSwingAsSwing = 0

            frndValues = dictForSwing[node]
            for values in frndValues:
                lastDigit = values%10
                if (values == infNode):
                    predSwingAsY = predSwingAsY + 1
                    #print("\nnode-",node,"value",values)
                    continue
                elif (lastDigit == 0) or (lastDigit == 1) or (lastDigit == 2) or (lastDigit == 3):
                    predSwingAsX = predSwingAsX + 1
                elif (lastDigit == 4) or (lastDigit == 5) or (lastDigit == 6) or (lastDigit == 7):
                    predSwingAsY = predSwingAsY + 1
                else:
                    predSwingAsSwing = predSwingAsSwing +1
                    #print("\nS", predSwingAsSwing)

            if predSwingAsX > predSwingAsY:
                assign = 'X'
                ax = ax+1

            elif predSwingAsY > predSwingAsX:
                assign = 'Y'
                ay = ay+1
            elif predSwingAsX == predSwingAsY:
            #assign using alternating global varibale
                global alterGlobalVar
                if alterGlobalVar == 'X':
                    assign = 'X'
                    ax = ax+1
                    #print("\nflag",assign)
                    alterGlobalVar = 'Y'
                elif alterGlobalVar == 'Y':
                    assign = 'Y'
                    ay = ay+1
                    alterGlobalVar = 'X'
                    #print("\nflag", assign)
                global predDict1
                predDict1[node] = assign

            else:
                assign = 'S'
                asw = asw+1
            global predDict
            predDict[node]=assign

            #print("\nGlobal Var", alterGlobalVar)

        #print("\nDictPredicted", predDict)
        #print("\n no of x",totalX)
        #print("\n no of y",)
        #print("\n swingX",(ax))
        #print("\nswingY",(ay))
        #print("\nlen",len(dictForSwing))
        i = i + 1
        #print("\npreddict1",predDict1)


    #print("\nFinal",predDict)

    for nodes, value in predDict.items():
        if value == 'X':
            finalPredX = finalPredX + 1
        elif value == 'Y':
            finalPredY = finalPredY + 1

    #print("\nFinalPredX",finalPredX)
    #print("\nFinalPredY",finalPredY)
    return finalPredX , finalPredY


