import requests
import jsonpath
import json
import random
from Utils import urls


def test_add_new_data():
    App_url="http://thetestingworldapi.com/api/studentsDetails"
    #App_url=urls.basic_url+urls.url_students
    f = open('/Users/oleksandrlitvincuk/Desktop/Python/API/JSONs/qwerty.json', 'r')
    request_json=json.loads(f.read())
    name_student = ['Sasha', 'John', 'David']
    request_json['first_name'] = random.choice(name_student)

    response=requests.post(App_url,request_json)
    assert 201 == response.status_code
    print(response.text)
    id=jsonpath.jsonpath(response.json(), 'id')
    print('my number is',id[0])

    techapi_url = "http://thetestingworldapi.com/api/technicalskills"
    #techapi_url=urls.basic_url+urls.tech_url
    f = open('/Users/oleksandrlitvincuk/Desktop/Python/API/JSONs/querty2.json')
    request_json = json.loads(f.read())
    name_student = ['Sasha', 'John','David']
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    request_json['first_name'] = random.choice(name_student)
    response = requests.post(techapi_url, request_json)
    assert 200 == response.status_code
    print(response.text)

    addres_url = "http://thetestingworldapi.com/api/addresses"
    #addres_url =urls.basic_url+urls.add_url
    f = open('/Users/oleksandrlitvincuk/Desktop/Python/API/JSONs/qwerty3.json')
    request_json = json.loads(f.read())
    response = requests.post(addres_url, request_json)
    print(response.text)
    #assert 201 == response.status_code


    #final_detal="http://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    final_detal = urls.basic_url + urls.url_students + str(id[0])
    response = requests.get(final_detal)
    assert 200 == response.status_code
    print(response.text)
    print(response.status_code)



