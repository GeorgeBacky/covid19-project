from django.shortcuts import render
import requests
import json

url = "https://rapidapi.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "3fb70290famsh4ee6af91c3e39cfp1f3446jsnecaaece2f9d1"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.

def indexview(request):
    noofresults = int(response['results'])
    mylist = []
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])
    if request.method == "POST":   
        selectedcountry = request.POST['selectedcountry']
        noofresults = int(response['results'])
        for x in range(0,noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                crtical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total =  response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'selectedcountry': selectedcountry ,'mylist': mylist,'new' : new , 'active' : active , 'critical' : crtical , 'recovered' : recovered , 'deaths' : deaths, 'total' :total}
        return render(request, 'index.html', context)
    noofresults = int(response['results'])
    mylist = []
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])
    context = {'mylist' : mylist}
    return render(request, 'index.html', context)