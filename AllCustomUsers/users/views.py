from django.shortcuts import render, redirect
from django.core import serializers
import logging
import json

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .otp_handler import *
from .forms import LoginForm, CustomUserForm, SearchBar
from .exceptions import *
from .models import CustomUser, CustomUserManager, Country, City
from .authorizer import auth_required, not_for_already_signed_users


@not_for_already_signed_users
def signup(request):
    context = {}
    try:
        if request.method == 'GET':
            form = CustomUserForm()
            context['form'] = form
        elif request.method == 'POST':
            form = CustomUserForm(request.POST)
            context['form'] = form
            if form.is_valid() is not True:
                context['error'] = "Invalid request !!"
                raise InvalidRequestException
            user = form.save()
            return redirect('login')
    except InvalidRequestException as ex:
        pass
    return render(request=request, template_name='signup.html', context=context)


@not_for_already_signed_users
def login(request):
    context = {}
    try:
        if request.method == 'GET':
            form = LoginForm()
            context['form'] = form
        elif request.method == 'POST':
            form = LoginForm(request.POST)
            context['form'] = form
            if not form.is_valid():
                raise InvalidRequestException
            form_data = form.cleaned_data
            if not ('email' in form_data and form_data['email']):
                raise InvalidRequestException
            print("Checking if user is valid.")
            user = CustomUserManager().get_user(email=form_data['email'])
            if user is None:
                print("Invalid User !!")
                raise UserNotFoundException
            print("User is valid")
            if form_data['otp']:
                print("Checking if you have sent a valid OTP")
                res = validate_otp(user=user, otp=form_data['otp'])
                if res is True:
                    print("Authenticated !!! You shall now be redirected to the home page")
                    request.session['authenticated_email'] = form_data['email']
                    return redirect('index')
                else:
                    print("Failed. Incorrect OTP")
                    raise InvalidOTPException
            else:
                # generate otp
                print("Since OTP is not present, generating OTP.")
                res, message = send_otp(user=user)
                context['error'] = message
    except InvalidRequestException:
        context['error'] = "Invalid Request !!"
    except UserNotFoundException:
        context['error'] = "Invalid User !!"
    except InvalidOTPException:
        context['error'] = "Invalid OTP !!"
    return render(request=request, template_name='login.html', context=context)


def logout(request):
    try:
        if request.session['authenticated_email']:
            user = CustomUserManager.get_user(email=request.session['authenticated_email'])
            user.last_successful_auth = 0
            user.last_otp_generation = 0
            del request.session['authenticated_email']
    except Exception as ex:
        raise ex
    finally:
        # He has never logged in. Redirect to login page
        form = LoginForm()
        return redirect('login')


@auth_required
def index(request):
    context = {}
    try:
        if request.method == "GET":
            form = SearchBar()
            context['form'] = form
        if request.method == "POST":
            form = SearchBar(request.POST)
            context['form'] = form
            if not form.is_valid():
                raise InvalidRequestException
            form_data = form.cleaned_data
            res_country = Country.objects.filter(Name__startswith=form_data['search_string'])
            res_city = City.objects.filter(Name__startswith=form_data['search_string'])
            context['res_country'] = res_country
            context['res_city'] = res_city
    except InvalidRequestException:
        context['error'] = "Invalid Request !!"
    return render(request=request, template_name='index.html', context=context)


@auth_required
def country(request, country_code):
    context = {}
    try:
        country = Country.objects.get(Code=country_code)
        context['country'] = country
    except Country.DoesNotExist:
        context['error'] = "Country Does not Exist"
    return render(request=request, template_name='country.html', context=context)
