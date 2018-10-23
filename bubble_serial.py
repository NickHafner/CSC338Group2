def sort(a):
    numSwaps = 0
    j = 0
    while j < len(a)-1:
        i = 0
        while i < len(a)-1 - j:
            if a[i] > a[i+1]:
                numSwaps+=1
                a[i], a[i+1] = a[i+1], a[i]
            i+=1
        j+=1
        
    return a