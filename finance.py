import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        url=self.base_url+"Finance/CryptoAdress/Types"
        h={"X-Api-Key":api_key}
        
        return requests.get(url,headers=h).json()
        

    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        url=self.base_url+"Finance/CryptoAdress"
        a={"X-Api-Key":api_key}
        t={"cryptoType":crypto_type}
        response=requests.get(url,params=t,headers=a).json()
        return response

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        url=self.base_url+"/Finance/Countries"
        a={"X-Api-Key":api_key}
        
        response=requests.get(url,headers=a).json()
        return response

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        url=self.base_url+"Finance/Countries"
        a={"X-Api-Key":api_key}
        t={"countryCode":country_code}
        response=requests.get(url,params=t,headers=a).json()
        return response
    
c=Finance()

print(c.get_iban_by_country_code("AL","48db25ad935a4a5c82c72db9260b214f"))