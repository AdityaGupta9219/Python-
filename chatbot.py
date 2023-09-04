import requests

url = "https://text-analysis12.p.rapidapi.com/language-detection/api/v1.1"

payload = { "text": "Hello how are you? Have you heard about SpaceX?" }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "c402d34ca1mshc77150e96ed43a2p12b136jsnf46e8cfb7772",
	"X-RapidAPI-Host": "text-analysis12.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())