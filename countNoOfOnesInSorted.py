l=[0,0,0,1,1,1,1,1]

for i in range(0,len(l)):
    if(l[i]==1):
        index=i    
        break;    

print(len(l)-index)