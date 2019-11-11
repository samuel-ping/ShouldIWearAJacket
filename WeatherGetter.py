import http.client

conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")
myKey = input("Enter your unique RapidAPI key: ")
headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': myKey # you need a unique rapidAPI key to use this
    }

# city = input("Enter your city: ")
# country = input("Enter your country: ")
zip = input("Enter your zipcode: ")

conn.request("GET", "/weather?units=%22imperial%22&mode=xml%2C%20html&q="+zip+"%2Cus", headers=headers)

res = conn.getresponse()
data = res.read().decode("utf-8")

startIndex = 15 + data.find('"main":{"temp":')
endIndex = data.find(',"pressure"')
temperature = float(data[startIndex:endIndex])
# print(temperature)
FTemp = (temperature-273.15)*(9.0/5.0)+32
# print(FTemp)
print("The current temperature is "+str(round(FTemp,2))+" degrees Fahrenheit. ")
if FTemp>67:
    print("You don't need a jacket.")
elif FTemp>57:
    print("A light jacket should be fine.")
elif FTemp>50:
    print("It's a little cold, so wear a warm jacket.")
elif FTemp>30:
    print("It's really cold! Wear a heavy jacket!")
elif FTemp>0:
    print("Holy jeezers its freezing! Bundle up!")
else:
    print("Are you climbing Mount Everest?")
