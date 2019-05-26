from django.urls import path
from .views import signup, login, logout, index, country

urlpatterns = [
    path('auth/signup/', signup, name='signup'),
    path('auth/login/', login, name='login'),
    path('auth/logout/', logout, name='logout'),
    path('', index, name='index'),
    path('country/<str:country_code>', country, name='country')
    # str:country_code: Whatever you are writing after 'country/' in the url, it will take that as country code
]