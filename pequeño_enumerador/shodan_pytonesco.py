import shodan 
import requests
#api
apie ="YgTS7cAjLb58KYQ0S43HZ6elNQWpu8Iv"

api = shodan.Shodan(apie)

ip ="34.102.242.46" 
re = f"https://api.shodan.io/shodan/host/{ip}?key={apie}"

sol = requests.get(re)

print(sol)
