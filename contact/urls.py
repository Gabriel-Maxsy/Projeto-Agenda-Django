from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    
    # Contact (CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'), # Read
    path('contact/create/', views.create, name='create'), # Create
    path('contact/<int:contact_id>/update', views.update, name='update'), # Update
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'), # Delete

    # User
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
]