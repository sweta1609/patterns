n = int(input())
i=1
while i<=n:
    j=0
    while j<i:
        print(0 if j and j<i-1 else i-1 or 1,end='')
        j=j+1
    print()
    i=i+1
    
