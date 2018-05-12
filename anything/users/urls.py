from django.urls import path

from users.views import SignupView

app_name = 'users'

urlpatterns = [
    path('', SignupView.as_view(), name='user_signup'),
]