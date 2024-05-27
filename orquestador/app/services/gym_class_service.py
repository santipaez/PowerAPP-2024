import requests

class GymClassService:
    def __init__(self):
        self.base_url = 'http://localhost:5003'

    def get_data(self):
        response = requests.get(f'{self.base_url}')
        if response.status_code != 200:
            self.get_compensation()
        else :
            raise Exception(response.json())
        
    def get_compensation(self):
        response = requests.get(self.base_url + 'compensation')
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.json())
