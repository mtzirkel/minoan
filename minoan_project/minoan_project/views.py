from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth.models import User
from quiz.admin import Profile


def home(request):
	if request.user.get_profile().role == 2:
		return render(request, 'teacher_home.html')
	elif request.user.get_profile().role == 1:
		return render(request, 'student_home.html')
	else:
		return render(request, 'superuser_home.html')	