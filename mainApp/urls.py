from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('report/', views.report, name='report'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('report/<int:pk>', views.detail, name='detail'),
    path('search', views.search, name='search'),
     # comment
    path('create_comment/<int:pk>', views.create_comment, name="create_comment"),
    path('delete_comment/<int:room_pk>/<int:comment_pk>/', views.delete_comment, name="delete_comment"),
    # login
    path('accounts/', include('allauth.urls')),
    # Mypage
    # path('mypage/', views.mypage, name='mypage'),
]