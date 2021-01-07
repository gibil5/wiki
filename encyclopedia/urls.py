"""
Module Url
    Created:    28 dec 2020
    Last up:     4 Jan 2021
"""
from django.urls import path
from . import views

# Routing
urlpatterns = [
    path("", views.index, name="index"),
    #path("wiki/css/", views.css, name="css"),
    path('wiki/<str:page>/', views.wiki, name="wiki"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("edit/<str:page>/", views.edit, name="edit"),
    #path("update/", views.edit, name="update"),
    #path("update/<str:page>/", views.update, name="update"),
    path("update/", views.update, name="update"),
]
