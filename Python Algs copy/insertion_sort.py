a = [3,4,1]
alist = [54,26,93,17,77,31,44,55,20]

def insertion_sort(a):
    for i in range(1,len(a)):
        this = a[i]
        pos = i
        while pos>0 and a[pos-1]>this:
            a[pos] = a[pos-1]
            pos=pos-1

        a[pos]=this

insertion_sort(a)
print(a)

