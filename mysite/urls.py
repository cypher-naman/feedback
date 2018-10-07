from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'mysite'
urlpatterns = [
    path('', views.feedback_form, name='form'),
    path('try_to_connect', views.try_to_connect),
    path('create', views.feedback_create, name='create'),
    # path(r'^detail/(?P<id>\d+)/$', views.feedback_detail),
    path('detail/<int:pk>/', views.feedback_detail , name='detail'),
    path('update/<int:pk>/', views.feedback_update, name='update'),
    path('delete/<int:pk>/', views.feedback_delete),
]
