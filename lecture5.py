""" Generators intro """


# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# print(my_list[0])


def our_generator(n):
    for i in range(n):
        yield i


# for item in our_generator(5):
#     print(item)

item = our_generator(3)
print(next(item))
print(next(item))
print(next(item))
