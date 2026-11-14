from django.views.generic import TemplateView

class AboutTemplateView(TemplateView):
    template_name = 'myapp/about.html'
    
    
# class ContactTemplateView(TemplateView):
#     template_name = 'myapp/contact.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['name'] = 'zarish'
#         context['roll'] = 101
        
#         return context
    
    
class ProfileTemplateView(TemplateView):
    template_name = 'myapp/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'zarish'
        
        return context
    