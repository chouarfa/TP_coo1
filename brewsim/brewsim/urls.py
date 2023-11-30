"""
URL configuration for brewsim project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from high_level import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "departement/<int:pk>",
        views.DepartementDetailView.as_view(),
        name="departement",
    ),

    path(
        "departement/<int:pk>",
        views.DepartementApiDetailView.as_view(),
        name="departement",
    ),
    path(
        "ingredient/<int:pk>",
        views.IngredientDetailView.as_view(),
        name="ingredient",
    ),
    path(
        "quantite/<int:pk>",
        views.QuantiteIngredientDetailView.as_view(),
        name="quantite",
    ),
    path(
        "usine/<int:pk>",
        views.UsineDetailView.as_view(),
        name="Usine",
    ),
    path(
        "prix/<int:pk>",
        views.DepartementDetailView.as_view(),
        name="departement",
    ),
    path(
        "recette/<int:pk>",
        views.IngredientDetailView.as_view(),
        name="ingredient",
    ),
    path(
        "action/<int:pk>",
        views.QuantiteIngredientDetailView.as_view(),
        name="quantite",
    ),
    path(
        "machine/<int:pk>",
        views.UsineDetailView.as_view(),
        name="Usine",
    ),
]
