import pytest
from django.test.client import Client
from user.models import User
from django.contrib.auth.hashers import make_password


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user_instance(db):
    return User.objects.create(
        email="randomabc@gmail.com",
        password=make_password("abcd")
    )

@pytest.fixture
def auth_user_password() -> str:
    """Returns the password needed for authentication"""
    return "abcd"