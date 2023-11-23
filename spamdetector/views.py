from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account.models import Profile
from django.shortcuts import render
# Create your views here.
@login_required(login_url='login')
def spam_view(request):

    user_object = User.objects.get(username=request.user)
    user_profile = Profile.objects.get(user=user_object)

    context = {"user_profile": user_profile}
    return render(request,"spam.html", context)

# detector/views.py

