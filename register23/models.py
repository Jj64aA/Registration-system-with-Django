from django.db import models

# Create your models here.


class Member_Records(models.Model):
   f_name = models.CharField(max_length=190, null=True)
   u_number = models.CharField(max_length=190, null=True)
   code_hash = models.CharField(max_length=190, null=True)
   p_number= models.CharField(max_length=190, null=True)
   email = models.CharField(max_length=190, null=True)
   date_created =models.CharField(max_length=190, null=True)
   u_major = models.CharField(max_length=190, null=True)
   date_b = models.CharField(max_length=190, null=True)
   def __str__(self):
        return self.f_name