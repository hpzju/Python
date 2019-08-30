import sys


def tail_recursion():
    pass


def tail_adder(seq, s=0):
    if len(seq) == 0:
        return s
    else:
        return tail_adder(seq[1:], s+seq[0])


if __name__ == '__main__':
    l = [i for i in range(101)]
    print(tail_adder(l))
    print(tail_adder([i for i in range(sys.getrecursionlimit())]))