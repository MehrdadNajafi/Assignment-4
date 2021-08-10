def Checkered_page(m,n):
    for i in range(m):
        
        if i%2 == 0:
            for j in range(n):
                
                if j%2 == 0:
                    print('#',end='')
                
                else:
                    print('*',end='')
            print()
        
        elif i%2 != 0:
            for j in range(n):
                
                if j%2 == 0:
                    print('*',end='')
                
                else:
                    print('#',end='')
            print()

x = int(input('pls enter the number of row: '))
y = int(input('pls enter the number of column: '))
Checkered_page(x,y)