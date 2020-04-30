from django.shortcuts import render, redirect
from . models import UserManager, User, CompanyManager, Company, Industrial_Material
from django.contrib import messages
import bcrypt

    # What functions do we want?
    # Allow Companys to see data on a list and visually on a map
    # Create a funtion to add materials from them and their own location onto the map.
    # Create a function to show the routing options if they were to request a material 

def index(request):
    context={
        "companies" : Company.objects.all()
    }
    if "user_id" in request.session:
        return redirect("/dashboard_map")
    else:
        return render(request,"index.html",context)

def process_user(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0:
        for key, error_msg in errors.items():
            messages.error(request, error_msg)
        return redirect('/')
    else:
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()         
        new_user = User.objects.create(name=name, email=email, password=pw_hash)
        request.session["user_id"] = new_user.id
        return redirect("/dashboard_map")

# this is the processing for the registration and login
def process_registration(request):
    errors = Company.objects.company_validator(request.POST)
    if len(errors) > 0:
        for key, error_msg in errors.items():
            messages.error(request, error_msg)
        # return redirect('/')
    else:
        name = request.POST ["name"]
        request.session['name']= name
        email = request.POST ["email"]
        password = request.POST ["password"]
        pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()         
        new_company = Company.objects.create(name=name, email=email, password=pw_hash)
        request.session["company_id"] = new_company.id
        # messages.dashboard(request,"You have been successfully registered!")
        return redirect("/")

def user_login(request):
    if "user_id" not in request.session:
        return redirect("/")
    else:
        return redirect("/dashboard_map")

def process_login(request):
    # if "company_id" not in request.session:
    #     return redirect("/")

    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, error_msg in errors.items():
            messages.error(request, error_msg)
        return redirect("/")
<<<<<<< HEAD
    login_company_list = Company.objects.filter(email=request.POST['email'])
    logged_in_company = login_company_list[0]
    request.session["name"] = logged_in_company.name
    request.session["company_id"] = logged_in_company.id
    request.session["company_name"] = logged_in_company.name
=======
    users_filtered = User.objects.filter(email=request.POST['email'])
    curr_user = users_filtered[0]
    request.session["user_id"] = curr_user.id
>>>>>>> 5601ded78f551f9fdf55c2d839ca8d5480333129
    return redirect("/dashboard_map")
    
# this processes the logout button and renders the resgistration and login page
# def logout(request):
#     request.session.clear()  
#     return redirect('/')

# this creates a list of materials that our Company has chosen
def dashboard_map(request):
    if 'user_id' not in request.session:
        return redirect("/")
<<<<<<< HEAD
        all_materials=Industrial_Material.objects.all()
        new_list=[]
    this_user = User.objects.get(id=request.session['user_id'])
    # for material in all_materials:
    #     if material not in this_company.material_source.all():
    #         new_list.append(material)
    # context = {
    #     "this_company" : this_company,
    #     "filtered_list" : new_list,
    #     "all_materials" : all_materials
    # }
    return render(request,"dashboard_map.html")
=======
    
    all_materials = Industrial_Material.objects.all()

    context = {
        "all_materials" : all_materials
    }
    return render(request,"dashboard_map.html", context)
>>>>>>> 5601ded78f551f9fdf55c2d839ca8d5480333129
    
def new_company(request):
    return render(request,"new_company.html")

# this renders the new page where you would add a material    
def new_material(request):
    context = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    
    return render(request,"new_material.html",context)

def add_company(request):
    errors = Company.objects.company_validator(request.POST)
    if len(errors) > 0:
        for key, error_msg in errors.items():
            messages.error(request, error_msg)
        return redirect('/')
    else:
        name = request.POST ["name"]
        street_address_1 = request.POST ["street_address_1"]
        street_address_2 = request.POST ["street_address_2"]
        city = request.POST ["city"]
        state = request.POST ["state"]
        zip_code = request.POST ["zip_code"]
        phone = request.POST ["phone"]
        email = request.POST ["email"]
        password = request.POST ["password"]
        pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()         
        new_company = Company.objects.create(name=name, street_address_1=street_address_1, street_address_2=street_address_2, city=city, state=state, zip_code=zip_code, phone=phone, email=email, password=pw_hash)
        # request.session["company_id"] = new_company.id
        return redirect("/dashboard_map")

# def process_user(request):
#     errors = User.objects.user_validator(request.POST)
#     if len(errors) > 0:
#         for key, error_msg in errors.items():
#             messages.error(request, error_msg)
#         return redirect('/')
#     else:
#         name = request.POST["name"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#         pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()         
#         new_user = User.objects.create(name=name, email=email, password=pw_hash)
#         request.session["user_id"] = new_user.id
#         return redirect("/dashboard_map")

# this the the create material processing
def add_material(request):
    if 'user_id' not in request.session:
        return redirect('/')
    errors = Industrial_Material.objects.material_validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect("/new_material")
    material_name = request.POST["material_name"]
    # company = Company.objects.get(name=request.POST["material_source"])
    # material_source = company
    # material_source = request.POST["material_source"]
    description = request.POST["description"]
    transport = request.POST["transport"]
    new_material = Industrial_Material.objects.create(material_name=material_name, description=description, transport_method=transport)
    # new_material.save()
    return redirect("/dashboard_map")

# def add_material(request, industrial_material_id, company_id):
#     this_material=Industrial_Material.objects.get(id=industrial_material_id)
#     this_material.material_source = Company.objects.get(id=company_id)
#     this_material.save()
#     return redirect("/dashboard_map")

# this renders the material_info page
def material_info(request, industrial_material_id):
    this_material = Industrial_Material.objects.get(id=industrial_material_id)
    context = {
        'material' : this_material
    }
    return render(request,"material_info.html", context)
        
# this renders edit material page
def edit(request, industrial_material_id):
    context ={
        "material" : Industrial_Material.objects.get(id=industrial_material_id),
        "user" : User.objects.get(id=request.session['user_id'])
    }
    return render(request,"edit_material.html", context)

# this is the processing for the edit material button
def edit_material(request, material_id):
    if 'user_id' not in request.session:
        return redirect('/')
    edit_material = Industrial_Material.objects.get(id=material_id)
    errors = Industrial_Material.objects.material_validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect(f'/edit/{material_id}')
    edit_material.title = request.POST["title"]
    edit_material.description = request.POST["description"]
    edit_material.location = request.POST["location"]
    edit_material.save()
    return redirect("/dashboard_map")

def delete_material(request, industrial_material_id):
    if 'user_id' not in request.session:
        return redirect('/')
    delete_material = Industrial_Material.objects.get(id=industrial_material_id)
    delete_material.delete()
    return redirect("/dashboard_map")


def cancel_material(request, industrial_material_id, Company_id):
    remove_this_one = Industrial_Material.objects.get(id=industrial_material_id)
    this_company = Company.objects.get(id=Company_id)
    this_company.material_source = Industrial_Material.objects.remove(remove_this_one)
    remove_this_one.save()
    return redirect("/dashboard_map")

