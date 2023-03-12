## does a neqs fetch for the headlines
import network  
import urequests 


wlan = network.WLAN(network.STA_IF)
wlan.active(True)


ssid = 'Sterling406'
password = 'Welcome406'
wlan.connect(ssid, password)



print("Querying for news..")

url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=919a8ccccf0f42fda7742752971a34c4'

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'hutchenaustin@gmail.com'  # This is another valid field
}

response = urequests.get(url, headers=headers)
print(response.text)
