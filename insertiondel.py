#insertion and deletion
aa,j2=map(str,input().split())
vj=0
if len(aa)>len(j2):
  aa,j2=j2,aa
i=0
while i<len(aa):
  vj+=(ord(j2[i])-ord(aa[i]))
  i+=1
for i in range(i,len(j2)):
  vj+=ord(j2[i])-ord('a')+1
print(vj)
