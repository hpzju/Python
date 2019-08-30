import pytest
from src.evaluation_stack import EvaluationStack
from collections import deque
import operator


@pytest.fixture
def evs():
    yield EvaluationStack()


class TestEvaluationStack:

    def test_add(self, evs):
        expr = deque((operator.add, 1, 2))
        assert 3 == evs(expr)

    def test_add_fail(self, evs):
        expr = deque((operator.add, 1, 2, 4))
        with pytest.raises(Exception):
            evs(expr)

    def test_mul(self, evs):
        expr = deque((operator.mul, 10, 2))
        assert 20 == evs(expr)

    def test_mul_add(self, evs):
        expr = deque((operator.mul, 10, operator.add, 8, operator.mul, 10, 2))
        assert 280 == evs(expr)

    def test_skip(self):
        pytest.skip('skip this test')