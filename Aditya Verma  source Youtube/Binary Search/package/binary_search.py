def binarysearch(array,x):
    start = 0
    end = len(array)-1
    
    while(start<=end):
        mid = start +(end-start)//2
        if array[mid] == x:
            return mid
        elif array[mid]>x:
            end = mid-1
        else:
            start = mid+1
    return -1

