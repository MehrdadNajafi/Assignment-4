num1 = int(input('pls enter a number: '))

m = 1
for i in range(1,num1+1):
    m *= i
    if m == num1:
        print(f'Yes\n{i}!')
        break
    elif i == num1 and m != num1 :
        print('No')