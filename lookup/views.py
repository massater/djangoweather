from django.shortcuts import render
import json
import requests  # Need to pip install
# Create your views here.

# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=C3129F0B-C4D5-49D6-8124-F9C3C2CD0245

def home(request):
    key = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=C3129F0B-C4D5-49D6-8124-F9C3C2CD0245"


    if request.method == "POST":
        zipcode = request.POST['zipcode']
        key = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=C3129F0B-C4D5-49D6-8124-F9C3C2CD0245"
        api_request = requests.get(key)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'lookup/home.html', {'api': api, 'x': api[0], 'zipcode': zipcode})
    else:
        try:
            api_request = requests.get(key)
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'lookup/home.html', {'api': api, 'x': api[0]})

def about(request):
    return render(request, 'lookup/about.html', {})
