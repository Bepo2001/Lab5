from django.urls import path
from . import views
app_name="test"
urlpatterns = [
    path("", views.Default_path, name="Default"),
    path("add", views.add, name="add"),

]