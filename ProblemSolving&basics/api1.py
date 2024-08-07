import requests
#from requests.packages.urllib3.exceptions import InsecureRequestWarning

#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
response = requests.post("https://api.thecatapi.com/v1/breeds/abys", verify = False)
print(response.status_code)
#print(response.text)
print(response.headers)
print(response)
#print(response.json)
{'photos': {'id': 754118,
   'sol': 2809,
   'camera': {'id': 20,
    'name': 'FHAZ',
    'rover_id': 5,
    'full_name': 'Front Hazard Avoidance Camera'},
   'img_src': 'https://mars.nasa.gov/msl-raw-images/...JPG',
   'earth_date': '2020-07-01',
   'rover': {'id': 5,
    'name': 'Curiosity',
    'landing_date': '2012-08-06',
    'launch_date': '2011-11-26',
    'status': 'active'}},
  
}




