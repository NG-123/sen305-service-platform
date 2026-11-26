from django.contrib import admin
from django.urls import include, path

from . import views

app_patterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include((app_patterns, "core"), namespace="core")),
    path("contact/", views.contact, name="contact"),
    path("workflow/", views.workflow, name="workflow"),
]
