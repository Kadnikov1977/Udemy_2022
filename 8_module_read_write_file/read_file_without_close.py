with open('sample.txt', 'r') as text1:
    for i in text1:
        print(i, end='')


with open('sample.txt', 'r') as text2:
    text = text2.read()

print(text, end='')