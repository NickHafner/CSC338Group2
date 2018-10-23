import math

def sort(a, left, right):
    if (left >= right):
        return

    pivot = a[math.floor((left+right)/2)]
    index = partition(a, left, right, pivot)
    sort(a, left, index-1)
    sort(a, index, right)

    return a
        

def partition(a, left, right, pivot):
    while (left <= right):
        while (a[left] < pivot):
            left+=1
        while (a[right] > pivot):
            right-=1
        
        if (left <= right):
            a[left], a[right] = a[right], a[left]
            left+=1
            right-=1
            
    return left

