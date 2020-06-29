from django.shortcuts import render


# Create your views here.

def default_map(request):
    mapbox_access_token = 'pk.<your_api_token>'
    return render(request, 'default.html', {'mapbox_access_token': mapbox_access_token})
