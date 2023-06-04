from django.urls import path

from . import views

#Create your URL

app_name = 'posts'

urlpatterns = [
    path('home/', views.HomeList.as_view(), name='home'),
    path('create_article/', views.CreateArticle.as_view(), name="create-article"),
    path('detail/<str:slug>/', views.DetailArticle.as_view(), name='detail'),
    path('update-article/<str:slug>/', views.UpdateArticle.as_view(), name='update-article'),
    path('delete-article/<str:slug>/', views.DeleteArticle.as_view(), name='delete-article'),

]
