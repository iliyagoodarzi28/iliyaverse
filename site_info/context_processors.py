
from .models import SiteInfo  
def site_info(request):
    return {
        'site_info': SiteInfo.get_info(),
    }