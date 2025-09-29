# Weather Reporter

A Python program that:
- Prompts the user for a city name (with input validation).
- Fetches current weather data from the OpenWeatherMap API.
- Displays a formatted weather report in the terminal.
- Saves the results to a CSV file ('city_data.csv').
- Reads back the CSV to show a summary of saved cities.

## Features

- Input Validation
- API Interaction
- File I/O
- PEP 8 Compliance
- requests, json, and csv Libraries

## How It Works

1. **Validate** user input until a non-empty city is entered ('get_valid_city').
2. **Request** weather data from the OpenWeatherMap API ('get_weather').
3. **Parse** the JSON response to extract city, country, temperature, humidity, and description ('get_weather').
4. **Write** the weather information as a new row in 'city_data.csv' ('write_to_csv').
5. **Read** the CSV file back and count/display all saved cities ('read_from_csv').
6. **Report** the current city's weather in a formatted summary ('__main__' section).

## How to Perform
Follow these steps to set up and run the program:
1. **Install dependencies**
- Make sure Python 3.9+ is installed. Then install the 'requests' library:
'''bash
pip install requests
2. **Get an API key
- Sign up at OpenWeatherMap.org
- Copy your personal API key.
3. Save the API key securely
- Create a file named weather_key.txt in the project folder.
- Paste only your API key inside (no quotes or extra spaces).
- Add weather_key.txt to your .gitignore so it is not shared on GitHub.
4. Run the program
- From the terminal, navigate to your project folder and run:
python reporter.py
5. Interact with the program
- Enter a city name when prompted.
- View the weather report in the terminal.
- Check city_data.csv to see all saved cities.

## Where to Watch Explanation
