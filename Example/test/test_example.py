import pytest


@pytest.fixture
def error_fixture():
    assert 0


@pytest.fixture(scope="module")
def smtp_connection():
    import smtplib
    return smtplib.SMTP("smtp.qq.com", 587, timeout=20)


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    print(msg)


def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass


@pytest.mark.xfail(raises=IndexError)
def test_f():
    a = []
    a[1]


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert "maximum recursion" in str(excinfo.value)


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        raise ValueError("Exception 123 raised")

