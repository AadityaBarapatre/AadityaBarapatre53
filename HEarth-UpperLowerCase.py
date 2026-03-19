S=input()
ans=""
for i in S:
    if i.islower():
        ans+=i.upper()
    else:
        ans+=i.lower()

print(ans)