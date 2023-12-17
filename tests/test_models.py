from conftest import book


def test_book_content(book):
    assert book.title == 'A good title'
    assert book.subtitle == 'An excellent subtitle'
    assert book.author == 'John Doe'
    assert book.isbn == '1234567890123'
