import requests
import json
import random
from Utils import urls


class Metods():

    #id = jsonpath.jsonpath(response.json(), 'id')

    @staticmethod
    def post_student():
        App_url = urls.basic_url + urls.url_students
        f = open('/Users/oleksandrlitvincuk/Desktop/Python/API/JSONs/qwerty.json', 'r')
        request_json = json.loads(f.read())
        name_student = ['Sasha', 'John', 'David']
        request_json['first_name'] = random.choice(name_student)

        response = requests.post(App_url, request_json)
        return response


    @staticmethod
    def post_skils():
        # techapi_url = "http://thetestingworldapi.com/api/technicalskills"
        techapi_url = urls.basic_url + urls.tech_url
        f = open('/Users/oleksandrlitvincuk/Desktop/Python/API/JSONs/querty2.json')
        request_json = json.loads(f.read())
        #request_json['id'] = int(id[0])
        #request_json['st_id'] = id[0]
        #request_json['first_name'] = random.choice(name_student)
        response = requests.post(techapi_url, request_json)
        return response

    @staticmethod
    def post_adres():
        addres_url = urls.basic_url + urls.add_url
        f = open('/Users/oleksandrlitvincuk/Desktop/Python/API/JSONs/qwerty3.json')
        request_json = json.loads(f.read())
        response = requests.post(addres_url, request_json)
        return response

    @staticmethod
    def get_final_detail():

        #final_detal = urls.basic_url+urls.url_students
        final_detal = "http://thetestingworldapi.com/api/studentsDetails/155401"
        response = requests.get(final_detal)
        return response