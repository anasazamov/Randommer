import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        url=self.base_url+"Misc/Cultures"
        a={"X-Api-Key":api_key}
        response=requests.get(url,headers=a).json()
        return response
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        url=self.base_url+"Misc/Cultures"
        a={"X-Api-Key":api_key}
        p={"culture":culture,
           "number":number
           }
        response=requests.get(url,params=p,headers=a).json()
        return response
