def binarySearch(li,val):
    left=0
    right=len(li)-1
    while(left<=right):
        mid=(left+right)//2  #NOTE: MID IS STORING THE INDICES
        if(li[mid]==val):
            return mid
        elif(val>li[mid]):
            left=mid+1
        elif(val<li[mid]):
            right=mid-1
    
    return "Element not found"




li=[20,30,40,50,60]
val=int(input())
res=binarySearch(li,val)
print(res);