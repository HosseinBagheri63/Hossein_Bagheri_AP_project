import time
def BubbleSort(lst: list):
    is_changed= True
    while is_changed:
        is_changed= False
        for i in range (1,len(lst)):
            if lst[i-1]> lst[i]:
                lst[i-1],lst[i]= lst[i], lst[i-1]
                is_changed = True
    return lst

def MergeSort(lst: list):
    if len(lst)==0 or len(lst)==1:
        return lst
    else:
        middle_indx=(len(lst)//2)
        L1:list= MergeSort(lst[:middle_indx])
        L2:list= MergeSort(lst[middle_indx:])
        L3=[]
        i=j=0
        while i<len(L1) and j<len(L2):
            if L1[i] <= L2[j]:
                L3.append(L1[i])
                i+=1
            else:
                L3.append(L2[j])
                j+=1
        L3+=L1[i:]
        L3+=L2[j:]
    return L3
#############################################################
l1=list(range(1000,0,-1))
l2=list(range(10000,0,-1))
l3=list(range(100000,0,-1))
#l4=list(range(1000000,0,-1))
start=time.perf_counter()
BubbleSort(l1)
end=time.perf_counter()
print('Bubblesort'+ str(end-start))
start=time.perf_counter()
MergeSort(l1)
end=time.perf_counter()
print('Mergesort'+ str(end-start))
start=time.perf_counter()
BubbleSort(l2)
end=time.perf_counter()
print('Bubblesort'+ str(end-start))
start=time.perf_counter()
MergeSort(l2)
end=time.perf_counter()
print('Mergesort'+ str(end-start))
start=time.perf_counter()
BubbleSort(l3)
end=time.perf_counter()
print('Bubblesort'+ str(end-start))
start=time.perf_counter()
MergeSort(l3)
end=time.perf_counter()
print('Mergesort'+ str(end-start))
# start=time.perf_counter()
# BubbleSort(l4)
# end=time.perf_counter()
# print('Bubblesort'+ str(end-start))
# start=time.perf_counter()
# MergeSort(l4)
# end=time.perf_counter()
# print('Mergesort' + str(end-start))