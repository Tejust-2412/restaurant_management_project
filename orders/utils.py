import string 
import secrets 
from .models import Coupon 
import logging 
from email_validator import validate_email , EmailNotValidError 


def generate_coupon_code(length = 10) :
    """Generate a unique alphanumeric coupon code """
    characters = string.ascii_uppercase + string.digits


    while True :

        code = ''.join(secrets.choice(characters) for _ in range(length))

        if not Coupon.objects.filter(code=code).exists() :
            return code



logger = logging.getLogger(__name__)

def is_valid_email(email : str) -> bool :
    try :
        validate_email(email)
        return True
    except EmailNotValidError as e :
        logger.warning(f"Invalid email attempted : {email} - {str(e)}")
        return False 