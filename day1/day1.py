arr1 = []
arr2 = []
res = []
with open('input.txt','r') as file:
    for line in file:
        x,y = map(int,line.strip().split())
        arr1.append(x)
        arr2.append(y)

sorted_arr1 = sorted(arr1)
sorted_arr2 = sorted(arr2)
for x,y in zip(sorted_arr1,sorted_arr2):
    res.append(abs(x-y))
# print(f'Smallest of arr1 {sorted_arr1[0]} - {sorted_arr2[0]} = {res[0]}')
print(f"sum of array is: {sum(res)}")

# Bsearch for faster search
'''def Bsearch(target,arr[],l,h):
    if l>h:
        return -1
    mid = l+(l+h)//2 
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return Bsearch(target,arr[],mid+1,h)
    else:
        return Bsearch(target,arr[],l,mid-1)
'''
'''
## Bisect
## excuz me wada fukk
import bisect

def occur(target, sorted_arr2):
    first = bisect.bisect_left(sorted_arr2,target)
    last = bisect.bisect_right(sorted_arr2,target)
    return last - first

def count(sorted_arr1, sorted_arr2):
    res = {}
    for x in sorted_arr1:
        res[x] = occur(x,sorted_arr2)
    return res
## Similarity score 
counts = count(sorted_arr1,sorted_arr2)
res2 = []
for x, y in counts.items():
    if y!=0:
        res2.append(x*y)
        print(f'Element {x} appears {y} times in list2')
#print((res))

'''

from collections import Counter
r_freq = Counter(sorted_arr2)
res = sum(left*r_freq.get(left,0) for left in sorted_arr1) # Ureka moment
print(res)
