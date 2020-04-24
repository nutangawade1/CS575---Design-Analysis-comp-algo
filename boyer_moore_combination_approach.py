

def findPatternMatch(pattern, text):

    patternLen = len(pattern)
    if (patternLen==0):
        print("Please enter valid pattern")
        return;
      
    #print("patternLen",patternLen)
    textLen = len(text)
    #print("textLen",textLen)
    if (textLen==0):
        print("Please enter valid Text")
        return;

    shiftTable = calculateShiftUsingBadChar(pattern, patternLen)
    print ("BadCharShiftTable",shiftTable)
    borderPos = [0] * (patternLen + 1)  
    # initialize all occurrence of shift to 0 
    shiftGood = [0] * (patternLen + 1) 
  
    createGoodSuffixTable(shiftGood, borderPos, pattern, patternLen)
    #print("borderPos",borderPos)
    #print("shiftGood1",shiftGood) 
    createGoodSuffixTable_case2(shiftGood, borderPos, pattern, patternLen) 
    print("GoodSuffixShiftArray",shiftGood)

    loopRange= textLen - patternLen
    matchIndex=[]
    badCharSkip=0
    i=0
    match_found=0
    while (i <= loopRange):
    #for i in range(forLoopRange1):
        print("i : ",i)
        badCharSkip = 0
        goodSuffixSkip=0
        match_count=0 

        for j in reversed(range(patternLen)):
            if j>=0:           
                if (pattern[j] != text[i+j]): 
                    #print ("j",j)
                    key=text[i+j]
                    skips=0
                    for hashKey,value in shiftTable.items():
                        if key==hashKey:
                            skips=value
                            badCharSkip=skips
                            #print ("badCharSkip: ",badCharSkip)
                            break                   
                    if skips ==0:
                        if match_count>0:
                            badCharSkip=j+1
                            #print ("badCharSkip: ",badCharSkip)  
                        else:    
                            badCharSkip= patternLen
                            #print ("badCharSkip: ",badCharSkip)  
                        
                    print ("badCharSkip: ",badCharSkip)
                    goodSuffixSkip = shiftGood[j+1]
                    print ("goodSuffixSkip: ",goodSuffixSkip)
                    i += max(badCharSkip,goodSuffixSkip) 
                    #print("i",i)     
                    break
                else:
                    match_count += 1
                    if (match_count==patternLen):
                        match_found=1
                        matchIndex.append(i)
                        #i += 1   

        if (match_found == 1):
            #print ("i",i)
            #print ("j",j)
            match_found=0
            if ((i+patternLen) < textLen):
                key=text[i+patternLen]
                skips=0
                for hashKey,value in shiftTable.items():
                    if key==hashKey:
                        skips=value
                        badCharSkip=skips
                        #print ("badCharSkip: ",badCharSkip)
                        break                   
                if skips ==0:
                    badCharSkip=patternLen+1
            else:
                badCharSkip=1
            print ("badCharSkip: ",badCharSkip) 
            goodSuffixSkip = shiftGood[0]
            print ("goodSuffixSkip: ",goodSuffixSkip) 
            i += max(badCharSkip,goodSuffixSkip)     
            #print("i",i)

    if len(matchIndex)==0:
        print("Pattern does not match")
    else:
        for x in range(len(matchIndex)):
                print("Pattern matches at :" , matchIndex[x])    
            #break
 
        
#Preprocessing function which generates bad character table to calculate shifts    
def calculateShiftUsingBadChar(pattern, patternLen):
    shiftTable={}
    shift=patternLen
    for char in range(patternLen):
        shift = patternLen - char - 1               
        hashKey=pattern[char]
        shiftTable[hashKey]=max(1,shift);

    #print(shiftTable)        
    return shiftTable


def createGoodSuffixTable(shiftGood, borderPos, pattern, patternLen): 
    i = patternLen 
    j = patternLen + 1
    borderPos[i] = j   
    while i > 0: 
        while j <= patternLen and pattern[i - 1] != pattern[j - 1]: 
            if shiftGood[j] == 0: 
                shiftGood[j] = j - i 
            j = borderPos[j] 
        i -= 1
        j -= 1
        borderPos[i] = j 
  
def createGoodSuffixTable_case2(shiftGood, borderPos, pattern, patternLen): 
    j = borderPos[0] 
    for i in range(patternLen + 1): 
        if shiftGood[i] == 0: 
            shiftGood[i] = j 
        if i == j: 
            j = borderPos[j] 
            

print("please enter the Text to search the pattern")
text=str(input())
print("please enter the Pattern to search")
pattern=str(input())

findPatternMatch(pattern, text)
