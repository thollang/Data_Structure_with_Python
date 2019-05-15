

def select_sort(alist):
    n = len(alist)
    for j in range(0,n-2):
        min_index = j
        for i in range(j+1,n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
    li = [54,226,93,17,77,31,44,55,20]
    print(li)
    select_sort(li)
    print(li)
