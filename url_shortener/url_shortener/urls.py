from django.contrib import admin
from django.urls import path
from shortener import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('admin/', admin.site.urls),
    path('shorten', views.ShortenURLView.as_view(), name='shorten'),
    path('shorten/<str:short_code>', views.URLDetailView.as_view(), name='retrieve'),
    path('shorten/<str:short_code>/update', views.URLDetailView.as_view(), name='update'),
    path('shorten/<str:short_code>/delete', views.URLDetailView.as_view(), name='delete'),
    path('shorten/<str:short_code>/stats', views.URLStatsView.as_view(), name='stats'),
]