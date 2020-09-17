from django.urls import path
from .views import get_id

urlpatterns = [
    path('contract_ids/<int:pk>/', get_id, name='conracts_data')

]

