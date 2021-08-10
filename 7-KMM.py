num1 = int(input('pls enter number1: '))
num2 = int(input('pls enter number2: '))

list_1 = []
list_2 = []

c = 1
while True:
    x1 = num1*c
    x2 = num2*c
    
    list_1.append(x1)
    list_2.append(x2)
    
    for item1 in list_1:
        for item2 in list_2:
            if item1 == item2:
                print(f'KMM is: {item1}')
                exit()

    c += 1