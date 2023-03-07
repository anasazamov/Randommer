import requests
from randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        url=self.base_url+"Name"
        a={"X-Api-Key":api_key}
        p={"quantity":quantity,
           "nameType":nameType
           }
        response=requests.get(url,params=p,headers=a).json()
        return response
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        url=self.base_url+"Name/Suggestions"
        a={"X-Api-Key":api_key}
        p={"startingWords":startingWords,
           
           }
        response=requests.get(url,params=p,headers=a).json()
        return response
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        url=self.base_url+"Name/Cultures"
        a={"X-Api-Key":api_key}
       
           
           
        response=requests.get(url,headers=a).json()
        return response