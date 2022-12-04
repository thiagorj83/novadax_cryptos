import requests
import json


class getsymbols:
    def get_symbols(self):
        symbols=[]
        try:
            req=requests.get("https://api.novadax.com/v1/common/symbols")
            symbols=json.loads(req.content)
            return symbols
        except Exception as e:
            print(e)