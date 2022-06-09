from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from .forms import *

from ..accounts import forms, models
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from ..accounts.models import *
# from .forms import LoginForm, RegisterForm,comment_form

# Create your views here.




