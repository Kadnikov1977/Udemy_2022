color = ['red', 'blue', 'black', 'white']

with open('colors.txt', 'w') as file1:
    for i in color:
        print(i, file=file1)

