import math

def sort(a, left, right):
    if (left >= right):
        return
    center = math.floor((left+right)/2)
    sort(a, left, center)
    sort(a, center+1, right)
    merge(a, left, right, center)

    return a

def merge(a, left, right, center):
    n1 = center - left + 1
    n2 = right- center 
    leftarr = [0]*n1
    rightarr = [0]*n2
  
    for i in range(0 , n1): 
        leftarr[i] = a[left + i] 
  
    for j in range(0 , n2): 
        rightarr[j] = a[center + 1 + j] 
  
    i,j,leftStart = 0,0,left
  
    while i < n1 and j < n2 : 
        if leftarr[i] <= rightarr[j]: 
            a[leftStart] = leftarr[i] 
            i += 1
        else: 
            a[leftStart] = rightarr[j] 
            j += 1
        leftStart += 1

    while i < n1: 
        a[leftStart] = leftarr[i] 
        i += 1
        leftStart += 1
  
    while j < n2: 
        a[leftStart] = rightarr[j] 
        j += 1
        leftStart += 1
    