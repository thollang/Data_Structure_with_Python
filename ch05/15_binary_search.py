def binary_search(alist, item):
    n = len(alist)
    mid = (n-1)//2 
    if n > 0:
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False

if __name__ == "__main__":
    li = [17,20,26,31,44,54,55,77,93]
    print(binary_search(li, 55))
    print(binary_search(li, 100))
