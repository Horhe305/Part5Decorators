""" Decorators, Examples where they can be used """
from random import randint
from time import time, sleep


# def run_script():
#     t1 = time()
#     sleep(randint(1, 4))
#     t2 = time()
#     print(f'The program is finished in {t2 - t1}')
#
#
# run_script()

def execution_time(func):
    def wrapper_fn(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'The program is finished in {t2 - t1}')

    return wrapper_fn


@execution_time
def run_script():
    sleep(randint(1, 4))


# run_script()

# example 2
user1 = {
    'registered': True,
    'name': 'Tom',
    'email': 'tom@gmail.com'
}
user2 = {
    'registered': False,
    'name': 'Jim',
    'email': 'jim@gmail.com'
}


def logged_in(func):
    def wrapper_fn(*args, **kwargs):
        if args[0]['registered']:
            func(*args, **kwargs)
        else:
            print('You are not registered')

    return wrapper_fn


@logged_in
def welcome_message(user):
    print(f'Welcome {user["name"]}')


welcome_message(user1)
welcome_message(user2)
