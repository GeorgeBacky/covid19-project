from django.shortcuts import render
import requests
import json
import asyncio

url = "https://rapidapi.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "3fb70290famsh4ee6af91c3e39cfp1f3446jsnecaaece2f9d1"
    }


covid_response = requests.request("GET", url, headers=headers).json()

async def data_reloader():
    await asyncio.sleep(300)
    covid_response = requests.request("GET", url, headers=headers).json()

data_reloader()

# Create your views here.
def indexview(request):
    covid_data = covid_response['response']
    noofresults = int(covid_response['results'])
    countries = []
    for result in covid_data:
        countries.append(result['country'])
    countries.sort()
    context = {
        'mylist': countries
    }

    if request.POST and request.POST['selectedcountry']:
        selectedcountry = request.POST['selectedcountry']
    else:
        selectedcountry = "All"

    for result in covid_data:
        if selectedcountry == result['country']:
            new = result['cases']['new']
            active = result['cases']['active']
            critical = result['cases']['critical']
            recovered = result['cases']['recovered']
            total =  result['cases']['total']
            deaths = result['deaths']['total']
    context.update({'selectedcountry': selectedcountry, 'new' : new , 'active' : active , 'critical' : critical , 'recovered' : recovered , 'deaths' : deaths, 'total' :total})
    return render(request, 'index.html', context)