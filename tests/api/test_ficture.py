import pytest


@pytest.mark.check
def test_change_name(user):
    assert user.name == 'Kyrylo'


@pytest.mark.check
def test_last_name(user):
    assert user.last_name == 'Kharkiv'
