from random import randint


def get_random_email():
    return f'test{str(randint(10000, 20000))}@mail.com'
