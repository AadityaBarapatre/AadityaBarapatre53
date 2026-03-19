L=int(input())
N=int(input())
for i in range(N):
    W,H=map(int,input().split())

    if W<L or H<L:
        print("UPLOAD ANOTHER")
    else:
        if W==H:
            print("ACCEPTED")
        else:
            print("CROP IT")