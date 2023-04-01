import random
import time
import sys
print(sys.setrecursionlimit(3000))

def partition(A, p, r, q):
    pivot=A[q]
    i=p-1
    for j in range(p, r):
        if A[j] <= pivot:
            i+=1
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
    temp=A[i+1]
    A[i+1]=A[r]
    A[r]=temp
    return i+1

def quicksort_last(A):
    def quicksort_last_h(A, p, r):
        if p<r:
            q=partition(A, p, r, r)
            quicksort_last_h(A, p, q-1)
            quicksort_last_h(A, q+1, r)
    quicksort_last_h(A, 0, len(A)-1)
list1=[1488, 88, 420, 69, 14, 666]

def quicksort_random(A):
    def quicksort_random_h(A, p, r):
        if p<r:
            if (p-r)>2:
                a=random.randint(p, r)
                b=random.randint(p, r)
                c=random.randint(p, r)
                keys=[A[a], A[b], A[c]]
                keys.sort()
                pivot=A.index(keys[1])
            else:
                pivot=r
            q=partition(A, p, r, pivot)
            quicksort_random_h(A, p, q-1)
            quicksort_random_h(A, q+1, r)
    quicksort_random_h(A, 0, len(A)-1)

list_sizes=[10, 100, 200, 500, 1000, 1500, 2000]
def generate_sorted_list(size):
    slist=[]
    for i in range(size):
        slist.append(i)
    return slist

def generate_random_list(size):
    rlist=[]
    for i in range(size):
        rlist.append(random.randint(0, 1000))
    return rlist

def test_time(func, input):
    x=time.time()
    func(input)
    y=time.time()
    return y-x


for size in list_sizes:
    sorted=generate_sorted_list(size)
    random_l=generate_random_list(size)
    t1=test_time(quicksort_last, sorted)
    t2=test_time(quicksort_last, random_l)
    print("Runtime for list of size {} using version 1 is {} for a sorted list and {} for a random list.".format(size, t1, t2))

for size in list_sizes:
    sorted=generate_sorted_list(size)
    random_l=generate_random_list(size)
    t1=test_time(quicksort_random, sorted)
    t2=test_time(quicksort_random, random_l)
    print("Runtime for list of size {} using version 2 is {} for a sorted list and {} for a random list.".format(size, t1, t2))
