from django.shortcuts import render
from django.utils import timezone
from uc.models import UnderConstruction
from decouple import config

class UnderConstructionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # print("One Time Initialization")

    # def __call__(self, request):
        
    #     print("this is before view")

    #     # response = self.get_response(request)
    #     response = render(request, 'uc/underc.html')
    #     print("this is after view")

    #     return response
    
    
    def __call__(self, request):
        #staff see the real site, and the admin login page must always open
        if request.user.is_staff or request.path.startswith('/admin/'):
            return self.get_response(request)
        
        uc_key = config("MAINTENANCE_BYPASS_KEY")
        
        if 'u' in request.GET and request.GET['u'] == uc_key:
            request.session['bypass_maintenance'] = True
            
        if request.session.get('bypass_maintenance'):
            return self.get_response(request)

        uc = UnderConstruction.objects.first()
        #no end time = stays on until unticked; past end time = site is live again
        if uc and uc.is_under_construction:
            context = {
                "uc_note": uc.uc_note,
                "uc_duration" :uc.uc_duration
            }
            return render(request, 'uc/underc.html', {'uc': uc})

        return self.get_response(request)
