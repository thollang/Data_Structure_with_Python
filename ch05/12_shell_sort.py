def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for j in range(1,n):
            for j in range(gap,n):
                i = j
                
                while i >= gap:
                    if alist[i] < alist[i-gap]:
                        alist[i], alist[i-gap] = alist[i-gap], alist[i]
                        i -= gap
                    else:
                        break
        gap //=2

if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    shell_sort(li)
    print(li)
