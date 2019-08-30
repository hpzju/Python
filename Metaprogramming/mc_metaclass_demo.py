class MetaType(type):
    print(f'in "MetaType" code')

    @classmethod
    def __prepare__(mcs, clsname, bases):
        print(f'in "{MetaType.__name__}" prepare: ')
        print('\t', f'"mcs" =: {mcs} ')
        print('\t', f'"clsname" =: {clsname}  ')
        print('\t', f'"bases" =: {bases}')
        return type.__prepare__(mcs, clsname, bases)

    def __new__(mcs, clsname, bases, clsdict):
        print(f'in "MetaType" new: ')
        print('\t', f'"cls" =: {mcs} ')
        print('\t', f'"clsname" =: {clsname}  ')
        print('\t', f'"bases" =: {bases}')
        print('\t', f'"clsdict" =: {clsdict}')
        return type.__new__(mcs, clsname, bases, clsdict)

    def __init__(cls, clsname, bases, clsdict):
        print(f'in "MetaType" init: ')
        print('\t', f'"cls" =: {cls} ')
        print('\t', f'"clsname" =: {clsname}  ')
        print('\t', f'"bases" =: {bases}')
        print('\t', f'"clsdict" =: {clsdict}')
        type.__init__(cls, clsname, bases, clsdict)

    # def __call__(cls, *args, **kwargs):
    #     print("^^^^^"*10)
    #     print(f'in "MetaType" call: ')
    #     print('\t', f'"self" =: {cls} ')
    #     print('\t', f'"args" =: {args}  ')
    #     print('\t', f'"kwargs" =: {kwargs}')
    #     print("^^^^^"*10)
    #     c = super(cls)
    #     print(f'super{cls} = {c} with type = {type(c)}')

    def spam(cls):
        print(f'in "MetaType" spam: ')


class Typed(metaclass=MetaType):
    print(f'in "Typed" code')

    def __init__(self, *args, **kwargs):
        print(f'in "Typed" init: ')
        print('\t', f'"self" =: {self} ')
        print('\t', f'"args" =: {args}  ')
        print('\t', f'"kwargs" =: {kwargs}')

    def __call__(self, *args, **kwargs):
        print(f'in "Typed" call: ')
        print('\t', f'"self" =: {self} ')
        print('\t', f'"args" =: {args}  ')
        print('\t', f'"kwargs" =: {kwargs}')


class IntType(Typed):
    print(f'in "IntType" code')

    def spam(self):
        c = super()
        print(f'super{self} = {c} with type = {type(c)}')


if __name__ == '__main__':
    print('--main start--' * 6)
    t = IntType('a', 32)
    print('***'*20)
    t(1)
    t.spam()
    print(IntType.mro())
    print('--main end--' * 6)
