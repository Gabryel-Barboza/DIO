# Definindo schemas de retorno para o usuário
from marshmallow import fields

from src.app.app import ma
from src.views.role_schema import RoleSchema


class UserSchema(ma.Schema):
    # Define os campos que vão compor o schema
    class Meta:
        fields = ('id', 'username', 'role')

    # role é um campo de outro schema
    role = ma.Nested(RoleSchema)


class CreateUserSchema(ma.Schema):
    # Definindo campos obrigatórios
    username = fields.String(required=True)
    password = fields.String(required=True)
    role_id = fields.Integer(required=True, strict=True)
