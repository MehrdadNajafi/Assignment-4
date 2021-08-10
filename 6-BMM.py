num1 = int(input('pls enter number1: '))
num2 = int(input('pls enter number2: '))

list_1 = []
list_2 = []
result_list = []

for i in range(1, num1+1):
    if num1 % i == 0:
        list_1.append(i)

for i in range(1, num2+1):
    if num2 % i == 0:
        list_2.append(i)

if num1<=num2:
    for item1 in list_1:
        for item2 in list_2:
            if item1 == item2:
                result_list.append(item1)

    max = result_list[0]
    for i in range(1, len(result_list)):
        if result_list[i] > max:
            max = result_list[i]

    print(f'BMM is: {max}')

elif num1>num2:
    for item2 in list_2:
        for item1 in list_1:
            if item2 == item1:
                result_list.append(item2)

    max = result_list[0]
    for i in range(1, len(result_list)):
        if result_list[i] > max:
            max = result_list[i]

    print(f'BMM is: {max}')