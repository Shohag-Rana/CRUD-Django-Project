from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name = "home"),
    path('update/<int:my_id>', views.update_data, name = "update"),
    path('<int:my_id>', views.delete_data, name = "delete"),
]