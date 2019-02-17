def up_array(arr):
    a=int(arr[-1])
    l=len(arr)
    c=0
    f1=0
    if 9>a>=0:
        a+=1
        a,arr[-1]=arr[-1],a
        if arr[-2]==10:
            arr[-2],c=c,arr[-2]
            e=int(arr[-3])+1
            arr[-3],e=e,arr[-3]
            return(arr)
            if arr[-3]==10:
                arr[-3],f1=f1,arr[-3]
                f=[1]+arr
                return(f)
        else:
            return(arr)
    if a==9:
        a=0
        a,arr[-1]=arr[-1],a
        b=int(arr[-2]+1)
        b,arr[-2]=arr[-2],b
        return(arr)
        if arr[-2]==10:
            arr[-2],c=c,arr[-2]
            e=int(arr[-3])+1
            arr[-3],e=e,arr[-3]
            return(arr)
            if arr[-3]==10:
                arr[-3],f1=f1,arr[-3]
                f=[1]+arr
                return(f)


    
            
        



