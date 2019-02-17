def up_array(arr):
    l=len(arr)
    a=[]
    k=0
    b=0
    c=0
    v=0
    while l!=0:
        b=int(arr[k])*10**(l-1)
        l-=1
        k+=1
        c+=b
    if arr[-2]==10:
        c1=[c]
    else:
        c+=1
        c1=[c]
    while c>0:
        c1.append(c%10)
        c=c//10
    c1=c1[::-1]
    c2=c1[:-1]
    return(c2)
