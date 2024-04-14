""" Decorators """


def print_hi():
    return f'Hi there'


# message = print_hi()
message = print_hi
# print(message)
print(message())


def print_m(funct_name):
    return (funct_name())


def message():
    return "Message fn"


msg = print_m(message)
print(msg)


# HOC (High Order Component)
def first():
    def second():
        return 'Hi'

    return second()


print(first())
