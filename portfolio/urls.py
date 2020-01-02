from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('contact/', views.ContactInfoView.as_view(), name='contact'),

    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail'),
]