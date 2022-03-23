#count 1s in an array using binary search

arr=[0,0,0,0,1,1,1,1]

left=0;
right=len(arr)-1
index=-1
while(left<=right):
    mid=(left+right)//2;
    if(arr[mid]<1):
        left=mid+1
    elif(arr[mid]>1):
        right=mid-1
    else:
        if(mid==0 or arr[mid-1]!=1 ):
            index=mid
            break;
        else:
            right=mid-1

print(len(arr)-index)
    
    
