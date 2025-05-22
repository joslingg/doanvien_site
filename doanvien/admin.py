from django.contrib import admin
from .models import Department,Member,Group

admin.site.register(Member)
admin.site.register(Department)
admin.site.register(Group)