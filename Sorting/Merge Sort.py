def mergeSort(mylist):
    if len(mylist)<=1:
        return mylist
    mid=int(len(mylist)/2)
    list_a=[]
    list_b=[]
    for i in range(0,mid):
        list_a.append(mylist[i])
    for i in range(mid,len(mylist)):
        list_b.append(mylist[i])
    
    sorted_a=mergeSort(list_a)
    sorted_b=mergeSort(list_b)
    
    result=[]
    x=0
    y=0
    
    for i in range(0,len(mylist)):
        if x==len(sorted_a):
            result.append(sorted_b[y])
            y+=1
        elif y==len(sorted_b):
            result.append(sorted_a[x])
            x+=1
        elif sorted_a[x]>sorted_b[y]:
            result.append(sorted_b[y])
            y+=1
        else:
            result.append(sorted_a[x])
            x+=1
    
    return result

test_list=[9,54,98,32,74,72,985,758,93,75,38]
print(mergeSort(test_list))

test_list2=[]
print(test_list2)

test_list3=[4]
print(test_list3)