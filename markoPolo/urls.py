from django.urls import path, include
from .views import ValuableList, ValuableDetail, UserList, UserDetail

urlpatterns = [
    path('valuables/', ValuableList.as_view()),
    path('valuables/<int:pk>/', ValuableDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]
