sam,se=input().split()
ram=abs(len(sam)-len(se))
for i in range(len(sam)):
    if len(se)==1 and se[i] in sam:
        break
    if sam[i]!=se[i]:
        ram+=1
print(ram)
