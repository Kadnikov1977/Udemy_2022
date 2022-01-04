# def is_cat_here(*args):
#     list1 = [str(i).lower() for i in list(args)]
#     if 'cat' in list1:
#         return True
#     else:
#         return False
#
# print(is_cat_here('Harry', 'Cat', 'Chpoker'))
#
# def is_item_here(item, *args):
#     if item in list(args):
#         return True
#     else:
#         return False
#
# print(is_item_here('qwerty', 'Cat', 'Chpoker', 'qwerty'))

#================================================================

def your_favorite_color(my_color, **kwargs):
    if my_color > kwargs['age']:
        return 'Агай'
    else:
        return 'Щегол'

e = your_favorite_color(43, firstname = 'Harry', secondname = 'Chpoker', age = 44)

print(e)



