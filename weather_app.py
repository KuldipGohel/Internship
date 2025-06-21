import requests

def get_weather(city):
    api_key = "82bd833718d914c0a0b89308e46ef228" 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {city}:")
        print("Temperature:", data['main']['temp'], "°C")
        print("Condition:", data['weather'][0]['description'].title())
    else:
        print("City not found or API error...!!")

if __name__ == "__main__":
    while True:
        city = input("\nEnter city name (or type 'EXIT' to quit): ")
        if city.lower() == "exit":
            break
        get_weather(city)
