# Definindo schemas de retorno para o usuário
from marshmallow import fields

from src.app.app import ma
from src.models import User
from src.views.role_schema import RoleSchema


class UserSchema(ma.SQLAlchemySchema):
    # Usando integração com SQLAlchemy para detecção de campo automático
    # Define os campos que vão compor o schema
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    # role é um campo de outro schema
    role = ma.Nested(RoleSchema)


class UserIDParameter(ma.Schema):
    user_id = fields.Integer(required=True, strict=True)


class CreateUserSchema(ma.Schema):
    # Definindo campos obrigatórios de um schema
    username = fields.String(required=True)
    password = fields.String(required=True)
    role_id = fields.Integer(required=True, strict=True)
