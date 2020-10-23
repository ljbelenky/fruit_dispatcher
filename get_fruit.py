import pandas as pd
import json
import numpy as np 
import requests

class FruitData:
    def __init__(self):
        self.set_address()

    def set_address(self):

        while True:
            
            try:
                address = input('Web address (or "stop"): ')
                if address.lower().strip() == 'stop':
                    break
                self.address = 'http://' + address.replace('http://', '')
                
                if requests.get(self.address).status_code == 200:
                    break
            except:
                pass


    @property
    def data(self):
            try:
                data = requests.get(self.address).json()
                data = pd.Series(data)
                print(data)
                return data

            except:
                self.set_address()


if __name__ == '__main__':

    f = FruitData()    
    while True:
        data = f.data
        if input('\n Next (or "stop")').lower().strip() == 'stop':
            break



