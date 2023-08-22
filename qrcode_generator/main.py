import requests

url = input("Which url do you want to link to the qr code? ")

request_url = f"https://qrtag.net/api/qr.png?url={url}"
response = requests.get(request_url)

print(f"QR Code: {request_url}")


