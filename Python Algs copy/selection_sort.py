def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

a = [1,3,6,2]
alist = [54,26,93,17,77,31,44,55,20]

def selection_sort(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
        swap(a,min,i)

selection_sort(alist)
print(alist)

# alist = [54,26,93,17,77,31,44,55,20]
# def selectionSort(List_):
#     for i in range(len(List_)):
#         min = i
#         for j in range(i+1,len(List_)):
#             if List_[j] < List_[min]:
#                 min = j
#         if min != i:
#             List_[min],List_[i] = List_[i],List_[min]
#
#
# selectionSort(alist)
# print(alist)