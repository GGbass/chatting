from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include ('contact.urls')),
    path('task/', include ('task.urls'))
]
