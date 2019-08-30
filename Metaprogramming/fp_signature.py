from inspect import signature, Signature, Parameter

def func(a, b=42, *args, d=None, **kwargs):
    pass


if __name__ == '__main__':
    sig1 = signature(func)
    print(sig1)

    parms = [
        Parameter('a', Parameter.POSITIONAL_OR_KEYWORD),
        Parameter('b', Parameter.POSITIONAL_OR_KEYWORD, default=42),
        Parameter('args', Parameter.VAR_POSITIONAL),
        Parameter('d', Parameter.KEYWORD_ONLY, default=None),
        Parameter('kwargs', Parameter.VAR_KEYWORD)]

    sig2 = Signature(parms)
    print(sig2)

    print(f'sig1 == sig2: {sig1 == sig2}')