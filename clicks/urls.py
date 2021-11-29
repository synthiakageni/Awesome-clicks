from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
 path(r'',views.home, name='home'),
 path('category/', views.category, name='image-category'),
 path('category/', views.imageDetail, name='image-detail'),
 url(r'^search/', views.search_results, name='search_results'),
 url(r'^detail/(\d+)', views.detail, name="detail"),
 url(r'^description/(\d+)',views.description, name='description'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

