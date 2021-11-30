from json.decoder import JSONDecodeError
from httpx import get

class poke_client:  

    base_url = 'https://pokeapi.co/api/v2/'

    def poke_name_by_id(self,number:int)->str:
        try:
            return get(f"{poke_client.base_url}pokemon/{str(number)}").json()["name"]
        except JSONDecodeError:
            return "No Such Pokemon with that id"

    def poke_id_by_name(self,name:int)->str:
        try:
            return get(f"{poke_client.base_url}pokemon/{str(name)}").json()['id']
        except JSONDecodeError:
            return "No Such Pokemon with that name"
