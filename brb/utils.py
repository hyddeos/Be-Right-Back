from .models import Away
from django.utils import timezone
from django.utils.timezone import timedelta

def auto_off(object):
    # Auto removes Active away status if too long time has past.
    # To prevent for message staying on site if user has forgotten to remove away message manually.
    
    safety_time = 1 # How many hours to wait after estimated Return_time has pasted
    current_datetime = timezone.localtime(timezone.now())
    remove_time = object.return_time + timedelta(hours=safety_time)
    
    if current_datetime > remove_time or current_datetime.date()!= object.creation_time.date():
        object.active = False
        object.save()
        return True
    
    return None
    
