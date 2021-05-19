import pytest
from pytest_example import api_example


@pytest.fixture
def credentials():
    return {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}


def test_login(credentials):
    # Arrange
    login = api_example.login
    email = credentials['email']
    password = credentials['password']

    # Act
    result = login(email, password)

    # Assert
    assert result.status_code == 200

    # Clean up
