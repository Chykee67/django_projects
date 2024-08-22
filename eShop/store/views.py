from django.shortcuts import render

from login.models import User

def IndexView(request, user_name):

    user = User.objects.get(user_name=user_name)

    if user.user_name == 'chykee67':
        return render(request, 'store/admin_index.html')
    else:
        return render(request, 'store/user_index.html')
    
# Create your views here.
