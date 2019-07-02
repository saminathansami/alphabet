# alphabet
from itertools import combinations
sam,v1=input().split()
v1=int(v1)
m=[]
dd=combinations(sam,len(sam)-v1)
for i in list(dd):
  m.append("".join(i))
print(min(m))
