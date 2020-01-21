from Utils.metods import Metods


class Test_end_to_end():
    @staticmethod
    def test_new_student():
        response=Metods.post_student()
        assert 201 == response.status_code
        print(response.status_code)
        print(response.text)
    @staticmethod
    def test_new_skils():
        response=Metods.post_skils()
        assert 200 == response.status_code
        print(response.text)
    @staticmethod
    def test_new_addres():
        response=Metods.post_adres()
        assert  201 == response.status_code
        print(response.text)

    @staticmethod
    def test_get_final_detail():
        response=Metods.get_final_detail()
        print(response.status_code)
        print(response.text)
        assert 200 == response.status_code
        #print(response.status_code)



