from django.db import models
import time

max_logged_in_time = 1 * 60 * 60 * 1000   # maximum time in milliseconds


class CustomUser(models.Model):
    GENDER_CHOICES = [('MALE', "Male"), ("FEMALE", "Female"), ("OTHER", "Other")]

    email_id = models.EmailField(primary_key=True, blank=False)
    first_name = models.CharField(blank=False, max_length=20)
    last_name = models.CharField(blank=False, max_length=20)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    phone_number = models.CharField(max_length=10, blank=False)

    last_successful_auth = models.CharField(blank=True, max_length=15)
    otp_random = models.CharField(blank=True, max_length=16)
    last_otp_generation = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = "email_id"
    EMAIL_FIELD = "email_id"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True


class CustomUserManager:
    '''
    CustomUserManager: Class used to interact with Custom User Model
    '''
    @staticmethod
    def get_user(email):
        """
        :param email: String type
        :return: CustomUser object if a valid user, else None
        """
        user = None
        try:
            user = CustomUser.objects.get(email_id=email)
        except CustomUser.DoesNotExist:
            user = None
        finally:
            return user

    @staticmethod
    def is_authenticated(email):
        '''
        :param email: String type
        :return: False, if User is logged out ( time is greater than maximum time i.e. 1 hr)
        '''
        result = False
        try:
            user = CustomUser.objects.get(email_id=email)
            last_login = int(user.last_successful_auth)
            if int(time.time()) - last_login > max_logged_in_time:
                result = False
            else:
                result = True
        except CustomUser.DoesNotExist:
            result = False
        except ValueError:
            result = False
        finally:
            return result


class Country(models.Model):
    Code = models.CharField(max_length=3, null=False, primary_key=True)
    Name = models.CharField(max_length=52, null=False, default='')
    continents = [('Asia', 'Asia'), ('Europe', 'Europe'), ('North America', 'North America'), ('Africa', 'Africa'), ('Oceania', 'Oceania'), ('Antarctica', 'Antarctica'), ('South America', 'South America')]
    Continent = models.CharField(choices=continents, default=continents[0], max_length=20)
    Region = models.CharField(max_length=26, null=False, default='')
    SurfaceArea = models.FloatField(default=0.00)
    IndepYear = models.SmallIntegerField(null=True, default=None)
    Population = models.IntegerField(null=False, default=0)
    LifeExpectancy = models.FloatField(null=True, default=None)
    GNP = models.FloatField(null=True, default=None)
    GNPOld = models.FloatField(null=True, default=None)
    LocalName = models.CharField(max_length=45, null=False, default='')
    GovernmentForm = models.CharField(max_length=45, null=False, default='')
    HeadOfState = models.CharField(max_length=60, null=True, default=None)
    Capital = models.IntegerField(null=True, default=None)
    Code2 = models.CharField(max_length=2, null=False, default='')


class City(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=35, null=False, default='')
    CountryCode = models.ForeignKey('Country', on_delete=models.CASCADE)
    District = models.CharField(max_length=20, null=False, default='')
    Population = models.IntegerField(null=False, default=0)


class CountryLanguage(models.Model):
    CountryCode = models.ForeignKey('Country', on_delete=models.CASCADE, primary_key=True)
    Language = models.CharField(max_length=30, null=False, default='')
    IsOfficial_Choices = [('T', 'T'), ('F', 'F')]
    IsOfficial = models.CharField(choices=IsOfficial_Choices, default=IsOfficial_Choices[1], max_length=2)
    Percentage = models.FloatField(null=False, default=0.0)

