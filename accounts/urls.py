from django.urls import path,re_path
from .views import LoginOrSignupView

app_name='accounts'

urlpatterns=[
    re_path(r'^$',LoginOrSignupView,name='login_or_signup_view'),
]