import re

raw = []
mul_mat = []
with open('input.txt','r') as f:
    for seq in f:
        raw.append(seq)

pattern = r'mul\((\d+),(\d+)\)'
for line in raw:
    match = re.findall(pattern,line)
    if match:
        mul_mat.extend(match)
res = [int(x)*int(y) for x,y in mul_mat]
print(sum(res))
