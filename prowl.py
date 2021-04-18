import requests


class Prowl:
    def __init__(self, apikey):
        self.apikey = apikey

    def send_notification(self, message):
        data = {'apikey': self.apikey,
                'application': 'Corona Zahlen',
                'event': message}

        response = requests.post('https://api.prowlapp.com/publicapi/add', data=data,
                                 headers={'Content-type': 'application/x-www-form-urlencoded'})
        return response.status_code
