def inversionOfIntegers(intList):
    """
    intList is a list of integers,
    """
    result = []
    count = 0
    print ("intlist is "+str(intList))
    if len(intList) < 2:
        print ("returning intlist: "+str(intList))
        return (intList, 0);
    mid = int (len(intList)/2)
    B,X = inversionOfIntegers(intList[:mid])
    C,Y = inversionOfIntegers(intList[mid:])
    i = 0
    j = 0
    while i<len(B) and j<len(C):
        if B[i] > C[j]:
            result.append(C[j])
            count += len(B)-i
            j+=1
            
        else:
            result.append(B[i])
            i+=1
    print B,C
    result += B[i:]
    result += C[j:]
    print ("D is " + str(result) +"\n")
    return (result,count+X+Y)
        
#text = open('Integers.txt','r')
#list1 = text.readlines()
#intlist1 = [int(x) for x in list1] # important to get the answer right
list2 = [5,4,3,2,1,8,10,34,22]
l, c = inversionOfIntegers(list2)
print ("c eqauls " + str(c))
