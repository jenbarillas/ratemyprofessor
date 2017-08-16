from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import registration.signals

# Create your views here.
def homepage(request):
	return render(request, 'webapp/homepage.html')

@login_required
def profilePage(request):
	'''
	Firstname=''
	Lastname=''
	Career=''
	'''
	return render(request, 'webapp/profile.html')

@login_required
def searchPage(request):
	return render(request, 'webapp/search.html')

@login_required
def professorSearchPage(request):
	return render(request, 'webapp/professorSearch.html')

@login_required
def courseSearchPage(request):
	return render(request, 'webapp/courseSearch.html')

@login_required
def loginTest(request):
	return HttpResponse("You shouldnt see this.")

#Signals
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")

@receiver(registration.signals.user_registered)
def userRegistered(sender, user, request, **kwargs):
	#Create entry in users table
	print "A new user registered, with id:"+str(user.id)+" username:"+str(user.username)+" email:"+str(user.email)