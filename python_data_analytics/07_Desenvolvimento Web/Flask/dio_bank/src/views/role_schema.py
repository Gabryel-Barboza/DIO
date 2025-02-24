from src.app.app import ma


class RoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
