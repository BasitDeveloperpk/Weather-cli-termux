import os
import requests

API_KEY_FILE = os.path.expanduser("~/.weather_api_key")

def get_api_key():
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, 'r') as f:
            return f.read().strip()
    else:
        print("🔑 Pehli dafa API key chahiye (OpenWeatherMap se).")
        key = input("➡️  API key daalein: ").strip()
        if key:
            with open(API_KEY_FILE, 'w') as f:
                f.write(key)
            print("✅ API key save ho gayi.")
            return key
        else:
            print("❌ API key nahi mili.")
            return None

def main():
    print("\n╔══════════════════════════════════╗")
    print("║     🌦️  WEATHER CHECK TOOL CLI     ║")
    print("╚══════════════════════════════════╝\n")

    city = input("🏙️  Shehar ka naam likho: ").strip()
    api_key = get_api_key()

    if not city or not api_key:
        print("\n⚠️  Shehar ya API key missing hai.")
        return

    print("\n🔄 Weather data laa rahe hain...\n")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description'].title()
            humidity = data['main']['humidity']
            wind = data['wind']['speed']

            print("📊 Weather Report:")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"📍 Shehar       : {city}")
            print(f"🌡️  Darja Hararat: {temp}°C")
            print(f"🌥️  Mausam       : {desc}")
            print(f"💧 Humidity     : {humidity}%")
            print(f"💨 Wind Speed   : {wind} m/s")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
        elif response.status_code == 404:
            print("❌ Galat shehar ka naam. Dubara koshish karein.")
        else:
            print(f"❌ API se kuch error aayi (Code: {response.status_code})")
    except Exception as e:
        print("🚫 Network ya API issue:", e)

if __name__ == "__main__":
    main()
