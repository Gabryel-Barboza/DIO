from functools import wraps
from http import HTTPStatus

from flask_jwt_extended import get_jwt_identity

from src.app import User, db


# TODO: Adicionar args da request
def requires_role(role_name, *args):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            user_id = get_jwt_identity()
            user = db.get_or_404(User, user_id)
            if user.role.name != role_name:
                return {'message': 'Access Unauthorized'}, HTTPStatus.FORBIDDEN
            return f()

        return wrapped

    return decorator
