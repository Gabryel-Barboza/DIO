# Customizando página MyAdmin
from django.contrib import admin

from polls.models import Choice, Question


# Customizando metadados do site
class CustomAdminSite(admin.AdminSite):
    site_header = 'Curso Django Admin'


# Registra os modelos para aparecerem no Django Admin

admin_site = CustomAdminSite()
# # Customizando modelos que devem aparecer
admin_site.register([Choice, Question])

# TODO: Adicionar modelos para páginas de controle de acesso
