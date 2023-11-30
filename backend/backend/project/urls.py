from django.contrib import admin
from django.urls import path, include
from app.views import list_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
