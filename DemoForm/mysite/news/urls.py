
from django.urls import  path
from . import views
app_name = "news"
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('save_news/', views.save_news, name='save_news'),
    path('email_views/', views.email_view, name='email_views'),
    path('process_email/', views.process_email, name='process_email')
]   