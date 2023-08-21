from django.urls import path
from .import views 

urlpatterns = [
    path('',views.test,name="test"),
    path('regi/',views.regi,name="regi"),
    path('login/',views.login,name="login"),
    path("welcome/",views.welcome,name="welcome"),
    path('loginuser/',views.loginuser,name="login"),
    path('views/',views.view,name="views"),
    path('detailview/<str:pk>',views.detailview,name="detailview"),
    path("update/<str:pk>",views.update,name="update"),
    path("delete/<str:pk>",views.delete,name="delete"),
    path("adminlogin/",views.adminlogin,name="adminlogin"),
    path("adminloguser/",views.adminloguser,name="adminloguse")
]
