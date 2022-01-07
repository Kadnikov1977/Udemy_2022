color = ['indigo', 'green']

with open('colors.txt', 'a') as file2:
    for i in color:
        print(i, file=file2)


