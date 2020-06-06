import requests


print("...............................Made By Sabbir Hossain..............................")
city=input('Enter your city name:')
url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=975154a1d4adacf218847495eead535e&units=metric'.format(city)
res=requests.get(url)
data=res.json()
temp=data['main']['temp']
wind=data['wind']['speed']
des=data['weather'][0]['description']

print("Todays Temperature:",temp)
print("Wind Speed:",wind)
print("Weather description:",des)

et=int(input("Enter 1 to exit:"))
if et==1:
    exit()
else:
    print("Enter the correct number")

