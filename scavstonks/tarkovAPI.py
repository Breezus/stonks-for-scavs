import configparser
import requests
import os


class tarkovAPI:
    def __init__(self, api) -> None:
        config = configparser.ConfigParser()
        config.read(os.path.dirname(__file__) + '/conf.ini')
        self.url = config.get(api, 'url')
        self.attribute = config.get(api, 'response')
        self.headers = {'content-type': 'application/json'}


    def run_query(self, query):
        response = requests.post(
            self.url,
            headers=self.headers,
            json={'query': query}
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))
