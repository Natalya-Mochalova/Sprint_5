import random


def generation_email():
    return f'testtest{random.randint(0, 999)}@ya.com'
    
def generation_password():
    return f'{random.randint(100, 999)}Qwery'
