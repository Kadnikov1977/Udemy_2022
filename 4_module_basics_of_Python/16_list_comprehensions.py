greetings = ['hello', 'hi', 'hey', 'hola']
list1 = []
for i in greetings:
    list1.append(i[1])
print(list1)

list2 = [i[1] for i in greetings]
print(list2)


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in digits:
    if i % 2 == 0:
        print(i)

list3 = [i for i in digits if i % 2 == 0]
print(list3)

