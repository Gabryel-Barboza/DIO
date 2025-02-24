from http import HTTPStatus

from sqlalchemy import func

from src.app.app import User, db


# Usando fixtures definidas em conftest.py
def test_get_user_success(client, access_token):
    # Given
    user = db.session.execute(db.select(User)).scalar_one()
    # When
    # client é uma aplicação Flask com interface de requisições
    response = client.get(
        f'/users/{user.id}', headers={'Authorization': f'Bearer {access_token}'}
    )

    # Then
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'id': user.id,
        'username': user.username,
        'role': {'id': user.role_id, 'role': user.role.name},
    }


def test_get_user_not_found(client, access_token):
    # Given
    user_id = len(db.session.execute(db.select(User)).scalars().all()) + 1

    # When
    response = client.get(
        f'/users/{user_id}', headers={'Authorization': f'Bearer {access_token}'}
    )

    # Then
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_list_users_success(client, access_token):
    # Given
    users = db.session.execute(db.select(User)).scalars()
    # When
    response = client.get(
        '/users/', headers={'Authorization': f'Bearer {access_token}'}
    )
    # Then
    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'users': [
            {
                'id': user.id,
                'username': user.username,
                'role': {'id': user.role_id, 'role': user.role.name},
            }
            for user in users
        ]
    }


def test_create_user_success(client, access_token):
    # Given
    user = db.session.execute(db.select(User)).scalar_one()
    result = client.post(
        '/auth/login/', json={'username': user.username, 'password': user.password}
    )
    access_token = result.json['access_token']

    # When
    payload = {'username': 'Kaio', 'password': '123', 'role_id': user.role_id}
    response = client.post(
        '/users/', json=payload, headers={'Authorization': f'Bearer {access_token}'}
    )

    # Then
    assert response.status_code == HTTPStatus.CREATED
    assert response.json == {'message': 'User created'}
    assert db.session.execute(db.select(func.count(User.id))).scalar() == 2
