from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from pybo.services import retrieve_user_profile


def user_profile(request, user_id: int):
    limit = 10
    user = get_object_or_404(User, pk=user_id)

    profile = retrieve_user_profile(user, limit)
    context = {'profile': profile}

    return render(request, 'pybo/user_profile.html', context)
