import pytest

from books import models


@pytest.fixture
def book(db):
    return models.Book.objects.create(
        title='A good title',
        subtitle='An excellent subtitle',
        author='John Doe',
        isbn='1234567890123'
    )
