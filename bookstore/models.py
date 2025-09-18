from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse




#User = get_user_model()


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)


    class Meta:
        swappable = 'AUTH_USER_MODEL'
    def __str__(self):
            return self.username+" ("+self.email+")"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='bookapp/pdfs/')
    cover = models.ImageField(upload_to='bookapp/covers/', null=True, blank=True)
    nbr_copy = models.IntegerField(max_length=100,null=True,default=0)

    def __str__(self):
        return self.title+" (copies restant:"+str(self.nbr_copy)+")"

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)        

class Emprunt(models.Model):   # <-- il faut hériter de models.Model !
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_prevu_depos = models.DateTimeField(auto_now_add=False, null=True)
    date_depos = models.DateTimeField(auto_now_add=False, null=True)
    date_save = models.DateTimeField(auto_now_add=True, null=False)
    amande_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=0)
    amande_paid_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=0)

    def __str__(self):
        return f"{self.book_id} emprunté par {self.user}"
    
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.message)


class DeleteRequest(models.Model):
    delete_request = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.delete_request


class Feedback(models.Model):
    feedback = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.feedback












