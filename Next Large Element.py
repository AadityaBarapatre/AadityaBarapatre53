arr = [1,3,2,4]
n = len(arr)
output=[]
for i in range(n):
    for j in range(i+1,n):
        if (arr[j]>arr[i]):
            output.append(arr[j])
            break
    else:
        output.append(-1)
print(output)