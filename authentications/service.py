import random
from authentications import models



class OtpService:

    @staticmethod
    def create_otp_random_code():
        return str(random.randint(100000,999999))

    @staticmethod
    def create_otp(user,purpose):
        otp=models.OTP.objects.filter(user=user,purpose=purpose)
        if otp:
            otp.delete()

        return models.OTP.objects.create(user=user,purpose=purpose,code=OtpService.create_otp_random_code())
       

    @staticmethod
    def otp_match(user,purpose,code):
        otp = models.OTP.objects.filter(user=user,purpose=purpose,code=code).first()
        if otp.is_expired():
            otp.delete()
            return False

        otp.delete()
        return True