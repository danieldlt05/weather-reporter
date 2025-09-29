import os
import csv
import json
import requests

def load_api_key(filename="weather_key.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().strip()

def get_valid_city(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty. Please enter valid city.")

def get_weather(city, api_key):
    """Return a dict of weather fields or None on error."""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response  = requests.get(base_url, params=params)
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None
    
    if not response.ok:
        print(f"Error fetching weather data: {response.status_code}")
        return None
    
    # Use the json library
    data = json.loads(response.text)

    # Some API errors return 200 but include an error code in JSON
    if data.get("cod") != 200:
        print(f"API error: {data.get('message', 'Unknown error')}")
        return None
    
    return {
        "City": data["name"],
        "Country": data["sys"]["country"],
        "Temperature": data["main"]["temp"],
        "Humidity": data["main"]["humidity"],
        "Description": data["weather"][0]["description"],

    }

def write_to_csv(row, filename="city_data.csv"):
    """Append one row to CSV; write header only if file is empty."""
    headers = ["City", "Country", "Temperature", "Humidity", "Description"]
        
    file_exists = os.path.exists(filename)
    need_header = True
    if file_exists and os.path.getsize(filename) > 0:
        need_header = False
    
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if need_header:
            writer.writeheader()
        writer.writerow(row)

def read_from_csv(filename="city_data.csv"):
    """Read CSV and print a simple summary."""
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("\nNo data saved yet.")
        return
    
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    print(f"\nNumber of cities saved: {len(rows)}")
    for r in rows:
        print(f"- {r['City']}: {r['Temperature']}ºC")

if __name__ == "__main__":
        try:
            API_KEY = load_api_key()
            
            city = get_valid_city("Enter city name: ")
            print(f"You entered: {city}.")

            weather = get_weather(city, API_KEY)
            if not weather:
                # Stop if it could not fetch valid data
                raise SystemExit
            
            print("\n--- Weather Report ---")
            print(f"City: {weather['City']}, {weather['Country']}")
            print(f"Temperature: {weather['Temperature']}ºC")
            print(f"Humidity: {weather['Humidity']}%")
            print(f"Condition: {weather['Description'].capitalize()}")
            print("-----------------------")

            write_to_csv(weather)
            read_from_csv()

        except KeyboardInterrupt:
            print("\nCancelled by user.")
