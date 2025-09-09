from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("entries.urls"))
]

admin.site.site_header = "LogBook Admin"
admin.site.site_title = "LogBook Admin"
admin.site.index_title = "Welcome to LogBook Admin"