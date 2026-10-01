from django.contrib import admin
from django.urls import path
from to_do_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.interface, name="view"),
    path("add/", views.Add, name="add"),
    path("action/<int:id_task>/", views.action, name="action")
]
