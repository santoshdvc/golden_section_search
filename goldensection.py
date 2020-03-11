from random import randint
def gs(a,n):
    r=0.618
    l=int(len(a)-1)
    flag=0
    st=0
    end=l
    md=0
    co=0
    i=0
    while(flag==0):
        if((end-st)<=1):
            break
        co=int(0.618*(end-st))
        md=co+st
        print(md,co,st,end)
        if(a[md]<n):
            st=md
        else:
            end=md
        print("iteration")
        if(a[st]==n):
            flag=1
        elif (a[end]==n):
            flag=1
        elif(a[st]>n or a[end]<n):
            flag=2
        i=i+1
    return flag
arr=[]
for i in range(0,1000000):
    arr.append(randint(0,200000))
arr.sort()
ar=set(arr)
arr=[]
arr=list(ar)
print(len(arr))
n=int(input("Enter a number btwn 0-200"))
fl=gs(arr,n)
if fl==0:
    print("not found")
elif fl==1:
    print("found")
elif fl==2:
    print("not found")
