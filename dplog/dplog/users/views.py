from django.shortcuts import render
from users.models import Profile


def profile(request, profile_name):
    user_profile = Profile.objects.get(user__username=profile_name)
    return render(
        request,
        'users/profile.html',
        context={'profile': user_profile}
    )