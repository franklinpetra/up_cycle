from django.urls import path
from . import views
import datetime
import bcrypt
import re

urlpatterns = [
    path('', views.index),
    path("process_user", views.process_user),
    path("process_registration", views.process_registration),
    path("process_login", views.process_login),
    path("dashboard_map", views.dashboard_map),
    path("new_material", views.new_material),
    path("add_company", views.new_material),
    path("new_company", views.new_company),
    path("material_info/<int:industrial_material_id>/<int:company_id>", views.material_info),
    path("edit/<int:industrial_material_id>", views.edit),
    path("edit_material/<int:material_id>", views.edit_material),
    path("delete_material/<industrial_material_id>", views.delete_material),
    path("add_material", views.add_material),
    path("cancel_material/<int:industrial_material_id>/<int:company_id>", views.cancel_material),
]