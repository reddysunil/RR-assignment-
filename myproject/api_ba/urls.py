from django.urls import path
from .views import user_list,register,LoginAPI
from knox import views as knox_views


urlpatterns = [
    path('user/', user_list),
    path('register/', register.as_view(),name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]