import requests
import time

class checkconnection:
    
    def check_conn(self):
        print('executando check_conn')
        url = "https://www.google.com"
        timeout = 2
        try:
            request = requests.get(url, timeout=timeout)
            print(request)
            return 200
        except (requests.ConnectionError, requests.Timeout) as exception:
            print('No internet available; trying reconnection...')
            time.sleep(5)
            self.repeat()
    
    def repeat(self):
        return self.check_conn()