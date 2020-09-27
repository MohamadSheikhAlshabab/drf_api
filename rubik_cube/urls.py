from django.urls import path
from .views import CubeList , CubeDetails

urlpatterns = [
    path('cube',CubeList.as_view(), name='cube_list'),
    path('cube/<int:pk>',CubeDetails.as_view(), name='cube_details'),
]