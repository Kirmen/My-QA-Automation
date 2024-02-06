import pytest

from modules.api.clients.github import GitHub


class User:
    def __init__(self):
        self.name = None
        self.last_name = None

    def create(self):
        self.name = 'Kyrylo'
        self.last_name = 'Kharkiv'

    def remove(self):
        self.name = ''
        self.last_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

@pytest.fixture
def github_api():
    api = GitHub()
    yield api