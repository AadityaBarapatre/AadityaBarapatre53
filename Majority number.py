a=list(map(int,input("Sample Input: ").split()))
n=len(a)
temp=0
for i in a:
    if (i>n/2):
        if (i>temp):
            temp=i
print(temp)