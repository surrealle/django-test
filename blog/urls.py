from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='details'),
]

urlpatterns += static(settings.MEDIA_URL, 
                        document_root=settings.MEDIA_ROOT)