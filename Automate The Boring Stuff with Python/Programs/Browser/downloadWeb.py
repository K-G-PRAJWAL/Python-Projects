import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)  # Get the status of the request
badRes = requests.get('https://automatetheboringstuff.com/files/afwevwav.txt')
print(badRes.raise_for_status())  # Get any status errors if present
