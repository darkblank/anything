from django.urls import path

from users.views import SignupView, SigninView

app_name = 'users'

urlpatterns = [
    path('', SignupView.as_view(), name='user_signup'),
    path('sign-in/', SigninView.as_view(), name='user_signin'),
]