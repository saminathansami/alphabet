p,q,c=map(int,input().split())
if(p>q):
    if(p>c):
        print(p)
    else:
        print(c)
elif(q>c):
    print(q)
else:
    print(c)
