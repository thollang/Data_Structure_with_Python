def quick_sort(alist,first,last):
    if first >= last:
        return 
    mid_value = alist[first]
    low = first
    high = last


    while low < high: 
        #high left shift
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]   

        #low right shift 
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    
    #when left while, low==high
    alist[low] = mid_value
    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)

if __name__ == "__main__":
    li = [54,36,93,17,77,31,44,55,20]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)
