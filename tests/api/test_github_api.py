import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunct')
    assert user['login'] == 'defunct'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergii-yo-yo-butenko123')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_one_char(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_emoji_exists(github_api):
    r = github_api.get_emojis()
    assert "100" in r


@pytest.mark.api
def test_emoji_not_exists(github_api):
    r = github_api.get_emojis()
    assert "1002523434242" not in r


@pytest.mark.api
def test_commits_can_be_found(github_api):
    r = github_api.search_commits('Kirmen', 'qa1')
    assert r[0]['commit']['author']['name'] == 'Kirmen'


@pytest.mark.api
def test_commits_cannot_be_found(github_api):
    r = github_api.search_commits('Kirmen-yo-yo', 'qa111')
    assert r['message'] == 'Not Found'
