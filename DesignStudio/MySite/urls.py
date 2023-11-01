from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('user/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('user/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('user/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
