import requests
import time
import os

urls = []
# urls.append({"name": "natboardhome", "url": "https://natboard.edu.in/"})
# urls.append({"name": "ceeKerala", "url": "https://cee.kerala.gov.in/main.php"})
# urls.append({"name": "arogya_karnataka", "url": "http://arogya.karnataka.gov.in/sast/fms/view.php"})
urls.append({"name": "vande_bharat_phase_5", "url": "https://mea.gov.in/phase-5.htm"})


BOT_TOKEN = os.environ['BOT_TOKEN']
url_update = (
    "https://api.telegram.org/bot"
    + BOT_TOKEN
    + "/sendMessage?chat_id=16795984&text=Site got updated:\n"
)


def check_now(a):
	url = urls[a]
	# print(url)
	res = requests.get(url["url"], verify=False)
	file_path = "contents/" + url["name"]
	try:
		f = open(file_path, "r")
		content = f.read()
		f.close()
	except:
		content = ""
	# print(content)
	result = res.text
	if content != result:
		print("Content changed for: "+url["name"])
		requests.get(url_update + url["name"] + "\n\n" + url["url"])
		f = open(file_path, "w+")
		f.write(result)
		f.close()
	else:
		print("same old: " + urls[a]["name"])


for a in range(len(urls)):
    check_now(a)
