def Multiplication_table(n,m):
    print(f' x\t\b', end='')
    
    for k in range(1,m+1):
        print(f'({k})', end='\t\b')
    print()

    for i in range(1,n+1):
        print(f'({i})', end='\t')

        for j in range(1,m+1):
            print(i*j, end='\t')
        print()

num1 = int(input('pls enter number1: '))
num2 = int(input('pls enter number2: '))

Multiplication_table(num1,num2)