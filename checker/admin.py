from django.contrib import admin
from .models import AdminUser, AdminRole

# Register your models here.
admin.site.register(AdminUser)
admin.site.register(AdminRole)
