def gym(X,Y,Z):
    if X+Y<=Z:
        print(2)
    elif X<=Z:
        print(1)
    else:
        print(0)
X,Y,Z=map(int,input().split())
gym(X,Y,Z)
