from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.forms import ModelForm
from bookstore.models import Chat, Book,Emprunt
from django import forms

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('message', )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publisher', 'year', 'uploaded_by', 'desc',"nbr_copy")        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
         
class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['book_id', 'user', 'date_prevu_depos', 'date_depos', 'amande_amount', 'amande_paid_amount']
