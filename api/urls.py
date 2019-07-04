from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ListSpaceCraft.as_view()),
    path('<int:pk>/', views.DetailSpaceCraft.as_view()),
    path('rest-auth/', include('rest_auth.urls'))
]