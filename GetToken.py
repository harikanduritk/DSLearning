import requests
import json
import requests as req
import  sys
import os


class GetToken:
    # hardcode the url to our APIs - Lets Try get API and then with parameter.
    token_url = 'https://login.microsoftonline.com/common/oauth2/token'

    payload = {
        'client_id': '271cc4b7-79b8-46a2-8973-158d29645c9b',
        'client_secret': 'I?92BDyMQucSIvs=eX5Xwbp4Cm-=d7xm',
        'grant_type': 'password',
        'UserName': 'IMPACT.COT.user9@pxlawecidcdpaad.onmicrosoft.com',
        'Password': 'IMPACT.COT.UI@user9x',
        'scope': '718856f4-ab9b-4f1c-bf7f-1dbdaa5222c9',
        'resource': '718856f4-ab9b-4f1c-bf7f-1dbdaa5222c9'}

    # Constructor
    def __init__(self):
        self.request_timeout = 120
        self.session = requests.Session()
        self.token_url = 'https://login.microsoftonline.com/common/oauth2/token'

    def _getToken(self):
        try:
            r = req.post(self.token_url, self.payload)
            content = json.loads(r.content.decode('utf-8'))
            self._writeToken(content)
            return r
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")

    def _writeToken(self,str):
        path = os.path.join(os.getcwd(), 'token.txt')
        json_object = json.dumps(str, indent=4)
        with open(path, 'w') as f:
            f.write(json_object)

