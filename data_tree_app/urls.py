from django.urls import path
from data_tree_app import views

appurls = [
    path('', views.file_view, name='home'),
    path('create_file/', views.form_view),
    path('create_file/submit_form/', views.form_submit)
]