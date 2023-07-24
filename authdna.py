import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth

USER = input('Enter your username for DNAC: ')
PASS = getpass('Enter your password for DNAC: ')

BASEURL = "https://sandboxdnac.cisco.com"
authAPI = "/dna/system/api/v1/auth/token"

payload = {}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

dnaAuth = BASEURL + authAPI

response = requests.post(dnaAuth, verify=False, auth=HTTPBasicAuth(USER, PASS), headers=headers, data=payload)

tokenJSON = response.json()

TOKEN = tokenJSON['Token']

print('Your token is:\n ' + TOKEN)

