import operator
from collections import deque


class EvaluationStack:

    def __call__(self, stack):
        return EvaluationStack.eval(stack)

    @staticmethod
    def eval(stack):
        while len(stack) > 2:
            opd1, opd2, opr = stack.pop(), stack.pop(), stack.pop()
            try:
                opd = opr(opd1, opd2)
            except Exception as e:
                raise Exception('Stacking Language Error', e)
            else:
                stack.append(opd)
        if len(stack) > 1:
            raise Exception('Stacking Language Error')
        return stack.pop()


if __name__ == '__main__':
    f = EvaluationStack()
    expr = deque((operator.mul, 5, operator.add, 2, 3))
    print(f(expr))