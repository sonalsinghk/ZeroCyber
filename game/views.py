from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account.models import Profile
# Create your views here.
@login_required(login_url='login')
def game_view(request):

    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)

    context = {"user_profile": user_profile}
    return render(request,"gamezone.html", context)
