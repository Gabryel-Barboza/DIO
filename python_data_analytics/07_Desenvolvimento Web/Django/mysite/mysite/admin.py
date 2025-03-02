# Customizando página MyAdmin
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User

from polls.models import Choice, Question

# Customizando metadados do site
class CustomAdminSite(admin.AdminSite):
    site_header = 'Curso Django Admin'


# Registra os modelos para aparecerem no Django Admin

admin_site = CustomAdminSite()
# # Customizando modelos que devem aparecer
admin_site.register([Choice, Question])
admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)
