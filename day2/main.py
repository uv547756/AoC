arr = []
with open('input.txt','r') as f:
    for line in f:
        x = list(map(int,line.strip().split())) #X is itself an arr of size == len(line)
        arr.extend(x)
print(arr[1])
        
