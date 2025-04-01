def move_zeros(arr):
    
    for i in arr:
        if i == 0:
            arr.remove(0)
            arr.append(0)
        else:
            continue

    return arr

arr=[1,7,0,0,8,0,10,12,0,4]
print(move_zeros(arr))