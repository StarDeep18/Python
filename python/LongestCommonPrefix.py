n = int(input("Enter number of words : ")) #gets input for number of words
lis = [] 
i=0 
while(i<n): #loop to get inputs
    strs=input("Enter the words : ") 
    lis.append(strs) #appending the words to list (lis)
    i+=1 
def LongestCommonPrefix(lis): 
    if not lis: #checking if list is empty
        return ""
    lis.sort() #sorting the list
    first_str = lis[0] 
    last_str = lis[-1] 
    i=0
    while(i<len(first_str) and i<len(last_str) and first_str[i]==last_str[i]): #finding common starting char between first and last word in list.
        i+=1
    return first_str[:i]
print(LongestCommonPrefix(lis))