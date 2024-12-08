from collections import Counter
arr = []
with open('input.txt','r') as f:
    for line in f:
        x = list(map(int,line.strip().split()))
        arr.append(x)

## arr is 2D array!! like [[1,2],[3,4]
def check(seq):
    if len(seq)<2:
        return True
    
    ## Case 1
    increasing = seq[1] > seq[0]
    decreasing = seq[1] < seq[0]
    
    for i in range(1,len(seq)):
        diff = seq[i]-seq[i-1]
        if abs(diff) not in [1,2,3]:
            return False
        if (increasing and diff<0) or (decreasing and diff>0):
            return False
    return True

def valid(arr):
    return [check(sub_arr) for sub_arr in arr]

res = Counter(valid(arr))
print(res)

