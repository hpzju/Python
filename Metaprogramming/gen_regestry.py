from functools import wraps


def genpass_regestry(genfunc, pass=1):
    pass


def infinite_gen():
    counter = 0
    while True:
        counter += 1
        yield counter