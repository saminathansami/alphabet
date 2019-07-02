sam=int(input())
a=[]
for i in range(0,sam):
 ram=input()
 a.append(ram)
zi=[]
for i in zip(*a):
 if(i.count(i[0])==len(i)):
  zi.append(i[0])
 else:
  break
print("  ".join(zi))
