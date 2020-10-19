def good_triplets (arr, n):
    ko=[]
    lk={}
    for i in range(0,n):
        if lk.get(int(arr[i])) is None:
            lk[int(arr[i])]=1
            ko.append(int(arr[i]))
        else:
            lk[int(arr[i])]=lk[int(arr[i])]+1
    
    m=0
    n=len(ko)
    
    for y in range(0,n):
        for z in range(y+1,n):
            l=ko[y]+ko[z]
            for a in range(z+1,n):
                l+=ko[a]
                ck=0
                if l%ko[y]==0:
                    ck+=1
                if l%ko[z]==0:
                    ck+=1
                if l%ko[a]==0:
                    ck+=1
                if ck==1:
                    m+=int(lk[ko[y]]*lk[ko[z]]*lk[ko[a]])
    
    for i in range(0,n):
        if lk[ko[i]]<2:
            continue
        for j in range(0,n):
            if i==j:
                continue
            l=ko[i]*2+ko[j]
            if l%ko[i]!=0 and l%ko[j]==0:
                m+=int(((lk[ko[i]]*(lk[ko[i]]-1))/2)*lk[ko[j]])
    
    return m*6
            
    
n = int(input())
arr = []
for i in range(n) : 
    x = input()
    arr.append(x)

out_ = good_triplets(arr, n)
print (out_)
