from django.contrib import admin
from .models import User,Book,Emprunt

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = 'username', 'first_name', 'last_name', 'email', 'password'
    
class BookAdmin(admin.ModelAdmin):
    list_display = 'title', 'author', 'publisher', 'year', 'uploaded_by', 'desc',"nbr_copy"
    
class EmpruntAdmin(admin.ModelAdmin):
    list_display = 'book_id', 'user', 'date_prevu_depos', 'date_depos', 'amande_amount', 'amande_paid_amount'
     
admin.site.register(User,UserAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Emprunt,EmpruntAdmin)

