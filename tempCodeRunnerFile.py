a=input()
b=input()
c=len(a)
d=len(b)
e=''
f=0
if(c>=d):
    f=c

else:
    f=d


for i in range(0,f):
    if(c>=i):
        e+=a[i]
    if(d>=i):
        e+=b[i]
#     if(f<c):
#         
#     if(f<d):
#         
print(e)
