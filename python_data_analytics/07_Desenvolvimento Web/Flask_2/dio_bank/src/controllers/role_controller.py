from http import HTTPStatus

from flask import Blueprint, request

from src.models import Role, db

app = Blueprint('role', __name__, url_prefix='/roles')


def _create_role():
    data = request.json
    role = Role(name=data['name'])
    db.session.add(role)
    db.session.commit()


def _list_roles():
    query = db.select(Role)
    roles = db.session.execute(query).scalars()
    return [
        {
            'id': role.id,
            'name': role.name,
        }
        for role in roles
    ]


@app.route('/', methods=['GET', 'POST'])
def insert_roles():
    if request.method == 'GET':
        return {'roles': _list_roles()}
    else:
        _create_role()
        return {'message': 'Role Created'}, HTTPStatus.CREATED
