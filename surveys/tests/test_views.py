import pytest


@pytest.mark.django_db
def test_with_client(client):
    response = client.get('')
    # assert response.content == 'Foobar'
    print(response)
    assert False