from django.shortcuts import render, get_object_or_404
from .models import Tab

def home(request, slug=None):
    tabs = Tab.objects.filter(is_active=True).order_by('order')
    current_tab = tabs.first() if not slug else get_object_or_404(Tab, slug=slug, is_active=True)
    return render(request, 'main/home.html', {
        'tabs': tabs,
        'current_tab': current_tab,
    })
