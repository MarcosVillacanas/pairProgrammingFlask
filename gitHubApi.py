#python -m venv myVenv
#. .\myVenv\Scripts\activate.ps1
#Get-Command pip
#pip freeze

from getpass import getpass
import requests

response = requests.get('https://api.github.com/repos/pallets/flask/issues', auth=('MarcosVillacanas', "21312b6c7ef3b5a8ae8662840447d1f40e317ef8"))

print(response.text)


#Evitar pip._vendor
