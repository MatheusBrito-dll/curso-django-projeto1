from django.urls import path
from recipes.views import home, teste

urlpatterns = [
    path('', home),
    path('teste', teste),
]
