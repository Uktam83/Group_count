a=[]
for i in range(10):
    b = input()
    a.append(b)
lst=[]
for i in range(len(a)):
    lst.append(len(a[i]))
ans=sorted(list(set(lst)))[::-1]
mx1,mx2,mx3=ans[0],ans[1],ans[2]
for i in range(len(a)):
    if len(a[i])==mx1 or len(a[i])==mx2 or len(a[i])==mx3:
        print(a[i],end=" ")

