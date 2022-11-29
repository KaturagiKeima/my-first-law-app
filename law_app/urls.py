from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name='home'),
    path('practice/', views.practice, name='practice'),
    path('practice_main/', views.practice_main, name='practice_main'),
    path("practice_answer/", views.practice_answer, name="practice_answer"),
    path("practice_end/", views.practice_end, name="practice_end"),
    path("production_start/", views.production_start, name="production_start"),
    path("production/", views.production, name="production"),
    path("production_answer/", views.production_answer, name="production_answer"),
    path("create_pdf/", views.create_pdf, name="create_pdf"),
    path("contact/", views.contact, name="contact"),
    path("<slug:slug>/", views.practice_question, name="practice_question"),
    
]