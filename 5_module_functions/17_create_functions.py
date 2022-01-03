def cat_voice():
    print('Meow!')

def dog_voice():
    print('Woof!')


def cat_voice1():
    return 'Meow!'

def dog_voice1():
    return 'Woof!'


cat_voice()
dog_voice()

cat_voice()
dog_voice()
cat_voice()
dog_voice()


def get_voice(s):
    return str(s) + '!'

print(get_voice(5))


def odd_range(x, y):
    list2 = []
    for i in range(x, y + 1):
        if i % 2 == 0:
            list2.append(i)
    return list2

print(odd_range(3, 15))

def odd_range1(x,y):
    list3 = [i for i in range(x, y + 1) if i % 2 == 0]
    return list3

print(odd_range1(3, 15))