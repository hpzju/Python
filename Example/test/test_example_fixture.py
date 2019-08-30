import pytest

order = []


@pytest.fixture(scope="session")
def s1():
    order.append("s1")


@pytest.fixture(scope="module")
def m1():
    order.append("m1")


@pytest.fixture
def f1(f3):
    order.append("f1")


@pytest.fixture
def f3():
    order.append("f3")


@pytest.fixture(autouse=True)
def a1():
    order.append("a1")


@pytest.fixture
def f2():
    order.append("f2")


def test_order(f1, m1, f2, s1):
    print(order)
    assert order == ["s1", "m1", "a1", "f3", "f1", "f2"]


# fixture setup and teardown
@pytest.fixture(scope="module")
def smtp_connection():
    import smtplib
    smtp_connection = smtplib.SMTP("smtp.qq.com", 587, timeout=5)
    yield smtp_connection
    print("teardown smtp")
    smtp_connection.close()


@pytest.fixture(scope="module")
def smtp_connection2():
    import smtplib
    with smtplib.SMTP("smtp.qq.com", 587, timeout=5) as smtp_connection:
        yield smtp_connection
        print("teardown smtp")


def test_connection(smtp_connection):
    assert (250, b'Ok') == smtp_connection.noop()


def test_connection2(smtp_connection2):
    assert (250, b'Ok') == smtp_connection2.noop()
