import re
with open('input.txt','r') as f:
    raw = f.read()

mul_mat = []
#pattern = r"don't.*?(?=\bdo\b|$)"
# God knows why doing re.sub(pattern,'',raw',flags=..) isn't working
matches = re.sub(r"don't.*?(?=\bdo\b|$)",'',raw,flags=re.DOTALL | re.IGNORECASE)

mul_mat = re.findall(r"mul\((\d+),(\d+)\)",matches)

print(sum([int(x)*int(y) for x,y in mul_mat]))
