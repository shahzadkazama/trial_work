from django.contrib.auth.decorators import login_required
from django.urls import path
from trial import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('trail/add_car/', views.add_car, name='add_car'),
    path('trail/del_car/', views.del_car, name='del_car'),
    path('trail/find_car/', views.find_car, name='find_car'),
    path('trail/update_car/', views.update_car, name='update_car'),

]
