import json
import requests

class EVNotify:
    
    def __init__(self, akey = None, token = None):
        self.RESTURL = 'https://app.evnotify.de/'
        self.akey = akey
        self.token = token

    def sendRequest(self, method, fnc, useAuthentication = False, params = {}):
        return getattr(requests, method)(self.RESTURL + fnc, json=params).json()

    def getKey(self):
        return self.sendRequest('get', 'key')['akey']

    def register(self, akey, password):
        return self.sendRequest('post', 'register', False, {
            "akey": akey,
            "password": password
        })

    def login(self, akey, password):
        return self.sendRequest('post', 'login', False, {
            "akey": akey,
            "password": password
        })