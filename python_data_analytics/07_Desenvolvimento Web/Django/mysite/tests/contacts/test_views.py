from http import HTTPStatus

import pytest
from django.contrib.auth.models import Permission
from django.urls import reverse


def test_contacts_thanks(client):
    # Given
    name = 'Gabryel'

    # When
    response = client.get(f'/contacts/thanks/{name}')

    # Then
    assert response.status_code == HTTPStatus.OK
    # Retorna um binário, decodifique
    assert response.content.decode() == f'Obrigado {name}'
    # TODO: Test templates


def test_contacts_create_with_unauthenticated_user(client):
    # Given
    url = f'{reverse("accounts:login")}?next={reverse("contacts:create")}'

    # When
    response = client.get('/contacts/create/')
    # breakpoint()

    # Then
    assert response.url == url
    assert response.status_code == HTTPStatus.FOUND


# @pytest.mark.skip() # Pula esse teste
@pytest.mark.django_db
def test_contacts_create_success(client, django_user_model):
    # Given
    data = {
        'subject': 'subject@email.com',
        'message': 'Hello World!',
        'sender': 'sender@testemail.com',
        'cc_myself': True,
    }
    name = data['sender'].split('@')[0]

    user = django_user_model.objects.create_user(
        username='gabryel', email='gabryel@email.com', password='123'
    )

    permission = Permission.objects.get(codename='add_contact')
    user.user_permissions.add(permission)

    # When
    client.force_login(user)
    response = client.post(reverse('contacts:create'), data)
    # breakpoint()

    # Then
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse('contacts:thanks', args=(name,))
