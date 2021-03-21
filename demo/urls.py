from django.urls import path

from demo.views import UserView, user_view

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('fbv/users/', user_view, name='fbv-users')
]

