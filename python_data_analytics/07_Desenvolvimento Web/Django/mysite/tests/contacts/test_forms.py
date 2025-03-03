from contacts.forms import NameForm


def test_name_form_success(client):
    # Given
    data = {'your_name': 'Gabryel'}

    # When
    form = NameForm(data=data)
    is_valid = form.is_valid()

    # Then
    assert is_valid is True


def test_name_form_fail(client):
    # Given
    data = {}

    # When
    form = NameForm(data=data)
    is_valid = form.is_valid()

    # Then
    assert is_valid is False


def test_name_form_your_name_max_length():
    # Given
    data = {'your_name': 'John' + 'k' * 100}

    # When
    form = NameForm(data=data)
    is_valid = form.is_valid()

    # breakpoint()

    # Then
    assert is_valid is False
    assert form.errors == {
        'your_name': [
            'Certifique-se de que o valor tenha no máximo 100 caracteres (ele possui 104).'
        ]
    }
