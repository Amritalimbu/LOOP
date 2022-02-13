list=[6,1,3,5,6,3,1]
a=[]
i=0
while i<len(list):
    if list[i]not in a:
        a.append(list[i])
    i=i+1
mul=1
j=0
while j<len(a):
    mul=mul*a[j]
    j=j+1
print(mul)