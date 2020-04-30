from django.db import models
import datetime
import bcrypt
import re

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
            errors['no_email'] = "Gosh. No emails match yours. Have you registered?"
        return errors
        
    def user_validator (self, formData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')           
        if len(formData['name']) == 0:
            errors['name'] = "Please enter a name."
        if len(formData['name']) < 2:
            errors['name'] = "Could you please submit a name longer than 2 characters."
        if not EMAIL_REGEX.match(formData['email']):   
            errors['email'] = "Well Gollie! Invalid format for your email address. We need bla bla bla @ bla bla. bla!"
        some_user = User.objects.filter(email=formData['email'])
        if len(some_user) == 1:
            errors['email'] = "Oh My! Appears that your email has been used by a previous account, please supply a spanking new email."
        if len(formData['password']) < 8:
            errors['pass_length'] = "Please give us a password that is at least 8 characters long!"
        if formData['password'] != formData["confirm"]:
            errors['pass_confirm'] = "Gosh. Looks like your passwords do not match. Please check for typos."
        return errors

class CompanyManager (models.Manager):
    def login_validator(self,formData):
        errors = {}
        company = Company.objects.filter(email=formData['email'])
        if company:
            our_company = company[0]
            if bcrypt.checkpw(formData['password'].encode(), our_company.password.encode()):
                print("Password matches!")
                return errors
            else:
                errors['no_pass'] = "Incorrect password. Typos perhaps?"
        else:
            errors['no email'] = "Gosh. No emails match yours. Have you registered?"
        return errors

    def company_validator (self, formData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')           
        if len(formData['name']) == 0:
            errors['name'] = "Please answer every question. Need something in each field."
        if len(formData['name']) < 2:
            errors['name'] = "Can you please submit a name longer than 2 characters."
        if not EMAIL_REGEX.match(formData['email']):   
            errors['email'] = "Well Gollie! Invalid format for your email address. We need bla bla bla @ bla bla. bla!"
        some_company = Company.objects.filter(email=formData['email'])
        if len(some_company) == 1:
            errors['email'] = "Oh My! Appears that your email has been used by a previous account, please supply a spanking new email."
        if len(formData['password']) < 4:
            errors['pass_length'] = "Please give us a password that is at least 8 characters long!"
        if formData['password'] != formData["confirm"]:
            errors['pass_confirm'] = "Gosh. Looks like your passwords do not match. Please check for typos."
        return errors

    def material_validator (self, formData):
        errors = {}           
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
class User(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    objects=UserManager()

class Company(models.Model):
    name=models.CharField(max_length=255)
    street_address_1=models.CharField(max_length=255)
    street_address_2=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    zip_code=models.IntegerField()
    material=models.CharField(max_length=255)  
    phone=models.IntegerField()
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CompanyManager()

class Industrial_Material(models.Model):
    material_name=models.CharField(max_length=255)
    material_source=models.ManyToManyField(Company, related_name="material_connection", blank =True, null=True)
    description=models.CharField(max_length=255)
    transport_method=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CompanyManager()
        #related name is material_connection

# Company.objects.all().values()
# <QuerySet [{'id': 1, 'name': 'LeHigh Cement', 'street_address_1': '5225 E. Marginal Way South', 'street_address_2': '1st Floor', 'city': 'Seattle', 'state': 'WA', 'zip_code': 98134, 'material': 'Grey Water', 'phone': 2067632525, 'email': 'jim@lehigh.com', 'password': 'Jim4489', 'created_at': datetime.datetime(2020, 4, 30, 5, 23, 32, 27834, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 4, 30, 5, 23, 32, 27872, tzinfo=<UTC>)}, {'id': 2, 'name': 'Ash Grove Cement', 'street_address_1': '3801 E. Marginal Way S', 'street_address_2': 'Blg 5', 'city': 'Seattle', 'state': 'WA', 'zip_code': 98134, 'material': 'cement crumble', 'phone': 2066235596, 'email': 'noel@ashgrove.com', 'password': 'Noel4489', 'created_at': datetime.datetime(2020, 4, 30, 5, 26, 38, 443500, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 4, 30, 5, 26, 38, 443525, tzinfo=<UTC>)}, {'id': 3, 'name': 'Puget Sound Energy', 'street_address_1': '6500 Ursula Pl S', 'street_address_2': 'Terminal Building', 'city': 'Seattle', 'state': 'WA', 'zip_code': 98108, 'material': 'glass grit', 'phone': 2062255773, 'email': 'laverne@pge.com', 'password': 'Laverne4489', 'created_at': datetime.datetime(2020, 4, 30, 5, 29, 52, 690121, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 4, 30, 5, 29, 52, 690149, tzinfo=<UTC>)}, {'id': 4, 'name': 'Kimberly Clark', 'street_address_1': '22001 84th Ave S', 'street_address_2': 'The Landing', 'city': 'Seattle', 'state': 'WA', 'zip_code': 98032, 'material': 'paper pulp', 'phone': 2528727537, 'email': 'joshua@kc.com', 'password': 'Joshua4489', 'created_at': datetime.datetime(2020, 4, 30, 5, 34, 18, 735501, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 4, 30, 5, 34, 18, 735528, tzinfo=<UTC>)}, {'id': 5, 'name': 'Lakeside Industries, Inc', 'street_address_1': '309 NW 39th St', 'street_address_2': 'Pier 3', 'city': 'Seattle', 'state': 'WA', 'zip_code': 98107, 'material': 'clean grit', 'phone': 4253132600, 'email': 'calder@lakeside.com', 'password': 'Calder4489', 'created_at': datetime.datetime(2020, 4, 30, 5, 39, 17, 508065, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 4, 30, 5, 39, 17, 508101, tzinfo=<UTC>)}]>
# >>> 