n = int (input())
i = 1;
while (i<=n):
    j = 1;
    while j<=i:
        print("1",end="")
        j = j + 1
        while j<=i-1:
            print("2",end="")
            j = j + 1
    
    i = i + 1
  
    
    print()
