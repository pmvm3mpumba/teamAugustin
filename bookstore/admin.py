from django.contrib import admin
from .models import User,Book,Emprunt

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = 'username', 'first_name', 'last_name', 'email', 'password'
    
class BookAdmin(admin.ModelAdmin):
    list_display = 'username', 'first_name', 'last_name', 'email', 'password'
    
class UserAdmin(admin.ModelAdmin):
    list_display = 'username', 'first_name', 'last_name', 'email', 'password'
    
class UserAdmin(admin.ModelAdmin):
    list_display = 'username', 'first_name', 'last_name', 'email', 'password'
    
admin.site.register(User,UserAdmin)
admin.site.register(Book,UserAdmin)
admin.site.register(Emprunt,UserAdmin)

