import pytest


def test_succeed():
    assert True


@pytest.mark.strict
@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
