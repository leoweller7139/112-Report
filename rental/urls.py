from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.push, name='push'),
    # path('<int:movie_id', views.details, name='movies_detail'),
    path('home', views.index, name='home'),
    # path('developer', views.developer, name='devName'),
    path('catalog', views.catalog, name='catalog'),
    path('details/<int:movie_id>', views.details, name='details'),
]