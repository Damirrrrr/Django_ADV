from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("", index),
    path("create/", create),
    path("delete/<int:id>", delete),
    path("edit/<int:id>", edit),
]