#The array/list must be sorted to apply this algorithm.

def binarySearch(mylist,target):
    l=0
    r=len(mylist)-1
    while True:
        mid=int((r+l)/2)
        if mylist[mid]==target:
            return mid
        elif mylist[mid]>target:
            r=mid-1
        else:
            l=mid+1
        if l>r :
            return -1
        
    
mylist=[3,5,7,9,10,11,12,13,14,15,16,18]
print(binarySearch(mylist,5))