from django.urls import path
from . import views

urlpatterns = [
    path('fitness/', views.fitness, name='fitness'),
    path('allenamenti/', views.allenamenti, name='allenamenti'),
    path("ollama/",views.ollama, name = "ollama"),
    path("workout/",views.workout, name = " workout"),
    path("index/", views.index, name = "index")
]