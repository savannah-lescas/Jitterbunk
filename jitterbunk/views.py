from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .forms import BunkForm 
import logging

from .models import User, Bunk

logger = logging.getLogger(__name__)

def index(request):
    all_bunks = Bunk.objects.order_by('-time')
    users = User.objects.all()
    context = {
        'all_bunks': all_bunks,
        'users': users
    }
    return render(request, 'jitterbunk/index.html', context)

def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    user_bunks = Bunk.objects.filter(from_user=user).order_by('-time')
    return render(request, 'jitterbunk/user_detail.html', {'user': user, 'user_bunks': user_bunks})

def submit_bunk(request):
    if request.method == 'POST':
        form = BunkForm(request.POST)
        if form.is_valid():
            logger.debug("form is valid")
            form.save()
            return redirect('index')
        else:
            logger.debug(f"Form errors: {form.errors}")
            for field, errors in form.errors.items():
                logger.debug(f"Error in {field}: {errors}")
    else:
        form = BunkForm()
    return render(request, 'jitterbunk/bunker.html', {'form': form})