from django.db import models
import datetime
import bcrypt
import re
import localflavor
from __future__ import absolute_import, unicode_literals
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import Field, RegexField, Select, CharField
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _


# we could add this as a the phone number validation # phone_digits_re = re.compile(r'^(?:1-?)?(\d{3})[-\.]?(\d{3})[-\.]?(\d{4})$')


# Our validations are here.


class UserManager (models.Manager):
    def login_validator(self,formData):
        errors = {}
        user = User.objects.filter(email=formData['email'])
        if user:
            our_user = user[0]
            if bcrypt.checkpw(formData['password'].encode(), our_user.password.encode()):
                print("Password matches!")
                return errors
            else:
                errors['no_pass'] = "Incorrect password. Typos perhaps?"
        else:
            errors['no email'] = "Gosh. No emails match your query."
        return errors

    def user_validator (self, formData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')           
        if len(formData['first']) < 0:
            errors['first'] = "Please answer every question. Need something in each field."
        if len(formData['last']) < 2:
            errors['last'] = "Can you please submit a name longer than 2 characters."
        if not EMAIL_REGEX.match(formData['email']):   
            errors['email'] = "Well Gollie! Invalid format for your email address. We need bla bla bla @ bla bla. bla!"
        some_user = User.objects.filter(email=formData['email'])
        if len(some_user)>0:
            errors['email'] = "Oh My! Appears that your email has been used by a previous account, please supply a spanking new email."
        if len(formData['password']) < 4:
            errors['pass_length'] = "Please give us a password that is at least 8 characters long!"
        if formData['password'] != formData["confirm"]:
            errors['pass_confirm'] = "Gosh. Looks like your passwords do not match. Please check for typos."
        return errors

    def material_validator (self, formData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')           
        if len(formData['material_name']) == 0:
            errors['material_name'] = "What exactly is this material? We need a name. Each field must be filled."
        if len(formData['material_name']) < 3:
            errors['material_name'] = "Can you please submit a name longer than 3 characters." 
        if len(formData['description']) == 0:
            errors['description'] = "How would you describe this material? Need something in each field."
        if len(formData['description']) < 3:
            errors['description'] = "Can you please add details and submit a description longer than 3 characters." 
        return errors

# Our Models are here.

class Company(models.Model):
    name=models.Charfield(max_length=255)
    street_address=models.Charfield(max_length=255)
    city=models.Charfield(max_length=255)
    state=models.Charfield(max_length=255)
    zip_code=models.IntegerField()
    by_product=models.ManyToManyField(Industrial_By_Product, related_name="valuable_material")
    material=models.ManyToManyField(Industrial_Material, related_name="material_user")  
    phone=models.IntegerField()
    email=models.Charfield(max_length=255)
    password=models.Charfield(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager() 
    # related_name = material_desired (for Industrial_By_Product)
    # related_name = from_company (for Industrial_Material)

class Industrial_Material(models.Model):
    material_name=models.CharField(max_length=255)
    uses=models.CharField(max_length=255)
    traditional_source=models.CharField(max_length=255)
    sourced_as_by_product=models.ForeignKey(Industrial_By_Product, related_name="from_company",on_delete=models.CASCADE)
    quantity=models.IntegerField()
    description=models.TextField()
    average_cost=models.IntegerField()
    transport_method=models.CharField(max_length=255)  truck, train, tanker
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager() 
    # related_name = valuable material

class Industrial_By_Product(models.Model):
    material=models.CharField(max_length=255)
    uses=models.CharField(max_length=255)
    company_producing_by_product=models.ManyToManyField(Industrial_Material, related_name="material_desired")  
    quantity=models.CharField(max_length=255)
    quality=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.IntegerField()
    transport_method=models.CharField(max_length=255) truck, train, tanker
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager() 
      #related name is material_creater