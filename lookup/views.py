#this is my views.py file
from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests


	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=2CBB98BF-3C6C-4352-A69D-D58A3C74CDFF")
	#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=~distance~&API_KEY=2CBB98BF-3C6C-4352-A69D-D58A3C74CDFF
	try:
    	 api = json.loads(api_request.content)
	except Exeption as e:
    	 api = "Error..."

	return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})

