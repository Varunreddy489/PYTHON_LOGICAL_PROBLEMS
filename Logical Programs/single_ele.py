def single_ele(arr):
    
    obj={}
    
    for i in arr:
        if i in obj:
            obj[i]+=1
        else:
            obj[i]=1
    
    return obj
    
arr=[2,2,1]
print(single_ele(arr))