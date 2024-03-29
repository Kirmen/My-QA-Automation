import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''


@pytest.mark.check
def test_name(user):
    assert user.name == 'Kyrylo'


@pytest.mark.check
def test_last_name(user):
    assert user.last_name == 'Kharkiv'
