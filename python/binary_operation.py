b1=input() #getting inputs
b2=input()
op=input()
res=[]
for i in range(len(b1)): #looping through length of b1
    bit1 = int(b1[i])
    bit2 = int(b2[i])
    if(op == 'AND'): #checks for AND
        res.append(str(bit1 & bit2))
    elif(op == 'OR'):
        res.append(str(bit1 | bit2))
    else:
        res.append(str(bit1 ^ bit2)) #appends str of the result operation
print("".join(res)) #prints as a string