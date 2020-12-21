from django.urls import path
from .views import CreateUser,LoginUser

user = CreateUser.as_view({
    'get' : 'list',
    'post':'create'
})
user1 = CreateUser.as_view({
    'get':'retrieve',
    'delete':'destroy'
})

urlpatterns = [
    path('createUser/',user),
    path('createUser/<int:pk>',user1),
    path('loginUser/',LoginUser.as_view())
]