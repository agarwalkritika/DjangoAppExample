from .models import CustomUser
import pyotp
import time

otp_validity_seconds = 80
regenerate_otp_seconds = otp_validity_seconds/2


def publish_otp(user, otp):
    print("Sending OTP {} to email address {}".format(otp, user.email_id))


def send_otp(user):
    """
    :param user: CustomUser object
    :return:
    # if an otp has been sent recently, don' t send the otp again. Return True
    # else generate and send a new OTP
    """
    time_now = int(time.time())
    if user.last_otp_generation and time_now - int(user.last_otp_generation) <= regenerate_otp_seconds:
        return True, "OTP is already generated. Please use the same to login"
    otp_random = pyotp.random_base32()
    user.otp_random = otp_random
    otp_obj = pyotp.TOTP(otp_random)
    user.last_otp_generation = str(time_now)
    otp = otp_obj.now()
    publish_otp(user=user, otp=otp)
    user.save()
    message = "Your OTP sent Successfully. ({})".format(otp)
    return True, message


def validate_otp(user, otp):
    user_random = user.otp_random
    if not user_random:
        print("User has never been sent an OTP !!!")
        return False
    otp_obj = pyotp.TOTP(user_random)
    if otp_obj.verify(str(otp).strip(), valid_window=2) is True:
        user.last_successful_auth = str(int(time.time()))
        user.save()
        return True
    else:
        return False
