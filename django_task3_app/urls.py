from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('login/',views.login, name="login"),
    path('success/',views.success, name="success"),
    path('signup/',views.signup, name="signup"),
    path('createblog/', views.createblog, name="createblog"),
    path('delete/<int:id>', views.deleteUser, name='deleteblog'),
    path('createblog/<int:id>', views.createblog, name='updateblog'),
    path("logout", views.logout_request, name="logout"),
]