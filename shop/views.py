from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from hashlib import sha512

from .forms import CustomUserCreationForm

# Python debugger
import pdb
from pprint import pprint

# Create your views here.
def index(request):
	return render(request, 'home.html', {})

def profile_view(request):
	return render(request, 'profile/view.html', {})

def register_view(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			
			# Generate the hash for account activation
			activationHash = _generate_activation_hash(user.id, user.email, user.date_joined)

			# URL to email
			url = request.build_absolute_uri(reverse('shop:activate', args = [str(user.id), str(activationHash)]))

			send_mail('User Activation', 'User Activation Message: ' + url, 'django@localhost', [user.email])
			return redirect('shop:index')

	return render(request, 'auth/register.html', { 'form': CustomUserCreationForm() })

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				messages.success(request, 'You were successfully logged in.')
				return redirect('index')
			else:
				messages.error(request, 'Your account is currently disabled.')
		else:
			messages.error(request, 'Login failed, please check your credentials and try again.')

	return render(request, 'auth/login.html', { 'form': AuthenticationForm() })

def logout_view(request):
	logout(request)
	return redirect('shop:index')

def activation_view(request, id, hash):
	user = get_object_or_404(User, pk=id)

	activationHash = _generate_activation_hash(user.id, user.email, user.date_joined)
	if hash and activationHash and hash != activationHash:
		return render(request, 'auth/activate.html', {'result': 'Failure'})

	user.is_active = True
	user.save()
	return render(request, 'auth/activate.html', {'result': 'Success'})

def _generate_activation_hash(id, email, datetime):
	hash_object = sha512((str(id) + email + datetime.strftime('%d/%m/%Y %H:%M:%S')).encode('utf-8'))
	return hash_object.hexdigest()