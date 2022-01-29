from django.contrib import admin
from .models import Account
# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email','first_name', 'last_name','date_joined', 'last_login', 'is_staff', 'is_admin')
    search_fields = ('email',)
    readonly_fields = ('id','date_joined', 'last_login',)
# Register your models here.
admin.site.register(Account,AccountAdmin)