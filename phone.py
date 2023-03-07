import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        url=self.base_url+"Name/Businessname"
        a={"X-Api-Key":api_key}
        p={"CountryCode":CountryCode,"Quantity":Quantity
           
           }
        response=requests.get(url,params=p,headers=a).json()
        return response
    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        url=self.base_url+"Phone/IMEI"
        a={"X-Api-Key":api_key}
        p={"Quantity":Quantity
           
           }
        response=requests.get(url,params=p,headers=a).json()
        return response
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        url=self.base_url+"Name/Businessname"
        a={"X-Api-Key":api_key}
        p={"CountryCode":CountryCode,"telephone":telephone
           
           }
        response=requests.get(url,params=p,headers=a).json()
        return response
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        url=self.base_url+"Phone/Countries"
        a={"X-Api-Key":api_key}
        
           
           
        response=requests.get(url,headers=a).json()
        return response
