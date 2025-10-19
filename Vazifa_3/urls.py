
from django.contrib import admin
from django.urls import path
from vazifa_3_app.views import vazifa3

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", vazifa3)
]
