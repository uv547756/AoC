from collections import Counter
arr = []
with open('input.txt', 'r') as f:
    for line in f:
        x = list(map(int,line.strip().split()))
        arr.append(x)

def valid(seq):
    if len(seq) < 2:
        return True
    increasing = seq[1] > seq[0]
    decreasing = seq[1] < seq[0]

    for i in range(1,len(seq)):
        diff = seq[i] - seq[i-1]
        if diff not in [1,2,3]:
            return False
        if (increasing and diff<0) or (decreasing and diff>0):
            return False
    return True

def relax(sub_seq):
    if valid(sub_seq):
        return True
    for i in range(len(sub_seq)):
        n_seq = sub_seq[:i]+sub_seq[i+1:]
        if valid(n_seq):
            return True
    return False

res = [relax(sub_seq) for sub_seq in arr]
print(Counter(res))
