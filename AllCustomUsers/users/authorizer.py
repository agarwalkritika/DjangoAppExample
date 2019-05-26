from .models import CustomUserManager
from django.shortcuts import redirect


def auth_required(func):
    '''
    Decorator to ensure that the user is logged in or not
    :param func:
    :return: Calling required function, if it satisfies 3 condition mentioned in code, otherwise redirecting to the login page
    '''
    def new_func(*args, **kwargs):
        if args:
            request = args[0]
        else:
            request = kwargs['request']
        if 'authenticated_email' in request.session:
            user = CustomUserManager.get_user(email=request.session['authenticated_email'])
            if user is not None and CustomUserManager.is_authenticated(email=user.email_id) is True:
                return func(*args, **kwargs)
        return redirect('login')
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    return new_func


def not_for_already_signed_users(func):
    def new_func(*args, **kwargs):
        if args:
            request = args[0]
        else:
            request = kwargs['request']
        if 'authenticated_email' in request.session:
            user =CustomUserManager.get_user(email=request.session['authenticated_email'])
            if user and CustomUserManager.is_authenticated(email=request.session['authenticated_email']) is True:
                print("This user must never be on this page. Redirect to home !!")
                return redirect('index')
        return func(*args, **kwargs)

    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    return new_func
