

def findPatternMatch(pattern, text):

    patternLen = len(pattern)
    print("patternLen",patternLen)
    textLen = len(text)
    #print("textLen",textLen)
    shiftTable = calculateShiftUsingBadChar(pattern, patternLen)
    print (shiftTable)
    loopRange= textLen - patternLen
    #print ("forLoopRange1",forLoopRange1)
    matchIndex=[]
    numOfSkips=0
    i=0
    match_found=0
    #while (process_done==0):
    while (i <= loopRange):
    #for i in range(forLoopRange1):
        #i=i+numOfSkips
        print("i : ",i)
        #print ("numOfSkips",numOfSkips)
        numOfSkips = 0
        match_count=0        #if  i<forLoopRange1:
        for j in reversed(range(patternLen)):
            if j>=0:           
                #print("j : ",j)
                if (pattern[j] != text[i+j]):
                    #print ("pattern[j]: ",pattern[j])
                    #print ("text[i+j]: ",text[i+j])  
                    key=text[i+j]

                    skips=0
                    for hashKey,value in shiftTable.items():
                        if key==hashKey:
                            skips=value
                            numOfSkips=skips
                            #print ("key: ",key)
                            #print ("value: ",value)
                            print ("numOFSkips: ",numOfSkips)
                            break    
                
                    if skips ==0:
                        #print("Key: ",key)
                        if match_count>0:
                            numOfSkips=j+1
                        else:    
                            numOfSkips= patternLen
                        print ("numOFSkips: ",numOfSkips)
        
                    i=i+numOfSkips       
                    break
                else:
                    match_count += 1
                    if (match_count==patternLen):
                        match_found=1
                        matchIndex.append(i)
                        #i += 1   
        
        if (match_found == 1):
            match_found=0
            if ((i+patternLen) < textLen):
                key=text[i+patternLen]
                skips=0
                for hashKey,value in shiftTable.items():
                    if key==hashKey:
                        skips=value
                        numOfSkips=skips
                        break                   
                if skips ==0:
                    numOfSkips=patternLen+1
            else:
                numOfSkips=1
            print ("numOfSkips2: ",numOfSkips)             
            i += numOfSkips     
            print("i",i)

    if len(matchIndex)==0:
        print("Pattern does not match")
    else:
        for x in range(len(matchIndex)):
                print("Pattern matches at :" , matchIndex[x])
            #break
 
        
#Preprocessing function which generates bad character table to calculate shifts    
def calculateShiftUsingBadChar(pattern, patternLen):
    badCharShiftTable= [-1]*256;
    shiftTable={}
    shift=patternLen
    for char in range(patternLen):
        #print("value of char", pattern[char])
        #print ("value of index", char)
        shift = patternLen - char - 1               
        hashKey=pattern[char]
        shiftTable[hashKey]=max(1,shift);

    print(shiftTable)        
    return shiftTable


#text="THIS IS A TEST A TEST A TEST"
#pattern = "TEST"
#text="THIS IS A TEST TEXT"
#pattern = "TEST"
#text="THIS IS A PEST TEXT"
#pattern = "TEST"
#text="THIS IS A TPST TEXT"
#pattern = "TEST"
#ext="ABABCABABABCABY"
#pattern = "ABCABY"
#text = "AABAACAADAABAABA"
#pattern = "AABA"

print("please enter the Text to search the pattern")
text=str(input())
print("please enter the Pattern to search")
pattern=str(input())

findPatternMatch(pattern, text)
