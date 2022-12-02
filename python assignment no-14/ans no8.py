# write a python script to print distinct elements along with their frequencies of occurence in the list.

val=eval(input("enter list"))
freq={}
for e in val:
    if e in freq:
        freq[e]+=1
    else:
        freq[e]=1
        
print(freq)



   
    
     

