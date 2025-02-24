from functools import wraps
from http import HTTPStatus

from flask_jwt_extended import get_jwt_identity

from src.models import User, db


def requires_role(role_name):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            user_id = get_jwt_identity()
            user = db.get_or_404(User, user_id)
            if user.role.name != role_name:
                return {'message': 'Access Unauthorized'}, HTTPStatus.FORBIDDEN
            return f(**kwargs)

        return wrapped

    return decorator


# Função para primeiros testes unitários
def square_number(num):
    return num**2
