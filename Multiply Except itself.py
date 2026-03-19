n = list(map(int, input("Sample Input: ").split()))
new = []

for i in range(len(n)):
    temp = 1
    for j in range(len(n)):
        if i != j:
            temp = temp * n[j]
    new.append(temp)

print(new)