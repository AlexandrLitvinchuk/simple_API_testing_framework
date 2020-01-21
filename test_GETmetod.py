import requests


def test_rrrr():
    final_detal="http://thetestingworldapi.com/api/studentsDetails/1234"
    #final_detal = urls.basic_url+urls.url_students+str(id[0])
    response = requests.get(final_detal)
    assert 200 == response.status_code

    print('this is',response.text)