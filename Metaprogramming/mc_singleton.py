import logging
import sys
from dec_logger import logger


class Singleton(type):
    @logger(logging.DEBUG)
    def __init__(cls, *args, **kwargs):
        print('Creating Singleton')
        cls.__instance = None
        super().__init__(*args, **kwargs)

    @logger(logging.DEBUG)
    def __call__(cls, *args, **kwargs):
        print(f'{cls}() Singleton called')
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class Spam(metaclass=Singleton):
    @logger(logging.DEBUG)
    def __init__(self):
        print('Creating Spam')

    @logger(logging.DEBUG)
    def __call__(self):
        print(f'{self}() Spam called')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    print('&&&&&' * 20)
    s = Spam()
    print('*****'*20)
    s()
    print('-----'*20)
    t = Spam()
    print('+++++' * 20)
    t()
    print(f's is t: {s is t}')
    print('Done')
