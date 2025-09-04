w1=input("Enter the first word : ") #getting inputs
w2=input("Enter the second word : ")
if(len(w1)==len(w2)): #conditional statement to check if both are of equal length
    if(sorted(w1)==sorted(w2)): #checking if they are equal after sorting
        print("YES, its an Anagram!!") 
    else:
        print("NO, its not an Anagram!!")
else: 
    print("Not eligible for checking Anagram. Both words must be of same length..!!") # prints when length is not equal