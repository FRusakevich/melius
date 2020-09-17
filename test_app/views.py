from django.shortcuts import render
from .models import Zayavka, Contract, Tovar, Proizvoditel


# Create your views here.
def get_id(request, pk):
    contarct_id = Contract.objects.prefetch_related('rel_zayavka__rel_tovar__rel_proizdodotel').only('id').distinct().get(id=pk)
    return contarct_id
