#Linear Search in python
val=int(input()) 
l=[12,33,42,54,64,98,42,34,42]
flag=False
for i in range(0,len(l)):
    if(val==l[i]):
        flag=True #10
        print(i)

if(flag==False):
    print("Element not found")