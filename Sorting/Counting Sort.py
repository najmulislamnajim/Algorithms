import random
def countingSort(nums):
    maxEliment=max(nums) # O(n)
    freequencyArray=[0]*(maxEliment+1)
    sortedArray=[]
    for num in nums:
        freequencyArray[num]+=1
    
    for i in range(len(freequencyArray)):
        while freequencyArray[i]>0:
            sortedArray.append(i)
            freequencyArray[i]-=1
    
    return sortedArray
    # time complexity for Counting Sort is O(n+k).
    

array=[103, 582, 326, 712, 448, 671, 398, 584, 903, 649, 111, 239, 598, 479, 556, 762, 842,792, 374, 160, 987, 839, 561, 276, 449, 893, 704, 331, 184, 261, 819, 950, 245, 312, 766, 843, 561,764, 280, 670, 592, 352, 811, 718, 367, 981, 477, 158, 289, 901, 649, 223, 397, 550, 740, 390, 881,306, 221, 550, 720, 165, 794, 256, 456, 678, 513, 692, 120, 987, 334, 491, 765, 852, 297, 145, 967,814, 531, 791, 485, 358, 643, 567, 322, 891, 700, 499, 902]
print(array)
sortedArray=countingSort(array)
print(sortedArray)