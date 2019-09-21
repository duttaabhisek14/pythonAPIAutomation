import requests
import json
token_url = "https://accounts-devsp.zeomega.org/oauth2/token"
data = {'grant_type': 'password', 'username': 'zeomega.com/zeadmin', 'password': 'Jiva@123', 'scope': 'mgc'}
access_token = requests.post(token_url, data=data,
                             headers={'Authorization': 'Basic MkQ1eVN2eWw1aFE1T2Q3ampCT2RscEw3bldFYToxazRDVzE5dVE2dVF5ZjBlTFZQQnQ2ZDR1WXdh'})
print(access_token)
tok=access_token.json()['access_token']
print(access_token.headers)
#print(access_token.text)
token1 = 'Bearer ' + tok
print(token1)