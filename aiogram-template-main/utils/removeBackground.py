import logging
import requests

url = "https://remove-background-image2.p.rapidapi.com/remove-background"

headers = {
	"X-RapidAPI-Key": "72ae49e89bmsh80881d10ecadaf9p1ca149jsnee125c940742",
	"X-RapidAPI-Host": "remove-background-image2.p.rapidapi.com"
}

# response = requests.post(url, headers=headers)
#
# print(response.json())

async def remove_background(img_url):
	payload= f"image={img_url}"
	response = requests.request("POST", url, headers=headers, data=payload)
	return response.json()['response']['image_url']