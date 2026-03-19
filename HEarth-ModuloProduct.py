N=int(input())
arr=list(map(int,input().split()))
answer=1
for i in range(N):
    answer=(answer*arr[i])%((10**9)+7)
print(answer)