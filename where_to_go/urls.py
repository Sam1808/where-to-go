from django.contrib import admin
from django.urls import path
from where_to_go import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_mainpage),
    path('places/<int:id>/', views.get_location),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
