from django.urls import path

from users import views
from users.views import SignUpView

urlpatterns = [
    # each is accessed through /users/signup or update_profile
    path('update_profile/<int:user_id>/', views.update_profile, name="update_profile"),
    path('signup', SignUpView.as_view(), name="signup"),
]
