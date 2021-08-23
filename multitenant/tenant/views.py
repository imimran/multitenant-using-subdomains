from django.shortcuts import render
from .models import Member
from .utils import get_tenant

# Create your views here.

def our_team(request):
    tenant = get_tenant(request)
    members = Member.objects.filter(tenant=tenant)
    return render(request, 'tenant/our_team.html', {'tenant':tenant, 'members':members})
