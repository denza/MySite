from django.urls import path
from django.conf.urls import url
from . import views

app_name = "postovi"

urlpatterns = [
    #/postovi/
    path('', views.IndexView.as_view(), name = "index"),
    #/postovi/1
    path('<pk>', views.DetailView.as_view(), name = "detail"),
    #/postovi/post/add
    path('post/add', views.QuestionCreate.as_view(), name = "create"),
    #/postovi/update
    path('update/<pk>', views.QuestionUpdate.as_view(), name = "update"),
    #/postovi/delete
    path('delete/<pk>', views.QuestionDelete.as_view(), name = "delete"),
]