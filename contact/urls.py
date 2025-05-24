# type:ignore
from django.urls import path
from contact.views import user_forms

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),

    # contact (CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contact/create/', views.create, name='create'),


    
    #user
    path('user/create/', user_forms.register, name='register'),
    path('user/login/', user_forms.login_view, name='login'),
    path('user/logout/', user_forms.logout_view, name='logout'),
    path('user/update/', user_forms.user_update, name='user_update'),
    
    
    

]