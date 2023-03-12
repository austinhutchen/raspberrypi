
import network  
import urequests 


wlan = network.WLAN(network.STA_IF)
wlan.active(True)


ssid = 'Sterling406'
password = 'Welcome406'
wlan.connect(ssid, password)



print("1. Querying google.com:")
r = urequests.get("http://www.google.com")
print(r.content)