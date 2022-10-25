from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['tab_num','username','first_name','last_name','email','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('tab_num',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('tab_num',)}),
    )

admin.site.register(CustomUser,CustomUserAdmin)
