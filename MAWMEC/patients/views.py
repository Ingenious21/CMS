# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    user = request.user
    return render(request, 'patients/home.html', {'user':user})